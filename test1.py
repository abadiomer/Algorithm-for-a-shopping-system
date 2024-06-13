import pandas as pd

# יצירת מאגר נתונים של מתכונים והמצרכים
data = {
    'Dish': ['Greek Salad', 'Pizza', 'Pasta', 'Omelette'],
    'Ingredients': [
        '3 tomatoes, 3 cucumbers, large handful of rocket leaves, 5 large lettuce leaves, half pack of Bulgarian cheese, vinegar, lemon juice, olive oil, half teaspoon of salt, black pepper, black and green olives',
        'cheese, dough, tomatoes, olive oil, salt, oregano',
        'pasta, tomatoes, olive oil, garlic, basil, salt, pepper',
        'eggs, salt, pepper, butter'
    ]
}

df = pd.DataFrame(data)

def get_ingredients(dish_names, df):
    ingredients_list = []
    for dish_name in dish_names:
        match = df[df['Dish'].str.lower() == dish_name.lower().strip()]
        if not match.empty:
            ingredients_list.append(match['Ingredients'].values[0])
        else:
            ingredients_list.append(f"Recipe for {dish_name} not found.")
    return ingredients_list

# קבלת שמות המאכלים מהמשתמש
user_input = input("Enter the names of the dishes (separated by commas): ")

# פיצול רשימת שמות המאכלים
dish_names = user_input.split(',')

# פלט רשימת המצרכים לכל המאכלים
ingredients = get_ingredients(dish_names, df)
for dish_name, ingredient in zip(dish_names, ingredients):
    print(f"Ingredients for {dish_name.strip()}: {ingredient}")
