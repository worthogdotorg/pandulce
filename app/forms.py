
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, IntegerField, RadioField, TextField
from wtforms.validators import NumberRange, ValidationError, DataRequired, EqualTo, Length, InputRequired

class recipeinput(FlaskForm):
    """Input recipe"""
    recipe_name = StringField('', default='Your recipe name', validators=[DataRequired(), Length(max=20)])
    levain_units = RadioField('Weight units')

    flour_qty = IntegerField('Flour weight', default=1000, validators=[DataRequired(), NumberRange(0,1000)])
    water_qty = IntegerField('Water weight', default=500, validators=[DataRequired(), NumberRange(0,1000)])
    dairy_qty = IntegerField('Dairy weight', default=0, validators=[DataRequired(), NumberRange(0,1000)])
    recipe_notes = TextAreaField('Recipe notes', validators=[Length(min=0, max=1000)])
    """recaptcha = RecaptchaField()"""
    levain_hyd = IntegerField('Sourdough hydration (%)', default=100, validators=[NumberRange(25,200)])
    levain_pct = IntegerField('Sourdough percentage (%)', default=0, validators=[NumberRange(0,100), InputRequired(message="Enter a whole number between 0-100")])
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



