g1 = set(globals().keys())

import contextlib

g2 = set(globals().keys())
print(g2 - g1)

import numpy as np

g3 = set(globals().keys())
print(g3 - g2)

from contextlib import closing

g4 = set(globals().keys())
print(g4 - g3)

from contextlib import *
g5 = set(globals().keys())
print(g5 - g4)


# Как работает import
import sys
print(sys.modules)  # кэш
print(sys.meta_path) # смотрим здесь
# PathFinder ищет здесь
print(sys.path)
# Можно через PYTHONPATH прокидывать собственные пути


# Импортируем наш модуль
import module
print(dir(module))
# Запустим module через python


# Пакеты
import package.a
import package.b
from package import a
from package import *
print(b)