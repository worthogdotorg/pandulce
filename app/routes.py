from app.forms import breadcalcinput, recipeinput, recipeoutput, recipesamples
from app import app
from flask import render_template, session, url_for, redirect, request, flash
from app import themath

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = breadcalcinput()
    
    #if form.validate_on_submit():
    if request.method == "POST":   
        if request.form["levain_units_calc"]=="gm":
            session['levain_units_calc'] = "grams"
        else:
            session['levain_units_calc'] = "ounces"
        session['flour_qty_recipe'] = request.form["flour_qty_recipe"]
        session['water_qty_recipe'] = request.form["water_qty_recipe"]
        session['levain_qty_recipe'] = request.form["levain_qty_recipe"]
        session['levain_hyd_recipe'] = request.form["levain_hyd_recipe"]
        session['levain_hyd_yours'] = request.form["levain_hyd_yours"]
        return redirect('/breadcalctable')
   
    return render_template('index.html', form=form)

@app.route('/breadcalctable', methods=['GET', 'POST'])
def breadcalctable():
    # These are session variables
    ingredients_calc = dict()
    ingredients_calc['levain_units'] = session['levain_units_calc']
    ingredients_calc['flour_qty_recipe'] = flour_qty_recipe = session['flour_qty_recipe']
    ingredients_calc['water_qty_recipe'] = water_qty_recipe = session['water_qty_recipe']
    ingredients_calc['levain_qty_recipe'] = levain_qty_recipe = session['levain_qty_recipe']
    ingredients_calc['levain_hyd_recipe'] = levain_hyd_recipe = session['levain_hyd_recipe'] 
    ingredients_calc['levain_hyd_yours'] = levain_hyd_yours = session['levain_hyd_yours'] 
    
    # These are calculations for original recipe
    ingredients_calc['dough_weight'] = int(flour_qty_recipe) + int(water_qty_recipe) + int(levain_qty_recipe)
    # pff is prefermented flour
    ingredients_calc['pff'] = pff = int(themath.levain_flour_qty_fnc(int(levain_qty_recipe),int(levain_hyd_recipe) / 100))
    flour_total = pff + int(flour_qty_recipe)
    ingredients_calc['levain_water_recipe'] = levain_water_recipe = int(themath.levain_water_qty_fnc(int(levain_qty_recipe),int(levain_hyd_recipe) / 100))
    ingredients_calc['water_total'] = water_total = int(water_qty_recipe) + levain_water_recipe
    ingredients_calc['water_bakers_pct'] = round(water_total /  flour_total * 100)
    ingredients_calc['water_recipe_bakers_pct'] = round(int(water_qty_recipe) /  flour_total * 100)
    ingredients_calc['flour_total'] = flour_total = pff + int(flour_qty_recipe)
    ingredients_calc['flour_recipe_bakers_pct'] = round(int(flour_qty_recipe) /  flour_total * 100)
    ingredients_calc['levain_bakers_pct'] = round(int(levain_qty_recipe) /  flour_total * 100)
    ingredients_calc['pff_bakers_pct'] = round(pff / flour_total * 100)
    ingredients_calc['levain_water_bakers_pct'] = round(levain_water_recipe / flour_total * 100)
    ingredients_calc['dough_hydration_recipe'] = round(water_total / flour_total * 100)

    #
    # These are calculations for adjusted recipe
    #

    ingredients_calc['levain_water_adjusted'] = levain_water_adjusted = int(themath.levain_water_adjusted(pff, int(levain_hyd_yours) / 100))
    ingredients_calc['levain_water_adjusted_bakers_pct'] = round(levain_water_adjusted / flour_total * 100)
    ingredients_calc['water_qty_adjusted'] = water_qty_adjusted = int(water_total - levain_water_adjusted)
    ingredients_calc['water_adjusted_bakers_pct'] = round(water_qty_adjusted /  flour_total * 100)
    ingredients_calc['levain_qty_adjusted'] = levain_qty_adjusted = levain_water_adjusted + pff
    ingredients_calc['levain_adjusted_bakers_pct'] = round(int(levain_qty_adjusted) /  flour_total * 100)
    ingredients_calc['flour_qty_adjusted'] = flour_qty_adjusted = flour_total - pff 
    ingredients_calc['flour_adjusted_bakers_pct'] = round(int(flour_qty_adjusted) /  flour_total * 100)

    return render_template('breadcalctable.html', **ingredients_calc)  


