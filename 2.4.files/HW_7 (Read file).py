import os
from pprint import pprint
path = os.path.join(os.getcwd(), 'recipes.txt')

with open(path, encoding='utf-8') as file:
    cook_book = {}
    for bludes in file:
        bluded_name = bludes.strip()
        count = int(file.readline().strip())
        all_ingredient = []
        for item in range(count):
            ingred, quantity, measure = file.readline().split('|')
            ingredient = {'ingredient_name': ingred, 'quantity': int(quantity), 'measure': measure.strip()}
            all_ingredient.append(ingredient)
        file.readline()
        cook_book[bluded_name] = all_ingredient

# Задание № 2

def my_f(dishes, person_count):
  my_dict = {}
  for bludes, ing in cook_book.items():
    for n_dishes in dishes:
      if n_dishes == bludes:
        for all_ing in ing:
          ing_n = all_ing['ingredient_name']
          quantity = all_ing['quantity']
          measure = all_ing['measure']
          if ing_n not in my_dict:
            my_dict[ing_n] = {'quantity': quantity*person_count, 'measure': measure}
          else:
              my_dict[ing_n]['quantity'] += quantity
  pprint(my_dict)

my_f(['Омлет', 'Фахитос'], 2)
print()
my_f(['Омлет', 'Омлет'], 1)


