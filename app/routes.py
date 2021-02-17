from app.forms import breadcalcinput, recipeinput, recipeoutput, recipesamples, bbga1input
from app import app
from flask import render_template, session, url_for, redirect, request, flash
from app import themath

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
#
# Here's the code for the BBGA calculator
#
def index():
    form = bbga1input()
    
    if request.method == "POST":   
       #if form.validate_on_submit():
       #    flash("bbga1 validated")
       #else:
       #    flash("bbga1 not validated")

        session['units'] = request.form["units"]
        
        session['bbga_recipe_name'] = request.form["bbga_recipe_name"]
        session['tdw'] = request.form["tdw"]
        session['flour1_type'] = request.form['flour1_type']
        session['flour2_type'] = request.form['flour2_type']
        session['flour3_type'] = request.form['flour3_type']
        session['flour1_pct'] = request.form['flour1_pct']
        session['flour2_pct'] = request.form['flour2_pct']
        session['flour3_pct'] = request.form['flour3_pct']
        
        session['water_pct'] = request.form["water_pct"]
        session['salt_pct'] = request.form["salt_pct"]
        session['yeast_pct'] = request.form["yeast_pct"]
        session['addin_pct'] = request.form["addin_pct"]
        session['pf1'] = request.form["pf1"]
        session['pf1_pff_pct'] = request.form["pf1_pff_pct"]
        session['pf1_water_pct'] = request.form["pf1_water_pct"]
        # But seed % is actually as a percentage in the total formula, which will be calculated below
        session['pf1_seed_pct'] = request.form["pf1_seed_pct"]
        session['pf1_salt_pct'] = request.form["pf1_salt_pct"]
        session['pf1_yeast_pct'] = request.form["pf1_yeast_pct"]
        session['pf1_flour1_type'] = request.form["pf1_flour1_type"]
        session['pf1_flour2_type'] = request.form["pf1_flour2_type"]
        session['pf1_flour3_type'] = request.form["pf1_flour3_type"]
        session['pf1_flour1_pct'] = request.form["pf1_flour1_pct"]
        session['pf1_flour2_pct'] = request.form["pf1_flour2_pct"]
        session['pf1_flour3_pct'] = request.form["pf1_flour3_pct"]
        return redirect('/bbga1table')
   
    return render_template('index.html', form=form)

