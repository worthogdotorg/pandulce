
def sourdough_qty_fnc(levain_pct, dough_weight):
    return(round(levain_pct * (dough_weight)))
   
def levain_flour_qty_fnc(levain_qty, levain_hyd):
    return(levain_qty / (1 + levain_hyd))

def levain_water_qty_fnc(levain_qty, levain_hyd):
    flour = levain_flour_qty_fnc(levain_qty, levain_hyd)
    return(levain_qty - flour)

def sourdough_pct_adjust_fnc(levain_water, levain_hyd, dough_weight):
    from sympy import Eq, solve, symbols, N
    x = symbols('x')
    water_calc = N(Eq((x + levain_water) - ((x + levain_water) / (1 + levain_hyd)), levain_water),1)
    flour = solve(water_calc, x)
    levain_weight = levain_water + int(flour[0])
    return(levain_weight / dough_weight)

def levain_water_adjusted(pff, hyd):
    return (pff * hyd)

def ingredient_mass(ing_pct, flour_mass):
    return (ing_pct * flour_mass / 100)
