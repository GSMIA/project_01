# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
for i in my_favorite_songs_dict:
    my_favorite_songs_dict[i]=format(my_favorite_songs_dict[i], '.2f')
from random import sample
play_list = list(my_favorite_songs_dict.items())
play_list_of_3 = sample(play_list, 3)
print ('Случайным образом выбраны песни:', play_list_of_3)
from datetime import timedelta, datetime
delta = timedelta (minutes=0, seconds=0)
time = 0
for i in range(len(play_list_of_3)):
    t = datetime.strptime(str(play_list_of_3[i][1]),"%M.%S")
    delta = delta + timedelta(minutes=t.minute, seconds=t.second)
print ('Три песни звучат ', delta.seconds//60, '.', format(delta.seconds%60, '02d'), " минут", sep="")
# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

