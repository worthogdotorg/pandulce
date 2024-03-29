# Bakers Percentage Calculator
This was inspired by three things:

* The [Introduction to Baker’s Percentages](https://www.theperfectloaf.com/reference/introduction-to-bakers-percentages/) article and subsequent comments in the excellent The Perfect Loaf website.
* My own baking experience maintaining a 100% hydration starter but wanting to quickly convert recipes using varying hydration levels. For example, I often bake breads from [FLOUR WATER SALT YEAST](https://kensartisan.com/flour-water-salt-yeast), but the author uses an 80% hydration starter and I maintain my starter at 100%. Therefore, I have to convert the recipe in order to maintain dough hydration and prefermented flour quantities.
* During the pandemic, in addition to spending a lot of time in the kitchen and exercising to keep things in balance, I thought it a good time to learn Python full stack programming.

# Sourdough Starter Discard Recipe Calculator

Like many, I've been finding creative ways to use sourdough discard which is safe, edible and delicious. So when not baking boules, I find myself using discard in recipes that may not call for sourdough, like traditional whole wheat bread, date nut loaf and tortillas, ¡Ay caramba!

But when replacing flour and water with sourdough discard it's important to maintain bakers percentages. Otherwise you may end up baking a brick or something resembling a stiff, hot porridge. This simple calculator will compute the amount of flour and water required to maintain the original recipe bakers percentages when replacing some portion of the dough with sourdough discard.

My primary objective with the calculator--beyond accuracy and a clean interface--is simplicity. For more information on how to use the calculator, give it a test ride and click Help in the navigation bar.

# Usage

My primary objective with the calculators--beyond accuracy and a clean interface--is simplicity. 

For more information on how to use the calculator, give it a test ride at pandulce.worthog.org and click Help in the navigation bar.

# Roadmap

Check out the [GitHub repository Issues list](https://github.com/worthogdotorg/pandulce/issues) for enhancements. Can you think of anything that you'd like to see? If so, then add a new issue to the list or send me an email.

# The Stack

The desire to have a simple calculator and learn something about Python full stack programming steered me in the direction of this stack. I used Pipenv to manage the packages and virtual environments for this project, so here's an excerpt from the Pipfile:

    bootstrap-flask==1.5
    click==7.1.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'
    dominate==2.5.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
    flask-bootstrap==3.3.7.1
    flask-wtf==0.14.3
    flask==1.1.2
    itsdangerous==1.1.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
    jinja2==2.11.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'
    markupsafe==1.1.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'
    mpmath==1.1.0
    python-dotenv==0.14.0
    sympy==1.6.2
    visitor==0.1.3
    werkzeug==1.0.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'
    wtforms==2.3.3
    
I'm a newbie full stack Python programmer, so don't be surprised at anything you find that might be a little unconventional. And I won't be offended if you tell me how to make things more Pythonic or in accordance with best practices.

The app is currently running as an Azure Web App for containers. Building and implementing the container app was way easier than I expected.    

# Acknowledgments

There are bushels of good bread calculators for calculating recipes, timings, or just exhibited a level of obsession about bread that I could appreciate. Here are three which inspired me:

*   [The Sourdough School Calculator](https://www.sourdough.co.uk/sourdough-hydration-calculator/)
*   [Bread Calculator](http://brdclc.com/?flour=1000&water=75&salt=2&leaven=20)
*   [Bread Scheduler](https://www.breadscheduler.com/#/ target=_)

This article is very has a simple explanation for bakers who are just starting to figure out how to use discard in conventional recipes, ["You Can Add Sourdough Starter Discard to Almost Anything — It Just Requires a Little Math"](https://www.thekitchn.com/using-sourdough-starter-discard-23025996#comments-23025996)

Icons and glyphs make the user experience a little more pleasant, IMHO. The images I used are courtesy of [icons8](https://icons8.com/).

For this calculator, simplicity was paramount even if the algebra required was sometimes not so simple (at least for me)! Somewhat embarrassingly, I could not have figured out the math without the help of [this terrific site](https://munchietamer.com/bread-math-sourdough-starter-and-dough-hydration/) which provided the needed formulas and helpful explanations. Hey, it's been awhile since I've done high school algebra. 

![Too Old For This Shit](https://imgs.xkcd.com/comics/too_old_for_this_shit.png)

Thanks to [XKCD](https://xkcd.com) for the awesome comic above.

Gracias. Huzzahs!

# About Me

I'm a long time home baker and have been maintaining starters since long before the pandemic struck. I'm also a little geeky and have some time on my hands (and sometimes bits of freshly kneaded dough). 

Contact information:

*   [stuff@worthog.org](mailto:stuff@worthog.org)

Paraphrasing [the great Papazian](https://www.brewerspublications.com/blogs/author/charlie-papazian), "Relax, don't worry, and have another slice of buttered bread." Happy Baking!
