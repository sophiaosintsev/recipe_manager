__author__ = 'sophiaosintsev'

class Recipes(object):

    def __init__(self):
        self.title = ""
        self.ingredients = []
        self.directions = ""

    def set_title(self, title="abcd"):
        self.tite = title

    def set_ingredients(self, ingredients=None):
        self.ingredients = ingredients or []

    def set_directions(self, directions="abcd"):
        self.directions = directions

    def create_recipe(self, title, ingredients, directions):
        self.set_title(title)
        self.set_ingredients(ingredients)
        self.set_directions(directions)

    # def display_recipe(self):
    #     return {'title': self.title, 'ingredients': self.ingredients, 'directions': self.directions}

