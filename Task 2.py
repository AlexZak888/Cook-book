def get_shop_list_by_dishes(dishes, person_count):
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
        # print(f'cook_book = {cook_book}')
    shop_list_by_dishes = {}
    for every_dish in dishes:
        if every_dish in cook_book.keys():
            for every_ingredients in cook_book[every_dish]:
                key = every_ingredients['ingredient_name']
                if key in shop_list_by_dishes.keys():
                    shop_list_by_dishes[key]['quantity'] += int(every_ingredients['quantity']) * person_count
                else:
                    mes = every_ingredients['measure']

                    shop_list_by_dishes[key] = {'quantity': int(every_ingredients['quantity']) * person_count, 'measure': mes}

    return (shop_list_by_dishes)


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))