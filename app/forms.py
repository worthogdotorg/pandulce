
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, IntegerField, RadioField, TextField, FloatField
from wtforms.validators import NumberRange, ValidationError, DataRequired, EqualTo, Length, InputRequired

class recipeinput(FlaskForm):
    """Input recipe"""
    recipe_name = StringField('', default='Your recipe name', validators=[DataRequired(), Length(max=20)])
    levain_units = RadioField('Weight units', validators=None)

    flour_qty = IntegerField('Flour weight', default=1000, validators=[DataRequired()])
    water_qty = IntegerField('Water weight', default=500, validators=None)
    dairy_qty = IntegerField('Dairy weight', default=0, validators=None)
    recipe_notes = TextAreaField('Recipe notes', validators=None)
    """recaptcha = RecaptchaField()"""
    levain_hyd = IntegerField('Sourdough hydration (%)', default=100, validators=None)
    levain_pct = IntegerField('Sourdough percentage (%)', default=0, validators=None)
    submit = SubmitField()
    
    # Not sure why I have to declare these here because they're not used in form.  But things break if I don't use them.
    new_flour_qty = IntegerField ('Adjusted flour weight', render_kw={'readonly': True})
    new_water_qty = IntegerField ('Adjusted water weight', render_kw={'readonly': True})
    new_dairy_qty = IntegerField ('Adjusted dairy weight', render_kw={'readonly': True})
    levain_qty = IntegerField ('Levain weight', render_kw={'readonly': True})

class recipeoutput(FlaskForm):
    """Output recipe"""
    recipe_notes = TextField('Recipe notes', validators=[Length(min=0, max=500)])
    levain_pct = IntegerField('Levain percentage (%)', validators=[NumberRange(0,100), DataRequired(message='Enter a number here to bake again!')])
    submit = SubmitField()
    """recaptcha = RecaptchaField()"""

class recipesamples(FlaskForm):
    """Output recipe"""
    levain_pct = IntegerField('Levain percentage', validators=[NumberRange(0,100), DataRequired(message='Enter a number here to bake again!')])
    submit = SubmitField()

class bbga1input(FlaskForm):
    """Input recipe"""
    bbga_recipe_name = StringField('', default='Your recipe name', validators=[InputRequired(), Length(max=20)])
    units = RadioField('Weight units', validators=None)
    tdw = IntegerField(validators=[InputRequired(), NumberRange(1,2000)])
    # Flours
    flour1_type = TextAreaField(validators=[InputRequired()])
    flour2_type = TextAreaField(validators=[InputRequired()])
    flour3_type = TextAreaField(validators=[InputRequired()])
    flour1_pct = IntegerField('Flour pct', validators=[InputRequired()])
    flour2_pct = IntegerField('Flour pct', validators=[InputRequired()])
    flour3_pct = IntegerField('Flour pct', validators=[InputRequired()])
    
    # Other ingredients
    water_pct = IntegerField('Water pct', validators=[InputRequired(), NumberRange(1,200)])
    salt_pct = FloatField('Salt pct', validators=[InputRequired(), NumberRange(0,20)])
    yeast_pct = FloatField('Yeast pct', validators=[InputRequired(), NumberRange(0,10)])
    addin_pct = FloatField('Addin pct', validators=[InputRequired(), NumberRange(0,50)])
    # Preferment #1
    #pf1_salt_pct = FloatField('Salt pct', validators=[InputRequired(), NumberRange(0,20)])
    pf1_yeast_pct = FloatField('Yeast pct', validators=[InputRequired(), NumberRange(0,10)])
    pf1_seed_pct = IntegerField('Seed pct', validators=[InputRequired(), NumberRange(0,50)])
    pf1 = TextAreaField(validators=[InputRequired()])
    pf1_pff_pct = IntegerField('PFF pct', validators=[InputRequired(), NumberRange(0,100)])
    pf1_flour1_type = TextAreaField(validators=[InputRequired()])
    pf1_flour2_type = TextAreaField(validators=[InputRequired()])
    pf1_flour3_type = TextAreaField(validators=[InputRequired()])
    pf1_flour1_pct = IntegerField('Flour pct', validators=[InputRequired()])
    pf1_flour2_pct = IntegerField('Flour pct', validators=[InputRequired()])
    pf1_flour3_pct = IntegerField('Flour pct', validators=[InputRequired()])
    pf1_water_pct = IntegerField('Starter water pct', validators=[InputRequired(), NumberRange(0,100)])
    
    submit = SubmitField()

class breadcalcinput(FlaskForm):
    """Input nums"""
    units = RadioField('Weight units')

    recipe_flour_mass = FloatField('Flour weight', default=1000, validators=[DataRequired(), NumberRange(0,1000)])
    recipe_water_mass = FloatField('Water weight', default=500, validators=[DataRequired(), NumberRange(0,1000)])
    recipe_levain_mass = FloatField('Dairy weight', default=0, validators=[DataRequired(), NumberRange(0,1000)])
    recipe_salt_mass = FloatField('Salt pct', default=0, validators=[InputRequired(), NumberRange(0,20)])
    recipe_yeast_mass = FloatField('Yeast pct', default=0, validators=[InputRequired(), NumberRange(0,20)])
    recipe_addin_mass = FloatField('Addin pct', default=0, validators=[InputRequired(), NumberRange(0,1000)])

    levain_hyd_recipe = IntegerField('Levain hydration (%)', default=100, validators=[NumberRange(50,150)])
    levain_hyd_yours = IntegerField('Levain hydration (%)', default=100, validators=[NumberRange(50,150)])
    
    submit = SubmitField()
    

