# Sourdough Starter Discard Recipe Calculator

Like many, I've been finding creative ways to use sourdough discard which is safe, edible and delicious. So when not baking boules, I find myself using discard in recipes that may not call for sourdough, like traditional whole wheat bread, date nut loaf and tortillas, ¡Ay caramba!

But when replacing flour and water with sourdough discard it's important to maintain [bakers percentages](https://www.theperfectloaf.com/reference/introduction-to-bakers-percentages/). Otherwise you may end up baking a brick or something resembling hot porridge. This simple calculator will compute the amount of flour and water required to maintain the original recipe bakers percentages when replacing some portion of the dough with sourdough discard.

## Usage

My primary objective with the calculator--beyond accuracy and a clean interface--is simplicity. Two screens, that's it!

For more information on how to use the calculator, give it a test ride at http://pandulce.info and click Help in the navigation bar.

## Roadmap

Check out the [GitHub repository Issues list](https://github.com/worthogdotorg/bread/issues) for application enhancements that I've thought of. Can you think of anything? If so, then add a new issue to the list. In addition to those, here are a couple of others:

*   Package the application in a container to better understand that process.
*   Create a second calculator showing how to adjust a recipe calling for a levain when using different hydrations. Hence the placeholder link in the navigation bar, which is just sort of a teaser for now.

## The Stack

The desire to have a simple calculator and learn something about Python full stack programming steered me in the direction of this stack. I used Pipenv to manage the packages and virtual environments for this project, so here's an excerpt from the Pipfile:

    [packages]
    flask = "*"
    python-dotenv = "*"
    flask-wtf = "*"
    bootstrap-flask = "*"
    flask-bootstrap = "*"
    sympy = "*"
    
I'm a newbie full stack Python programmer, so don't be surprised at anything you find that might be a little unconventional. And I won't be offended if you tell me how to make things more Pythonic or in accordance with best practices.

The app is currently running on an AWS EC2 instance.  When I figure out how to run in a container I will likely move to a more permanent home.  

## Acknowledgments

There are bushels of good bread calculators for calculating recipes, timings, or just exhibited a level of obsession about bread that I could appreciate. Here are three which inspired me:

*   [The Sourdough School Calculator](https://www.sourdough.co.uk/sourdough-hydration-calculator/)
*   [Bread Calculator](http://brdclc.com/?flour=1000&water=75&salt=2&leaven=20)
*   [Bread Scheduler](https://www.breadscheduler.com/#/ target=_)

This article is very has a simple explanation for bakers who are just starting to figure out how to use discard in conventional recipes, ["You Can Add Sourdough Starter Discard to Almost Anything — It Just Requires a Little Math"](https://www.thekitchn.com/using-sourdough-starter-discard-23025996#comments-23025996)

Icons and glyphs make the user experience a little more pleasant, IMHO. The images I used are courtesy of [icons8](https://icons8.com/).

I could not have deployed this on an AWS EC2 instance without [this very well written blog post on Twilio](https://www.twilio.com/blog/deploy-flask-python-app-aws). 

For this calculator, simplicity was paramount even if the algebra required was sometimes not so simple (at least for me)! Somewhat embarrassingly, I could not have figured out the math without the help of [this terrific site](https://munchietamer.com/bread-math-sourdough-starter-and-dough-hydration/) which provided the needed formulas and helpful explanations. Hey, it's been awhile since I've done high school algebra. Thank you. Gracias. Huzzahs!

## About Me

I'm a long time home baker and have been maintaining starters since long before the pandemic struck. I'm also a little geeky and have some time on my hands (and sometimes bits of freshly kneaded dough). I'm sort of semi-retired, but hoping to somehow leverage my nascent programming skills and many years of enterprise data center experience into something interesting with an organization doing good things for all of us.

Contact information:

*   [info@pandulce.info](mailto:info@pandulce.info)
*   [LinkedIn](www.linkedin.com/in/frank-a-espinoza)

Paraphrasing [the great Papazian](https://www.brewerspublications.com/blogs/author/charlie-papazian), "Relax, don't worry, and have another slice of buttered bread." Happy Baking!
