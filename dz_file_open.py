from pprint import pprint

# 1 Задача

cook_book = {}

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    dishes = ''
    for x in file:
        x = x.strip()
        if x.isdigit():
            continue
        elif x and '|' not in x:
            cook_book[x] = []
            dishes = x
        elif x and '|' in x:
            a, b, c = x.split(" | ")
            cook_book.get(dishes).append(dict(ingredient_name=a, measure=c, quantity=int(b)))
pprint(cook_book)
print()

# Задача 2 

def get_shop_list_by_dishes(dishes_list, person_count):
    shop_list = {}
    for dish in dishes_list:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    shop_list[ingredient['ingredient_name']] = ({'measure': ingredient['measure'], 'quantity':
                                                                (ingredient['quantity'] * person_count)})
        else:
            print('Такого блюда нет в книге')
    return shop_list
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))

# 3 Задача 

lines = {}
file_name = {}
with open('1.txt') as file:
   count_1 = 0 
   lines_1 = []
   for line in file:
      count_1 +=1
      lines_1.append(line)  
lines.update({count_1 : lines_1})
file_name.update({count_1 : '1.tx'})

with open('2.txt') as file:
   count_2 = 0 
   lines_2 = []
   for line in file:
      count_2 +=1
      lines_2.append(line)  
lines.update({count_2 : lines_2})
file_name.update({count_2 : '2.tx'})  

with open('3.txt') as file:
   count_3 = 0 
   lines_3 = []
   for line in file:
      count_3 +=1
      lines_3.append(line)  
lines.update({count_3 : lines_3}) 
file_name.update({count_3 : '3.tx'})  

sorted_lines = dict(sorted(lines.items()))
sorted_file_name = dict(sorted(file_name.items()))

for keys, value in sorted_file_name.items():
   with open('answer.txt', 'a') as f:
      f.write(f'{value} \n{keys}\n')
      f.flush
      key = sorted_lines[keys]
      count = 1 
      for line in key:
         f.write(f'Строка номер {count} - {line}')
         count += 1
         f.flush
      f.write('\n')