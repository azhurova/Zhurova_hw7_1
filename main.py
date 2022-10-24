#1 ЗАДАНИЕ
cook_book = {}
dish_list = []
with open('file_1', 'rt', encoding='utf8') as file:
    for l in file:
        dish_name = l.strip()
        ingredients_list = []
        dish = {dish_name: ingredients_list}
        dish_count = file.readline()
        for i in range(int(dish_count)):
            dsh = file.readline().strip().split(' | ')
            ingredients_list.append({'ingredient_name': dsh[0], 'quantity': int(dsh[1]), 'measure': dsh[2]})
            dish_list.append(dish)
        blank_line = file.readline()
        cook_book.update(dish)
    import pprint
    pprint.pprint(cook_book)


#2 ЗАДАНИЕ
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for loc in cook_book[dish]:
                person_q = int(loc['quantity']) * person_count
                dict_list = {loc['ingredient_name']: {'measure': loc['measure'], 'quantity': person_q}}
                shop_list.update(dict_list)
        return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))