@app.route('/bbga1table', methods=['GET', 'POST'])
def bbga1table():    
    def calculate_flour(flour_mass, section, flour1, flour1_pct, flour2, flour2_pct, flour3, flour3_pct):
        
        class flourKeys:
            def __init__(self, type, section):
                pct = '_pct'
                mass = '_mass'
                if 'APF' in type:
                    self.flour_pct_key = section + 'apf' + pct
                    self.flour_mass_key = section + 'apf' + mass
                    
                elif 'Bread' in type:
                    self.flour_pct_key = section + 'bread' + pct
                    self.flour_mass_key = section + 'bread' + mass

                elif 'Whole' in type:
                    self.flour_pct_key = section + 'ww' + pct
                    self.flour_mass_key = section + 'ww' + mass

                elif 'Rye' in type:
                    self.flour_pct_key = section + 'rye' + pct
                    self.flour_mass_key = section + 'rye' + mass

                elif 'Other' in type:
                    self.flour_pct_key = section + 'other' + pct
                    self.flour_mass_key = section + 'other' + mass

        flourvalues = {}

        flourvalues[section + 'apf_pct'] =  0
        flourvalues[section + 'apf_mass'] = 0
        flourvalues[section + 'ww_pct'] =  0
        flourvalues[section + 'ww_mass'] = 0
        flourvalues[section + 'bread_pct'] =  0
        flourvalues[section + 'bread_mass'] = 0
        flourvalues[section + 'rye_pct'] =   0
        flourvalues[section + 'rye_mass'] =  0
        flourvalues[section + 'other_pct'] =  0
        flourvalues[section + 'other_mass'] = 0


        total_keys = flourKeys(flour1, section)
        if flour1_pct != 0:
            flourvalues[total_keys.flour_pct_key] += flour1_pct
            flourvalues[total_keys.flour_mass_key] = themath.ingredient_mass(int(flourvalues[total_keys.flour_pct_key]), flour_mass)
        
        total_keys = flourKeys(flour2, section)
        if flour2_pct != 0:
            # Using += for assignment in case user selects the same flour type in more than one field
            flourvalues[total_keys.flour_pct_key] += flour2_pct
            flourvalues[total_keys.flour_mass_key] = themath.ingredient_mass(flourvalues[total_keys.flour_pct_key], flour_mass)
        
        total_keys = flourKeys(flour3, section)
        if flour3_pct != 0:
            # Using += for assignment in case user selects the same flour type in more than one field
            flourvalues[total_keys.flour_pct_key] += flour3_pct
            flourvalues[total_keys.flour_mass_key] = themath.ingredient_mass(int(flourvalues[total_keys.flour_pct_key]), flour_mass)

        return(flourvalues)

    #
    # Body
    #
    
    
    # These are session variables, or values entered by user
    bbga1dict = {}
    initialize_bbga1dict = ('apf_pct', 'bread_pct', 'ww_pct', 'rye_pct', 'other_pct', 'apf_mass', 'bread_mass', 'ww_mass', 'rye_mass', 'other_mass', 'pf1_yeast_mass', 'pf1_salt_mass', \
        'pf1_apf_pct', 'pf1_bread_pct', 'pf1_ww_pct', 'pf1_rye_pct', 'pf1_other_pct', 'pf1_apf_mass', 'pf1_bread_mass', 'pf1_ww_mass', 'pf1_rye_mass', 'pf1_other_mass', \
        'final_apf_pct', 'final_bread_pct', 'final_ww_pct', 'final_rye_pct', 'final_other_pct', 'final_apf_mass', 'final_bread_mass', 'final_ww_mass', 'final_rye_mass', 'final_other_mass', \
        'final_yeast_mass', 'final_salt_mass')

    initialDict = dict.fromkeys(initialize_bbga1dict, 0)
    bbga1dict.update(initialDict)

    bbga1dict['bbga_recipe_name'] = bbga_recipe_name = session['bbga_recipe_name']
    bbga1dict['units'] = session['units']
    bbga1dict['tdw'] = tdw = session['tdw']
    bbga1dict['water_pct'] = water_pct = int(session['water_pct'])
    bbga1dict['salt_pct'] = salt_pct = float(session['salt_pct'])
    bbga1dict['yeast_pct'] = yeast_pct = float(session['yeast_pct'])
    bbga1dict['addin_pct'] = addin_pct = float(session['addin_pct'])
    
    bbga1dict['total_formula_pct'] = total_formula_pct = 100 + water_pct + salt_pct + yeast_pct + addin_pct

    bbga1dict['flour_mass'] = flour_mass = int(tdw) / total_formula_pct * 100
    bbga1dict['water_mass'] = water_mass = themath.ingredient_mass(water_pct,flour_mass)
    bbga1dict['salt_mass'] = salt_mass = themath.ingredient_mass(salt_pct,flour_mass)
    bbga1dict['yeast_mass'] = yeast_mass = themath.ingredient_mass(yeast_pct,flour_mass)
    bbga1dict['addin_mass'] = addin_mass = themath.ingredient_mass(addin_pct,flour_mass)

    totals_section_prefix = ''
    flour1_type = (session['flour1_type'])
    flour2_type = (session['flour2_type'])
    flour3_type = (session['flour3_type'])
    flour1_pct = int(session['flour1_pct'])
    flour2_pct = int(session['flour2_pct'])
    flour3_pct = int(session['flour3_pct'])
    flourvalues = calculate_flour(flour_mass, totals_section_prefix, flour1_type, flour1_pct, flour2_type, flour2_pct, flour3_type, flour3_pct)

    bbga1dict.update(flourvalues) 


    # Calculate flour totals
    
    # Determine which template to use
    if "None" in session['pf1']:
        # Use values as calculated above
        bbga1dict['pf1'] = "None"
        bbga1dict['desc'] = "This is a straight dough--no preferment."
        return render_template('bbgastraight.html', **bbga1dict)
    else:
    #
    # PF1 calculations with PF
    #  
        bbga1dict['pf1'] = session['pf1']
        bbga1dict['desc'] = "This dough contains a preferment as indicated in the table."
        
        bbga1dict['pf1_pff_pct'] = pf1_pff_pct = float(session['pf1_pff_pct'])
        bbga1dict['total_seed_pct'] = total_seed_pct = float(session['pf1_seed_pct']) 
        bbga1dict['pf1_seed_pct'] = pf1_seed_pct = total_seed_pct / pf1_pff_pct * 100
        
        bbga1dict['pf1_water_pct'] = pf1_water_pct = float(session['pf1_water_pct'])

        # Yeast, first calculate pf1 yeast as a percentage of total
        bbga1dict['pf1_yeast_pct'] = pf1_yeast_pct = float(session['pf1_yeast_pct'])
        
        pf1_yeast_compare = pf1_yeast_pct * pf1_pff_pct / 100
        if pf1_yeast_compare > bbga1dict['yeast_pct']:
            bbga1dict['yeast_pct'] = yeast_pct = pf1_yeast_compare
            bbga1dict['footnote_yeast'] = "**"
            bbga1dict['footnote_yeast_text'] = "** Yeast total percentage recalculated to accommodate yeast in preferment."

        # Yeast, first calculate pf1 yeast as a percentage of total
        bbga1dict['pf1_salt_pct'] = pf1_salt_pct = float(session['pf1_salt_pct'])
        
        pf1_salt_compare = pf1_salt_pct * pf1_pff_pct / 100
        if pf1_salt_compare > bbga1dict['salt_pct']:
            bbga1dict['salt_pct'] = salt_pct = pf1_salt_compare
            bbga1dict['footnote_salt'] = "&&"
            bbga1dict['footnote_salt_text'] = "&& Salt total percentage recalculated to accommodate salt in preferment."
    
        bbga1dict['total_formula_pct'] = total_formula_pct = 100 + water_pct + salt_pct + yeast_pct + addin_pct + total_seed_pct
        bbga1dict['flour_mass'] = flour_mass = int(tdw) / total_formula_pct * 100
        
        # Recalculate everything after changing flour mass
        bbga1dict['water_mass'] = water_mass = themath.ingredient_mass(water_pct,flour_mass)
        bbga1dict['salt_mass'] = salt_mass = themath.ingredient_mass(salt_pct,flour_mass)
        bbga1dict['yeast_mass'] = yeast_mass = themath.ingredient_mass(yeast_pct,flour_mass)
        bbga1dict['addin_mass'] = addin_mass = themath.ingredient_mass(addin_pct,flour_mass)

        bbga1dict['pf1_flour_mass'] = pf1_flour_mass = themath.ingredient_mass(pf1_pff_pct, flour_mass)
        bbga1dict['pf1_water_mass'] = pf1_water_mass = themath.ingredient_mass(pf1_water_pct, pf1_flour_mass)
        if bbga1dict['water_mass'] < bbga1dict['pf1_water_mass']:
            flash("Preferment water mass too high to maintain dough hydration level.  Starting over.")
            return redirect('/index')
        else:
            bbga1dict['final_water_mass'] = round(bbga1dict['water_mass'] - bbga1dict['pf1_water_mass'],1)
        bbga1dict['pf1_salt_mass'] = pf1_salt_mass = themath.ingredient_mass(pf1_salt_pct,pf1_flour_mass)
        bbga1dict['pf1_yeast_mass'] = pf1_yeast_mass = themath.ingredient_mass(pf1_yeast_pct, pf1_flour_mass)

        
        
        bbga1dict['pf1_seed_mass'] = pf1_seed_mass = themath.ingredient_mass(pf1_seed_pct, pf1_flour_mass)
        bbga1dict['pf1_mass'] = pf1_flour_mass + pf1_water_mass + pf1_salt_mass + pf1_yeast_mass + pf1_seed_mass
        bbga1dict['pf1_formula_pct'] = 100 + pf1_water_pct + pf1_salt_pct + pf1_yeast_pct + pf1_seed_pct
        # Adding 0 to following two calcs so that total does not show as "-0.0"
        bbga1dict['final_salt_mass'] = round(bbga1dict['salt_mass'] - bbga1dict['pf1_salt_mass'] + 0,1)
        bbga1dict['final_yeast_mass'] = round(bbga1dict['yeast_mass'] - bbga1dict['pf1_yeast_mass'] + 0,1)

        totals_section_prefix = 'pf1_'
        flour1_type = (session['pf1_flour1_type'])
        flour2_type = (session['pf1_flour2_type'])
        flour3_type = (session['pf1_flour3_type'])
        flour1_pct = int(session['pf1_flour1_pct'])
        flour2_pct = int(session['pf1_flour2_pct'])
        flour3_pct = int(session['pf1_flour3_pct'])
        flourvalues_pf1 = calculate_flour(pf1_flour_mass, totals_section_prefix, flour1_type, flour1_pct, flour2_type, flour2_pct, flour3_type, flour3_pct)
        bbga1dict.update(flourvalues_pf1) 
                        

        def recalc_totals (fType):
            flourvalues_dict = {} 

            # List of cumulative differences -- you'll see later how they are used.
            
            calculated_pct = bbga1dict[fType + "_pct"] - ((bbga1dict["pf1_" + fType + "_pct"] * bbga1dict['pf1_pff_pct']) / 100)
            
            #adjust_flag = False
            
            if calculated_pct < 0:
                flourvalues_dict[fType + "_pct"] = bbga1dict[fType + "_pct"] + abs(calculated_pct)
                flourvalues_dict["footnote_" + fType] = "##"
                flourvalues_dict["footnote_flour_text"] = "## Total formula flour percentage recalculated to accommodate flour in preferment." 
                flourvalues_dict['cum_neg'] = abs(calculated_pct)
                #adjust_flag = True
            elif calculated_pct == 0:
                flourvalues_dict[fType + "_pct"] = bbga1dict[fType + "_pct"]
                flourvalues_dict["footnote_" + fType] = "xx"
                flourvalues_dict['cum_pos'] = 0
                #adjust_flag = True
            else:            
                flourvalues_dict["footnote_" + fType] = ""
                flourvalues_dict[fType + "_pct"] = flourvalues_dict['cum_pos'] = bbga1dict[fType + "_pct"]

            flourvalues_dict[fType + "_mass"] = themath.ingredient_mass(flourvalues_dict[fType + "_pct"], bbga1dict['flour_mass']) 
            flourvalues_dict["final_" + fType + "_mass"] = flourvalues_dict[fType + "_mass"] - bbga1dict["pf1_" + fType + "_mass"]
                
            #flourvalues_dict['adjust_flag'] = adjust_flag

            return(flourvalues_dict)

        def recalc_totals_again (fType):
            flourvalues_dict2 = {}
            if bbga1dict["footnote_" + fType] == "xx":
                flourvalues_dict2["footnote_" + fType] = ""
            elif bbga1dict[fType + "_pct"] != 0 and bbga1dict["footnote_" + fType] != "##":
                flourvalues_dict2["footnote_" + fType] = "##"
                flourvalues_dict2[fType + "_pct"] = bbga1dict[fType + "_pct"] - (bbga1dict[fType + "_pct"]/bbga1dict['cum_pos'] * bbga1dict['cum_neg'])
                flourvalues_dict2[fType + "_mass"] = themath.ingredient_mass(flourvalues_dict2[fType + "_pct"], bbga1dict['flour_mass']) 
                flourvalues_dict2["final_" + fType + "_mass"] =round(flourvalues_dict2[fType + "_mass"] - bbga1dict["pf1_" + fType + "_mass"],1)
            return(flourvalues_dict2)


        floursList = ("apf", "bread", "ww", "rye", "other")
        #adjust_flag = False
        
        cum_neg = 0
        cum_pos = 0

        for flours in floursList:
            flourvalues_dict = recalc_totals(flours)
            
            #if flourvalues_dict['adjust_flag']:
                
            if flourvalues_dict["footnote_" + flours] == "##":
                #adjust_flag = True   
                cum_neg += flourvalues_dict['cum_neg']
            else:
                cum_pos += flourvalues_dict['cum_pos']
                    

            bbga1dict.update(flourvalues_dict)

        bbga1dict['cum_neg'] = cum_neg    
        bbga1dict['cum_pos'] = cum_pos
            
        #if adjust_flag:
            #flash("Adjust flag true ")
        for flours in floursList:
            flourvalues_dict2 = recalc_totals_again(flours)
            bbga1dict.update(flourvalues_dict2)
        
        return render_template('bbga1table.html', **bbga1dict)  

