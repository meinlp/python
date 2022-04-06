## LISTS:
``` python
list = [$DATA] # создание списка. Элементы разделяются запятыми, например
list.pop($INDEX) # вывод и удаление объекта с индексом $INDEX, по умолчанию последний
list.remove($DATA) # удаление объекта $DATA, если он в списке не найден - ошибка
list.append($DATA) # динамическое добавление объекта $DATA в конец списка
list.extend($LIST) # добавление списка к списку
list.insert($INDEX, $DATA) # вставка объекта $DATA перед индексом $INDEX

var.split() # разделяет var на элементы и формирует список
''.join(list) # объединяет list в один стринг, разделяя элементы '' (можно сюда вставить делиметр)
```

## DICTIONARIES:
``` python
dict = {} # dictionary init
dict["key"] = value # adding/changing key-value pair
```

## VARIABLES:
``` python
len(var) # считает размер переменной, ну или количество элементов, если речь о списке
round(var, int) # округление var до int после запятой
```

## RANDOMIZATION
``` python
import random
var = random.randint(1, 999) # генерация рандома от 1 до 999
random.random() # рандомный float от 0 до 1
random.choice(list) # рандомный элемент из list
random.shuffle(list) # перемешивает элементы list
```

## SLICING LISTS
``` python
keys = ["a", "b", "c", "d", "e", "f"]
print(keys[2:5])	# взять элементы с 2 по 5 не включительно, отсчет с нуля
['c','d','e']
print(keys[2:5:2])	# взять элементы с 2 по 5 с шагом 2
['c','e']
print(keys[2:])	# зять элементы с 2 до конца
['c','d','e','f']
```