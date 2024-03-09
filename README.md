<<<<<<< HEAD
# Описание библиотеки FindWay

Библиотека FindWay предназначена для поиска кратчайшего пути между двумя точками на карте. Она разработана на языке программирования Python и использует алгоритмы поиска пути, такие как алгоритм Дейкстры или алгоритм A*.

## Установка

Для установки библиотеки FindWay, выполните следующие шаги:

1. Склонируйте репозиторий с библиотекой с помощью команды:
```
git clone https://github.com/DimaChepuchtanov/Tickets.git
```

2. Перейдите в папку с библиотекой:
```
cd Tickets/Labrery/FindWay
```

3. Установите необходимые зависимости с помощью команды:
```
pip install -r requirements.txt
```

## Использование

Для использования библиотеки FindWay, импортируйте модуль и создайте объект класса FindWay:
```python
from findway import FindWay

fw = FindWay()
```

Затем вызовите метод `find_shortest_path` для поиска кратчайшего пути между двумя точками на карте. Метод принимает координаты начальной и конечной точки, а также карту с препятствиями:
```python
start = (0, 0)
end = (5, 5)
obstacles = [(1, 1), (2, 2), (3, 3)]

path = fw.find_shortest_path(start, end, obstacles)
print(path)
```

## Пример

Пример использования библиотеки FindWay для поиска кратчайшего пути на карте:

```python
from findway import FindWay

fw = FindWay()

start = (0, 0)
end = (5, 5)
obstacles = [(1, 1), (2, 2), (3, 3)]

path = fw.find_shortest_path(start, end, obstacles)
print(path)
```

## Автор

Библиотека FindWay была разработана Дмитрием Чепучтановым. Связаться с ним можно по электронной почте: d.chepuchtanov@gmail.com.

## Лицензия

Эта библиотека распространяется под лицензией MIT. Подробности можно узнать в файле `LICENSE` в корне репозитория.
![alt text](iconSite.png)
=======
### Официальная библиотека системы FindWay
![alt text](iconSite.png)
>>>>>>> 93ef3652baccd882ca0fe5f3b653406f72a2d494