# 
# Below is code for sourdough discard calculator
#

def ingredients_dict(ingredients):
   
    flour_qty = int(ingredients['flour_qty'])
    water_qty = int(ingredients['water_qty'])
    dairy_qty = int(ingredients['dairy_qty'])
    levain_hyd = int(ingredients['levain_hyd']) / 100
    levain_pct = int(ingredients['levain_pct']) / 100
    dough_weight = flour_qty + water_qty + dairy_qty
    
    levain_qty = int(themath.sourdough_qty_fnc(levain_pct, dough_weight))
          
    levain_water = int(themath.levain_water_qty_fnc(levain_qty, levain_hyd))
    if levain_water > water_qty:
        levain_water = water_qty
        levain_pct = ingredients['levain_pct'] = themath.sourdough_pct_adjust_fnc(levain_water, levain_hyd, dough_weight)
        levain_qty = int(themath.sourdough_qty_fnc(levain_pct, dough_weight))
        flash("Can't maintain bakers percentages. Constraining max sourdough quantity as shown in the Adjusted Recipe.")
        if dairy_qty > 0:
            flash("Can't maintain bakers percentages. Constraining max sourdough quantity as shown in the Adjusted Recipe.")
            flash("I see you have a quantity of dairy. Click on Help for more information.")



    ingredients['levain_qty'] = levain_qty  
    ingredients['old_levain_pct'] = int(levain_pct * 100)
    
    ingredients['levain_flour'] = int(themath.levain_flour_qty_fnc(levain_qty, levain_hyd))
    ingredients['levain_water'] = int(levain_qty - ingredients['levain_flour'])
    
    ingredients['new_flour_qty'] = round(flour_qty - ingredients['levain_flour'])
    ingredients['new_water_qty'] = round(water_qty - ingredients['levain_water'])

    # Divide by itself, to set up for future varying flour types
    ingredients['flour_pct'] = int(flour_qty / flour_qty * 100)
    ingredients['new_flour_pct'] = round(ingredients['new_flour_qty'] / flour_qty * 100) 
    
    ingredients['water_pct'] = int(water_qty / flour_qty * 100)
    ingredients['new_water_pct'] = int(ingredients['new_water_qty'] / flour_qty * 100)
    
    # Maintain dairy pct but add flash if exceeding total H2O
    ingredients['dairy_pct'] = int(dairy_qty / flour_qty * 100)
    ingredients['new_dairy_qty'] = dairy_qty

    return(ingredients)


@app.route('/discard', methods=['GET', 'POST'])
def discard():
    form = recipeinput()
    
    #if form.validate_on_submit():
    if request.method == "POST":
        #flash("Test from index.")       
        session['recipe_name'] = request.form["recipe_name"]
        if request.form["levain_units"]=="gm":
            session['levain_units'] = "grams"
        else:
            session['levain_units'] = "ounces"
        session['flour_qty'] = request.form["flour_qty"]
        session['water_qty'] = request.form["water_qty"]
        session['dairy_qty'] = request.form["dairy_qty"]
        #session['recipe_notes'] = request.form["recipe_notes"]
        session['levain_hyd'] = request.form["levain_hyd"]
        session['levain_pct'] = request.form["levain_pct"]
        return redirect('/newrecipe')
    return render_template('discard.html', form=form)


@app.route('/newrecipe', methods=['GET', 'POST'])
def newrecipe():
    form = recipeoutput()
    
    ingredients = dict()
    ingredients['recipe_name'] = session['recipe_name']
    ingredients['levain_units'] = session['levain_units']
    ingredients['flour_qty'] = session['flour_qty']
    ingredients['water_qty'] = session['water_qty']
    ingredients['dairy_qty'] = session['dairy_qty']
    
    ingredients['levain_hyd'] = session['levain_hyd']
    
    if request.method == "POST":
        ingredients['levain_pct'] = request.form['levain_pct']
        ingredients['recipe_notes'] = request.form['recipe_notes']
    else:
        ingredients['levain_pct'] = int(session['levain_pct'])
                                   
    ingredients_dict(ingredients)
   
    if ingredients['new_flour_qty'] < 0:
        flash("Discard percentage was too high for a recipe that would probably have had the consistency of quicksand. Check your recipe. Starting over.")
        return redirect('/discard')

    return render_template('newrecipe.html', form=form, title="Calculated Recipe", **ingredients)  

