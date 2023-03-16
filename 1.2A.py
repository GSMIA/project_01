# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

random_3_list = random.sample (my_favorite_songs, 3)
min = 0
sec = 0
print ('Случайным образом были выбраны песни:', random_3_list)
for i in range(len(random_3_list)): 
    min = int(min + int(random_3_list[i][1]))
    sec = sec + random_3_list[i][1] - int(random_3_list[i][1])
    sec = round(sec,2)

if sec >= 0.6:
    min = min+sec//0.60
    sec = sec-(sec//0.6)*0.6
print ('Три песни звучат', min+sec, 'минут')

