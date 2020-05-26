cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}


def print_recipe(r):
    if recipe in cookbook:
        print("Recipe for {}:".format(r))
        print("Ingredients list:", cookbook[r]["ingredients"])
        print("To be eaten for {}." .format(cookbook[r]["meal"]))
        print("Takes {} minutes of cooking." .format(cookbook[r]["prep_time"]))
    else:
        print("This recipe is not available.")


def delete_recipe(recipe):
    if recipe in cookbook:
        cookbook.pop(recipe)
    else:
        print("This recipe is not present in the cookbook.")


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }


def print_cookbook():
    print("The different recipes available :")
    if len(cookbook) == 0:
        print("None")
    for recipe in cookbook:
        print(recipe)


choice = ""
while (choice != "5"):
    print("")
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    print("")
    choice = input()
    if choice == "1":
        enter = ""
        ingredients = []
        print("What is the name of the recipe ?")
        name = input()
        if name in cookbook:
            print("This recipe already exists, impossible to add it.")
        else:
            print("What are the ingredients ? (Enter: 'end' to finish)")
            while (enter != "end"):
                enter = input()
                if (enter != "end"):
                    ingredients.append(enter)
            print("What type of meal is it ?")
            meal = input()
            print("how long to prepare it ?")
            time = input()
            add_recipe(name, ingredients, meal, time)
    elif choice == "2":
        print("Which recipe do you want to delete ?")
        recipe = input()
        delete_recipe(recipe)
    elif choice == "3":
        print("Which recipe do you want to display ?")
        recipe = input()
        print_recipe(recipe)
    elif choice == "4":
        print_cookbook()
    elif choice == "5":
        print("Cookbook closed.")
    else:
        print("This option does not exist, \
please type the corresponding number.")
        print("To exit, enter 5.")
