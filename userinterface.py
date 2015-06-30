__author__ = 'sophiaosintsev'

from pprint import pprint

recipe_manager = {"Cake": {"Ingredients": "Cake ingredients", "Directions": "Cake directions"},
                  "Cookies": {"Ingredients": "These are my ingredient", "Directions": "These are my directions"}}

# Function to search for recipes
def search():
    title = raw_input("\nWhat is the name of the recipe you want to search for? >> \n").capitalize()
    if title not in recipe_manager:
        print "\nThis recipe does not exist!\n"
        return
    pprint(recipe_manager[title])
    #TODO make display pretty
    # for x in recipe_manager:
    #     pprint(x)
    #     for y in recipe_manager[x]:
    #         print (y + "\n" + recipe_manager[x][y])

# Function to add recipes
def add():
    title = raw_input("\nWhat is the name of the recipe you want to add? >> \n").capitalize()
    if title in recipe_manager:
        print "\nThis recipe already exists!\n"
    else:
        # TODO make sure ingredients is a list not a string
        ingredients = raw_input("\nPlease list the ingredients for this recipe >> \n")
        directions = raw_input("\nPlease list the directions for this recipe >> \n")
        recipe_manager[title] = {"Ingredients": ingredients, "Directions": directions}
    print "\nThe new recipe has been added!\n"

# Function to edit recipes
def edit():
    title = raw_input("\nWhat is the title of the recipe you want to edit? >> \n").capitalize()
    if title not in recipe_manager:
        print "\nThis recipe does not exist!\n"
        return
    else:
        ingredients = recipe_manager[title]["Ingredients"]
        directions = recipe_manager[title]["Directions"]
        pprint(recipe_manager[title])
    subchoice = raw_input("""
        \nWhat would you like to change?
        \t1. Recipe name
        \t2. Recipe ingredients
        \t3. Recipe directions
        Please enter a choice by number. >> \n""")

    if subchoice == '1':
        new = raw_input("\nWhat is the new name of the recipe? >> \n").capitalize()
        recipe_manager[new] = {"Ingredients": ingredients, "Directions": directions}
        del recipe_manager[title]
        print "\nThe name of this recipe has been changed!\n"

    elif subchoice == '2':
        new = raw_input("\nWhat is the new list of ingredient? >> \n")
        recipe_manager[title.capitalize()] = {"Ingredients": new, "Directions": directions}
        print "\nThe ingredients in this recipe have been changed!\n"

    elif subchoice == '3':
        new = raw_input("What are the new directions for this recipe? >> ")
        recipe_manager[title.capitalize()] = {"Ingredients": ingredients, "Directions": new}
        print "\nThe directions for this recipe have been changed!\n"

    else:
        print "\nThat's not a choice! Please try again.\n"

# Function to delete recipes
def delete():
    title = raw_input("\nWhat is the name of the recipe you want to delete? >> \n").capitalize()
    if title not in recipe_manager:
        print "\nThis recipe does not exist!\n"
        return
    else:
        pprint(recipe_manager[title])
        response = raw_input("\nAre you sure you want to delete this recipe? (yes/no) >> \n")
        if response == "yes":
            del recipe_manager[title]
            print "\nRecipe {} has been deleted!\n".format(title)
        else:
            if response == "no":
                return

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
        done = True
    else:
        print "\nThat is not a valid choice!\n"