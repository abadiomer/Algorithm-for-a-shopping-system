import tkinter as tk
from tkinter import messagebox
import pandas as pd

# יצירת מאגר נתונים של מתכונים, המצרכים והאלרגיות
data = {
    'Dish': ['Greek Salad', 'Pizza', 'Pasta', 'Omelette'],
    'Ingredients': [
        '3 tomatoes, 3 cucumbers, large handful of rocket leaves, 5 large lettuce leaves, half pack of Bulgarian cheese, vinegar, lemon juice, olive oil, half teaspoon of salt, black pepper, black and green olives',
        'cheese, dough, tomatoes, olive oil, salt, oregano',
        'pasta, tomatoes, olive oil, garlic, basil, salt, pepper',
        'eggs, salt, pepper, butter'
    ],
    'Allergens': [
        'none, none, none, none, dairy, none, none, none, none, none, none',
        'dairy, gluten, tomatoes, none, none, none',
        'gluten, tomatoes, none, garlic, none, none, none',
        'eggs, none, none, dairy'
    ]
}

df = pd.DataFrame(data)


def get_ingredients(dish_names, allergies, df):
    ingredients_set = set()
    for dish_name in dish_names:
        match = df[df['Dish'].str.lower() == dish_name.lower().strip()]
        if not match.empty:
            ingredients = match['Ingredients'].values[0]
            allergens = match['Allergens'].values[0].split(', ')
            for ingredient, allergen in zip(ingredients.split(', '), allergens):
                if allergen not in allergies and allergen != 'none':
                    ingredients_set.add(ingredient)
    return list(ingredients_set)


def show_ingredients():
    dish_input = dish_entry.get()
    allergy_input = allergy_entry.get()
    dish_names = dish_input.split(',')
    user_allergies = allergy_input.lower().split(',')

    ingredients = get_ingredients(dish_names, user_allergies, df)
    result = "Total ingredients to buy:\n" + "\n".join(ingredients)
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
