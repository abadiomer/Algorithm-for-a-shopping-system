import tkinter as tk
from tkinter import messagebox
import pandas as pd

# יצירת מאגר נתונים של מתכונים, המצרכים והאלרגיות
data = {
    'Dish': [
        'Greek Salad', 'Pizza', 'Pasta', 'Omelette', 'Chicken Soup', 'Beef Stew', 'Fish Tacos', 'Vegetable Stir Fry',
        'Apple Pie', 'Chocolate Cake', 'Caesar Salad', 'Grilled Cheese Sandwich', 'Bacon and Eggs', 'Fried Rice',
        'Tomato Soup', 'Lentil Soup', 'Quiche', 'Spaghetti Bolognese', 'Lasagna', 'Moussaka', 'Shakshuka',
        'Falafel', 'Hummus', 'Pita Bread', 'Tabbouleh', 'Gazpacho', 'Ratatouille', 'Paella', 'Tuna Salad',
        'Stuffed Peppers', 'Chicken Parmesan', 'Lamb Chops', 'Beef Burger', 'Fish and Chips', 'Chicken Curry',
        'Beef Tacos', 'Veggie Burger', 'Clam Chowder', 'Minestrone Soup', 'Pumpkin Pie', 'Cheesecake',
        'Banana Bread', 'Blueberry Muffins', 'French Toast', 'Pancakes', 'Waffles', 'Scrambled Eggs',
        'Eggs Benedict', 'Bagel with Cream Cheese', 'BLT Sandwich', 'Ham Sandwich', 'Turkey Sandwich',
        'Chicken Sandwich', 'Avocado Toast', 'Guacamole', 'Nachos', 'Quesadilla', 'Burrito', 'Enchiladas',
        'Chili', 'Steak', 'Pork Chops', 'Roast Beef', 'Meatloaf', 'Sausages', 'Ribs', 'Pulled Pork Sandwich',
        'Fried Chicken', 'Mashed Potatoes', 'Roasted Vegetables', 'Cauliflower Rice', 'Zucchini Noodles',
        'Baked Ziti', 'Mac and Cheese', 'Fettuccine Alfredo', 'Gnocchi', 'Chicken Alfredo', 'Eggplant Parmesan',
        'Stuffed Shells', 'Manicotti', 'Tortellini', 'Ravioli', 'Carbonara', 'Pesto Pasta', 'Shrimp Scampi',
        'Lobster Bisque', 'Crab Cakes', 'Baked Salmon', 'Grilled Shrimp', 'Tuna Steak', 'Ceviche',
        'Stuffed Mushrooms', 'Bruschetta', 'Caprese Salad', 'Antipasto', 'Garlic Bread', 'French Onion Soup',
        'Chicken Wings', 'Buffalo Wings'
    ],
    'Ingredients': [
        '3 tomatoes, 3 cucumbers, large handful of rocket leaves, 5 large lettuce leaves, half pack of Bulgarian cheese, vinegar, lemon juice, olive oil, half teaspoon of salt, black pepper, black and green olives',
        'cheese, dough, tomatoes, olive oil, salt, oregano',
        'pasta, tomatoes, olive oil, garlic, basil, salt, pepper',
        'eggs, salt, pepper, butter',
        'chicken, carrots, celery, onion, garlic, salt, pepper, chicken broth',
        'beef, potatoes, carrots, onions, garlic, beef broth, salt, pepper',
        'fish, tortillas, cabbage, lime, cilantro, avocado, sour cream',
        'broccoli, bell peppers, carrots, soy sauce, ginger, garlic',
        'apples, sugar, flour, butter, cinnamon, nutmeg, pie crust',
        'flour, sugar, cocoa powder, eggs, butter, baking powder, milk',
        'romaine lettuce, Caesar dressing, croutons, Parmesan cheese, lemon juice',
        'bread, cheese, butter',
        'bacon, eggs, salt, pepper',
        'rice, soy sauce, eggs, peas, carrots, green onions',
        'tomatoes, onion, garlic, chicken broth, cream, basil, salt, pepper',
        'lentils, carrots, celery, onions, garlic, cumin, salt, pepper',
        'eggs, cream, cheese, ham, pie crust, salt, pepper',
        'spaghetti, ground beef, tomato sauce, onion, garlic, oregano, basil, salt, pepper',
        'lasagna noodles, ricotta cheese, mozzarella cheese, Parmesan cheese, ground beef, tomato sauce, garlic, onion, basil, oregano, salt, pepper',
        'eggplant, ground beef, tomatoes, onions, garlic, cinnamon, allspice, salt, pepper, béchamel sauce',
        'tomatoes, bell peppers, onions, garlic, eggs, cumin, paprika, salt, pepper',
        'chickpeas, garlic, parsley, cumin, coriander, salt, pepper, flour, baking powder, oil',
        'chickpeas, tahini, lemon juice, garlic, olive oil, salt, water',
        'flour, yeast, water, salt, olive oil',
        'bulgur wheat, parsley, mint, tomatoes, cucumber, lemon juice, olive oil, salt, pepper',
        'tomatoes, cucumber, bell peppers, onion, garlic, olive oil, vinegar, salt, pepper',
        'eggplant, zucchini, bell peppers, tomatoes, onions, garlic, thyme, rosemary, salt, pepper, olive oil',
        'rice, saffron, chicken, shrimp, chorizo, bell peppers, peas, onions, garlic, tomatoes, chicken broth, salt, pepper',
        'tuna, mayonnaise, celery, onions, lemon juice, salt, pepper',
        'bell peppers, ground beef, rice, onions, garlic, tomatoes, cumin, paprika, salt, pepper',
        'chicken breasts, Parmesan cheese, bread crumbs, marinara sauce, mozzarella cheese, olive oil, salt, pepper',
        'lamb chops, rosemary, garlic, olive oil, salt, pepper',
        'ground beef, burger buns, lettuce, tomato, cheese, pickles, ketchup, mustard, mayonnaise',
        'fish fillets, potatoes, flour, eggs, bread crumbs, oil, salt, pepper',
        'chicken, curry powder, coconut milk, onions, garlic, ginger, tomatoes, cilantro, salt, pepper',
        'ground beef, taco shells, lettuce, tomatoes, cheese, sour cream, salsa, onions',
        'black beans, quinoa, burger buns, lettuce, tomato, avocado, onions',
        'clams, potatoes, onions, celery, bacon, cream, butter, salt, pepper',
        'vegetable broth, tomatoes, carrots, celery, onions, zucchini, beans, pasta, garlic, basil, oregano, salt, pepper',
        'pumpkin puree, sugar, eggs, evaporated milk, cinnamon, nutmeg, pie crust',
        'cream cheese, sugar, eggs, graham cracker crust, vanilla extract',
        'bananas, flour, sugar, eggs, butter, baking soda, salt',
        'blueberries, flour, sugar, eggs, butter, baking powder, milk',
        'bread, eggs, milk, cinnamon, sugar, butter, vanilla extract',
        'flour, eggs, milk, sugar, baking powder, butter, vanilla extract',
        'flour, eggs, milk, sugar, baking powder, butter, vanilla extract',
        'eggs, milk, butter, salt, pepper',
        'eggs, ham, English muffins, hollandaise sauce, butter',
        'bagels, cream cheese',
        'bread, bacon, lettuce, tomato, mayonnaise',
        'bread, ham, cheese, mustard, mayonnaise',
        'bread, turkey, lettuce, tomato, mayonnaise',
        'bread, chicken, lettuce, tomato, mayonnaise',
        'bread, avocado, salt, pepper, lemon juice',
        'avocado, tomatoes, onion, cilantro, lime juice, salt',
        'tortilla chips, cheese, jalapenos, salsa, sour cream',
        'tortillas, cheese, chicken, bell peppers, onions',
        'tortillas, beans, rice, cheese, lettuce, tomatoes, sour cream, guacamole',
        'tortillas, chicken, cheese, enchilada sauce, onions, olives',
        'ground beef, beans, tomatoes, chili powder, cumin, onions, garlic, salt, pepper',
        'steak, salt, pepper, garlic, rosemary, butter',
        'pork chops, salt, pepper, garlic, rosemary, olive oil',
        'roast beef, salt, pepper, garlic, rosemary, olive oil',
        'ground beef, breadcrumbs, eggs, onions, garlic, ketchup, Worcestershire sauce, salt, pepper',
        'sausages, onions, peppers, oil',
        'ribs, barbecue sauce, salt, pepper, garlic powder, onion powder',
        'pork shoulder, barbecue sauce, buns, coleslaw',
        'chicken, flour, eggs, breadcrumbs, oil, salt, pepper',
        'potatoes, butter, milk, salt, pepper',
        'carrots, potatoes, bell peppers, zucchini, olive oil, salt, pepper',
        'cauliflower, olive oil, salt, pepper',
        'zucchini, olive oil, garlic, salt, pepper',
        'ziti pasta, ricotta cheese, mozzarella cheese, Parmesan cheese, tomato sauce, ground beef, garlic, onions, basil, oregano, salt, pepper',
        'macaroni, cheese, milk, butter, flour, salt, pepper',
        'fettuccine pasta, heavy cream, Parmesan cheese, butter, garlic, salt, pepper',
        'potatoes, cheese, flour, egg, butter, salt, pepper',
        'chicken breasts, heavy cream, Parmesan cheese, butter, garlic, fettuccine pasta, salt, pepper',
        'eggplant, Parmesan cheese, marinara sauce, mozzarella cheese, breadcrumbs, garlic, basil, salt, pepper',
        'pasta shells, ricotta cheese, mozzarella cheese, Parmesan cheese, marinara sauce, garlic, basil, salt, pepper',
        'pasta tubes, ricotta cheese, mozzarella cheese, Parmesan cheese, marinara sauce, garlic, basil, salt, pepper',
        'tortellini, cheese, marinara sauce, basil, salt, pepper',
        'ravioli, cheese, marinara sauce, basil, salt, pepper',
        'spaghetti, eggs, Parmesan cheese, bacon, black pepper',
        'pasta, basil pesto, Parmesan cheese, pine nuts, garlic, olive oil, salt',
        'shrimp, garlic, butter, lemon juice, white wine, parsley, fettuccine pasta, salt, pepper',
        'lobster, butter, cream, onions, garlic, salt, pepper',
        'crab meat, bread crumbs, mayonnaise, mustard, egg, Worcestershire sauce, lemon juice, salt, pepper',
        'salmon fillets, olive oil, lemon juice, garlic, salt, pepper',
        'shrimp, olive oil, garlic, lemon juice, salt, pepper',
        'tuna steak, olive oil, lemon juice, garlic, salt, pepper',
        'fish, lime juice, onions, cilantro, tomatoes, jalapenos, salt, pepper',
        'mushrooms, cheese, garlic, olive oil, breadcrumbs, parsley, salt, pepper',
        'bread, tomatoes, garlic, basil, olive oil, salt, pepper',
        'tomatoes, mozzarella cheese, basil, olive oil, balsamic vinegar, salt, pepper',
        'cured meats, cheese, olives, roasted peppers, artichoke hearts, bread',
        'bread, garlic, butter, parsley, salt',
        'onions, beef broth, bread, Gruyere cheese, thyme, salt, pepper',
        'chicken wings, salt, pepper, garlic powder, onion powder, paprika, barbecue sauce',
        'chicken wings, hot sauce, butter, garlic powder, onion powder, salt, pepper'
    ],
    'Allergens': [
        'none, none, none, none, dairy, none, none, none, none, none, none',
        'dairy, gluten, tomatoes, none, none, none',
        'gluten, tomatoes, none, garlic, none, none, none',
        'eggs, none, none, dairy',
        'none, none, none, none, none, none, none',
        'none, none, none, none, none, none, none',
        'fish, none, none, none, none, none',
        'none, none, none, soy, none, garlic',
        'none, none, gluten, dairy, none, none',
        'gluten, none, cocoa, eggs, dairy, none',
        'none, dairy, gluten, dairy, none',
        'gluten, dairy, none',
        'none, eggs, none, pepper',
        'gluten, soy, eggs, none, none, none',
        'tomatoes, none, garlic, none, dairy, basil, none, pepper',
        'none, none, none, garlic, cumin, none, pepper',
        'eggs, dairy, none, pork, gluten, none, pepper',
        'gluten, beef, tomatoes, none, garlic, oregano, basil, none, pepper',
        'gluten, dairy, beef, tomatoes, none, garlic, none, basil, oregano, none, pepper',
        'eggplant, beef, tomatoes, onions, garlic, none, none, cinnamon, allspice, none',
        'tomatoes, peppers, onions, garlic, eggs, cumin, paprika, none, pepper',
        'chickpeas, garlic, parsley, cumin, coriander, none, flour, baking powder, oil',
        'chickpeas, sesame, lemon, garlic, none, olive oil, salt, water',
        'gluten, none, water, none, olive oil',
        'bulgur, parsley, mint, tomatoes, cucumber, lemon, none, olive oil, salt, pepper',
        'tomatoes, cucumber, peppers, onion, garlic, olive oil, vinegar, salt, pepper',
        'eggplant, zucchini, peppers, tomatoes, onions, garlic, thyme, rosemary, none, olive oil',
        'rice, saffron, chicken, shrimp, chorizo, peppers, peas, onions, garlic, tomatoes, chicken broth, salt, pepper',
        'fish, eggs, mayonnaise, celery, onions, lemon, none, salt, pepper',
        'peppers, beef, rice, onions, garlic, tomatoes, cumin, paprika, none, pepper',
        'chicken, dairy, gluten, none, tomatoes, olive oil, salt, pepper',
        'lamb, rosemary, garlic, olive oil, none, pepper',
        'beef, gluten, lettuce, tomatoes, dairy, pickles, ketchup, mustard, mayonnaise',
        'fish, potatoes, gluten, eggs, bread crumbs, oil, none, pepper',
        'chicken, curry, coconut milk, onions, garlic, ginger, tomatoes, cilantro, none, pepper',
        'beef, gluten, lettuce, tomatoes, dairy, sour cream, salsa, onions',
        'beans, gluten, buns, lettuce, tomatoes, avocado, onions',
        'clams, potatoes, onions, celery, bacon, cream, butter, none, pepper',
        'vegetable broth, tomatoes, carrots, celery, onions, zucchini, beans, pasta, garlic, basil, oregano, salt, pepper',
        'pumpkin, gluten, eggs, evaporated milk, cinnamon, nutmeg, pie crust',
        'dairy, sugar, eggs, gluten, vanilla',
        'bananas, gluten, sugar, eggs, butter, baking soda, salt',
        'blueberries, gluten, sugar, eggs, butter, baking powder, milk',
        'gluten, eggs, milk, cinnamon, sugar, butter, vanilla',
        'gluten, eggs, milk, sugar, baking powder, butter, vanilla',
        'gluten, eggs, milk, sugar, baking powder, butter, vanilla',
        'eggs, milk, butter, salt, pepper',
        'eggs, pork, gluten, hollandaise, butter',
        'gluten, dairy',
        'gluten, bacon, lettuce, tomatoes, mayonnaise',
        'gluten, dairy, mustard, mayonnaise',
        'gluten, dairy, lettuce, tomatoes, mayonnaise',
        'gluten, chicken, lettuce, tomatoes, mayonnaise',
        'gluten, avocado, salt, pepper, lemon',
        'avocado, tomatoes, onions, cilantro, lime, salt',
        'tortilla, cheese, jalapenos, salsa, sour cream',
        'tortilla, cheese, chicken, peppers, onions',
        'tortilla, beans, rice, cheese, lettuce, tomatoes, sour cream, guacamole',
        'tortilla, chicken, cheese, enchilada, onions, olives',
        'beef, beans, tomatoes, chili powder, cumin, onions, garlic, salt, pepper',
        'beef, salt, pepper, garlic, rosemary, butter',
        'pork, salt, pepper, garlic, rosemary, olive oil',
        'beef, salt, pepper, garlic, rosemary, olive oil',
        'beef, breadcrumbs, eggs, onions, garlic, ketchup, Worcestershire, salt, pepper',
        'pork, onions, peppers, oil',
        'pork, barbecue sauce, salt, pepper, garlic, onion powder',
        'pork, barbecue sauce, buns, coleslaw',
        'chicken, gluten, eggs, breadcrumbs, oil, none, pepper',
        'potatoes, butter, milk, salt, pepper',
        'carrots, potatoes, peppers, zucchini, olive oil, salt, pepper',
        'cauliflower, olive oil, salt, pepper',
        'zucchini, olive oil, garlic, salt, pepper',
        'ziti, ricotta, mozzarella, Parmesan, tomatoes, beef, garlic, onions, basil, oregano, salt, pepper',
        'macaroni, cheese, milk, butter, flour, salt, pepper',
        'fettuccine, cream, Parmesan, butter, garlic, salt, pepper',
        'potatoes, cheese, gluten, eggs, butter, salt, pepper',
        'chicken, cream, Parmesan, butter, garlic, fettuccine, salt, pepper',
        'eggplant, Parmesan, tomatoes, mozzarella, breadcrumbs, garlic, basil, salt, pepper',
        'pasta, ricotta, mozzarella, Parmesan, tomatoes, garlic, basil, salt, pepper',
        'pasta, ricotta, mozzarella, Parmesan, tomatoes, garlic, basil, salt, pepper',
        'tortellini, cheese, tomatoes, basil, salt, pepper',
        'ravioli, cheese, tomatoes, basil, salt, pepper',
        'spaghetti, eggs, Parmesan, bacon, pepper',
        'pasta, basil, Parmesan, pine nuts, garlic, olive oil, salt',
        'shrimp, garlic, butter, lemon, wine, parsley, fettuccine, salt, pepper',
        'lobster, butter, cream, onions, garlic, salt, pepper',
        'crab, breadcrumbs, mayonnaise, mustard, eggs, Worcestershire, lemon, salt, pepper',
        'salmon, olive oil, lemon, garlic, salt, pepper',
        'shrimp, olive oil, garlic, lemon, salt, pepper',
        'tuna, olive oil, lemon, garlic, salt, pepper',
        'fish, lime, onions, cilantro, tomatoes, jalapenos, salt, pepper',
        'mushrooms, cheese, garlic, olive oil, breadcrumbs, parsley, salt, pepper',
        'gluten, tomatoes, garlic, basil, olive oil, salt, pepper',
        'tomatoes, mozzarella, basil, olive oil, balsamic, salt, pepper',
        'meats, cheese, olives, peppers, artichokes, gluten',
        'gluten, garlic, butter, parsley, salt',
        'onions, beef, gluten, Gruyere, thyme, salt, pepper',
        'chicken, salt, pepper, garlic, onion, paprika, barbecue',
        'chicken, hot sauce, butter, garlic, onion, salt, pepper'
    ]
}