@app.route('/newrecipe/tortillas', methods=['GET', 'POST'])
def tortillas():  
    form = recipesamples()
    ingredients = dict()
    ingredients['levain_units'] = "ounces"
    ingredients['recipe_name'] = "Tortillas"
    ingredients['flour_qty'] = 10
    ingredients['water_qty'] = 14
    ingredients['dairy_qty'] = 0
    ingredients['recipe_notes'] = "<p>Based on the wonderful Samin Nosrat's <a href=""https://cooking.nytimes.com/recipes/1019621-sonoran-style-flour-tortillas"">recipe in the NY Times.</a></p><p><a href=""https://www.cookingcompaniontv.com/cookingcompaniontv/flourtortillas"">This video</a> offers instructions on how to prepare tortillas using Samin's recipe.  These tortillas are like those of my mama, my abuela, and <a href=""https://joyspersonalchefse.wixsite.com/joytrotter"">my niece</a>.  The smell of fresh tortillas takes me back to my childhood, anxiously waiting for the fresh tortillas to come off the griddle to be slathered with butter and devoured.  ¡Que disfrute!</p>"
    ingredients['levain_hyd'] = 100
    ingredients['levain_pct'] = 10
        
    if request.method == "POST":
        ingredients['levain_pct'] = request.form['levain_pct'] 
    
    ingredients_dict(ingredients)
 
    return render_template('newrecipe.html', form=form, title="Calculated Recipe", **ingredients)  


@app.route('/newrecipe/datenutloaf', methods=['GET', 'POST'])
def datenutloaf():  
    form = recipesamples()
    ingredients = dict()
    ingredients['levain_units'] = "grams"
    ingredients['recipe_name'] = "Date Nut Loaf"
    ingredients['flour_qty'] = 206
    ingredients['water_qty'] = 227
    ingredients['dairy_qty'] = 0
    ingredients['recipe_notes'] = "<p>Sourdough discard is brilliant in date nut loaf.  The <a href=""https://www.kingarthurbaking.com/recipes/old-fashioned-date-nut-bread-recipe"">King Arthur date nut loaf recipe</a> is a gem and marries wonderfully with starter.  You can substitute instant coffee powder or crystals for brewed coffee, adjusting the water weight accordingly.</p>"
    ingredients['levain_hyd'] = 100
    ingredients['levain_pct'] = 20
        
    if request.method == "POST":
        ingredients['levain_pct'] = request.form['levain_pct'] 
    
    ingredients_dict(ingredients)
 
    return render_template('newrecipe.html', form=form, title="Calculated Recipe", **ingredients)  


@app.route('/newrecipe/wholewheat', methods=['GET', 'POST'])
def wholewheat():  
    form = recipesamples()
    ingredients = dict()
    ingredients['levain_units'] = "Ounces"
    ingredients['recipe_name'] = "Whole Wheat Bread"
    ingredients['flour_qty'] = 28
    ingredients['water_qty'] = 10
    ingredients['dairy_qty'] = 8
    ingredients['recipe_notes'] = "A simple whole wheat, properly presented by weight, with some dairy to play around with. Find the recipe <a href=""https://www.allrecipes.com/recipe/6773/simple-whole-wheat-bread/"">here.</a>"
    ingredients['levain_hyd'] = 100
    ingredients['levain_pct'] = 25
        
    if request.method == "POST":
        ingredients['levain_pct'] = request.form['levain_pct'] 
    
    ingredients_dict(ingredients)
 
    return render_template('newrecipe.html', form=form, title="Calculated Recipe", **ingredients)  

#
#  Below is code for about and help screens
#
@app.route('/about', methods=['GET', 'POST'])
def about():  
    return render_template('about.html')

@app.route('/help', methods=['GET', 'POST'])
def help():  
    return render_template('help.html')
