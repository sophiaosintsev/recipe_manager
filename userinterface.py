__author__ = 'sophiaosintsev'
from termcolor import colored
import saving_recipes

# recipe_manager = {"Cake": {"Ingredients": ["1 cup sugar",
#                                            "4 eggs",
#                                            "1 tsp. baking powder"],
#                            "Directions": "Cake directions"},
#                   "Cookies": {"Ingredients": ["1 cup butter",
#                                               "1 cup sugar",
#                                               "2 cups flour"],
#                               "Directions": "1. Preheat oven and grease pan. "
#                                             "2. Combine all ingredients. "
#                                             "3. Bake for 20 minutes. "}}

recipe_manager = saving_recipes.get_from_file()

# Function to search for recipes
def search():
    title = raw_input("\nWhat is the name of the recipe you want to search for? >> \n").title()
    if title not in recipe_manager:
        print(colored("\nThis recipe does not exist!\n", "red"))
        return
    print_recipe(title, recipe_manager[title])

# Function to add recipes
def add():
    title = raw_input("\nWhat is the name of the recipe you want to add? >> \n").title()
    if title in recipe_manager:
        print(colored("\nThis recipe already exists!\n", "red"))
    else:
        ingredients = raw_input("\nPlease list the ingredients for this recipe separated by comma(,) >> \n").split(", ")
        directions = raw_input("\nPlease list the directions for this recipe, ending each set of directions "
                               "with a period(.) >> \n").split(". ")
        recipe_manager[title] = {"Ingredients": ingredients, "Directions": directions}
        print "\nThe new recipe has been added!\n"
    saving_recipes.write_to_file(recipe_manager)

# Function to edit recipes
def edit():
    title = raw_input("\nWhat is the title of the recipe you want to edit? >> \n").title()
    if title not in recipe_manager:
        print(colored("\nThis recipe does not exist!\n", "red"))
        return
    else:
        ingredients = recipe_manager[title]["Ingredients"]
        directions = recipe_manager[title]["Directions"]
        print_recipe(title, recipe_manager[title])
    subchoice = raw_input("""
        \nWhat would you like to change?
        \t1. Recipe name
        \t2. Recipe ingredients
        \t3. Recipe directions
        Please enter a choice by number. >> \n""")

    if subchoice == '1':
        new = raw_input("\nWhat is the new name of the recipe? >> \n").title()
        recipe_manager[new] = {"Ingredients": ingredients, "Directions": directions}
        del recipe_manager[title]
        print "\nThe name of this recipe has been changed!\n"

    elif subchoice == '2':
        new = raw_input("\nWhat is the new list of ingredient? Please separate ingredients by comma >> \n").split(", ")
        recipe_manager[title.capitalize()] = {"Ingredients": new, "Directions": directions}
        print "\nThe ingredients in this recipe have been changed!\n"

    elif subchoice == '3':
        new = raw_input("\nWhat are the new directions for this recipe? "
                        "Please end each set of directions with a period(.) >> \n").split(". ")
        recipe_manager[title.capitalize()] = {"Ingredients": ingredients, "Directions": new}
        print "\nThe directions for this recipe have been changed!\n"

    else:
        print(colored("\nThat's not a choice! Please try again.\n", "red"))
    saving_recipes.write_to_file(recipe_manager)

# Function to delete recipes
def delete():
    title = raw_input("\nWhat is the name of the recipe you want to delete? >> \n").title()
    if title not in recipe_manager:
        print(colored("\nThis recipe does not exist!\n", "red"))
        return
    else:
        print_recipe(title, recipe_manager[title])
        response = raw_input("\nAre you sure you want to delete this recipe? (yes/no) >> \n")
        if response == "yes":
            del recipe_manager[title]
            print "\nRecipe {} has been deleted!\n".format(title)
        else:
            if response == "no":
                return
    saving_recipes.write_to_file(recipe_manager)

# use this function to print pretty in the format that I want
def print_recipe(title, recipe_dict):
    print "\n" + "\n" + "\n" + "\n" '\033[1m' + (colored(title, "blue"))
    print
    print '\033[1m' + (colored("Ingredients", "blue"))
    for ingredient in recipe_dict["Ingredients"]:
        print '\t' + "   " + ingredient
    print
    print '\033[1m' + (colored("Directions", "blue"))
    for direction in recipe_dict["Directions"]:
        print '\t' + "   " + direction


while True:
    choice = raw_input("""
        Please make a selection:
        \t1. Search for recipe by name
        \t2. Add a recipe
        \t3. Edit a recipe
        \t4. Delete a recipe
        \t5. Exit the system
        Please enter a choice by number. >> """)
    if choice == '1':
        search()
    elif choice == '2':
        add()
    elif choice == '3':
        edit()
    elif choice == '4':
        delete()
    elif choice == '5':
        saving_recipes.write_to_file(recipe_manager)
        break
    else:
        print(colored("\nThat is not a valid choice!\n", "red"))
