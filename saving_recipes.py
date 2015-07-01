__author__ = 'sophiaosintsev'
import cPickle as pickle


pickle_file = "/Users/sophiaosintsev/Documents/pdxcodeguild/recipe_manager/savedrecipes"

def write_to_file(recipe_manager):
    with open(pickle_file, 'w') as pfile:
        pickle.dump(recipe_manager, pfile)

def get_from_file():
    with open(pickle_file) as pfile:
        loaded_obj = pickle.load(pfile)
    return loaded_obj