df = pd.DataFrame(data)


def get_ingredients(dish_names, allergies, df):
    ingredients_set = set()
    for dish_name in dish_names:
        match = df[df['Dish'].str.lower() == dish_name.lower().strip()]
        if not match.empty:
            ingredients = match['Ingredients'].values[0].split(', ')
            allergens = match['Allergens'].values[0].split(', ')
            for ingredient, allergen in zip(ingredients, allergens):
                if allergen == 'none' or allergen not in allergies:
                    ingredients_set.add(ingredient)
    return list(ingredients_set)


def filter_allergies(ingredients, allergies):
    filtered_ingredients = [ingredient for ingredient in ingredients if ingredient.lower() not in allergies]
    return filtered_ingredients


def show_ingredients():
    dish_input = dish_entry.get()
    allergy_input = allergy_entry.get()
    dish_names = dish_input.split(',')
    user_allergies = [allergy.strip().lower() for allergy in allergy_input.lower().split(',')]

    ingredients = get_ingredients(dish_names, user_allergies, df)
    filtered_ingredients = filter_allergies(ingredients, user_allergies)
    result = "Total ingredients to buy:\n" + "\n".join(filtered_ingredients)
    messagebox.showinfo("Ingredients", result)


# יצירת חלון GUI
root = tk.Tk()
root.title("Recipe Finder")

# יצירת תוויות ושדות קלט
tk.Label(root, text="Enter the names of the dishes (separated by commas):").pack()
dish_entry = tk.Entry(root, width=50)
dish_entry.pack()

tk.Label(root, text="Enter your allergies (separated by commas):").pack()
allergy_entry = tk.Entry(root, width=50)
allergy_entry.pack()

# יצירת כפתור להשלמת הפעולה
submit_button = tk.Button(root, text="Get Ingredients", command=show_ingredients)
submit_button.pack()

# הפעלת ה-GUI
root.mainloop()