@app.route('/breadcalc', methods=['GET', 'POST'])
def breadcalc():
    form = breadcalcinput()
    
    if request.method == "POST":  
        #if form.validate_on_submit():
        #    flash("Validate on submit test.")
        #else:
        #    flash("Not validated.")
        if request.form["units"]=="gm":
            session['units'] = "grams"
        else:
            session['units'] = "kilograms"
        session['recipe_flour_mass']  = request.form['recipe_flour_mass'] 
        session['recipe_water_mass']  = request.form['recipe_water_mass'] 
        session['recipe_levain_mass'] = request.form['recipe_levain_mass']
        session['recipe_salt_mass'] =   request.form['recipe_salt_mass'] 
        session['recipe_yeast_mass'] =  request.form['recipe_yeast_mass']
        session['recipe_addin_mass'] =  request.form['recipe_addin_mass'] 

        
        session['levain_hyd_recipe'] = request.form["levain_hyd_recipe"]
        session['levain_hyd_yours'] = request.form["levain_hyd_yours"]
        return redirect('/breadcalctable')
    
    return render_template('breadcalc.html', form=form)

@app.route('/breadcalctable', methods=['GET', 'POST'])
def breadcalctable():
    # These are session variables
    ingredients_calc = dict()
    ingredients_calc['units'] = session['units']
    ingredients_calc['recipe_flour_mass'] = recipe_flour_mass = session['recipe_flour_mass']
    ingredients_calc['recipe_water_mass'] = recipe_water_mass = session['recipe_water_mass']
    ingredients_calc['recipe_salt_mass'] =  recipe_salt_mass =  session['recipe_salt_mass']
    ingredients_calc['recipe_yeast_mass'] = recipe_yeast_mass = session['recipe_yeast_mass']
    ingredients_calc['recipe_addin_mass'] = recipe_addin_mass = session['recipe_addin_mass']
    ingredients_calc['recipe_levain_mass'] = recipe_levain_mass = session['recipe_levain_mass']
    ingredients_calc['levain_hyd_recipe'] = levain_hyd_recipe = session['levain_hyd_recipe'] 
    ingredients_calc['levain_hyd_yours'] = levain_hyd_yours = session['levain_hyd_yours'] 
    
    # These are calculations for original recipe
    
    ingredients_calc['pf_flour_mass'] = pf_flour_mass = float(themath.levain_flour_qty_fnc(float(recipe_levain_mass),float(levain_hyd_recipe)/100))
    ingredients_calc['tdw'] = float(recipe_flour_mass) + float(recipe_water_mass) + float(recipe_salt_mass) + float(recipe_yeast_mass) + float(recipe_addin_mass) + float(recipe_levain_mass)
    
    # pff is prefermented flour
    ingredients_calc['flour_mass'] = flour_mass = pf_flour_mass + float(recipe_flour_mass)
    ingredients_calc['pff_pct'] = pf_flour_mass / flour_mass * 100

    old_PF_water_mass = themath.levain_water_qty_fnc(float(recipe_levain_mass),float(levain_hyd_recipe) / 100)

    ingredients_calc['water_mass'] = water_mass = float(recipe_water_mass) + old_PF_water_mass
    ingredients_calc['water_pct'] = water_pct = water_mass /  flour_mass * 100

    ingredients_calc['salt_mass'] = salt_mass = float(recipe_salt_mass) 
    ingredients_calc['salt_pct'] = salt_pct = salt_mass /  flour_mass * 100

    ingredients_calc['yeast_mass'] = yeast_mass = float(recipe_yeast_mass)
    ingredients_calc['yeast_pct'] = yeast_pct = yeast_mass /  flour_mass * 100

    ingredients_calc['addin_mass'] = addin_mass = float(recipe_addin_mass)
    ingredients_calc['addin_pct'] = addin_pct = addin_mass /  flour_mass * 100

    #
    # These are calculations for adjusted recipe
    #
    ingredients_calc['pf_water_mass'] = pf_water_mass = themath.levain_water_adjusted(pf_flour_mass, int(levain_hyd_yours) / 100)
    ingredients_calc['pf_mass'] = pf_flour_mass + pf_water_mass
    ingredients_calc['final_flour_mass'] = flour_mass - pf_flour_mass
    ingredients_calc['final_water_mass'] = water_mass - pf_water_mass

    #
    # Total row
    #
    ingredients_calc['total_formula_pct'] = 100 + water_pct + salt_pct + yeast_pct + addin_pct
    ingredients_calc['pf_formula_pct'] = 100 + int(levain_hyd_yours)

    return render_template('breadcalctable.html', **ingredients_calc)  

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
    
    # Round this?
    ingredients['new_flour_qty'] = flour_qty - ingredients['levain_flour']
    ingredients['new_water_qty'] = water_qty - ingredients['levain_water']

    # Divide by itself, to set up for future varying flour types
    ingredients['flour_pct'] = int(flour_qty / flour_qty * 100)

    # Round this?
    ingredients['new_flour_pct'] = ingredients['new_flour_qty'] / flour_qty * 100 
    
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
