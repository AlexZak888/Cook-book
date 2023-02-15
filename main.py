with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        dish_name = dish.strip()
        count_of_ingredients = int(file.readline())
        ingredients = []
        for i in range(count_of_ingredients):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingredients
    print(f'cook_book = {cook_book}')