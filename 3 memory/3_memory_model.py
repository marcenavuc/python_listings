# __init__ - инициализация созданного объекта
# __del__ - вызывается, при удалении объекта, когда кол-во ссылок на объект == 0

class C:

    def __init__(self, i):
        self.i = i
        print(f"{i} initialized")

    def __del__(self):
        print(f"{self.i} deleted")
        # super().__del__()

def f():
    for i in range(2):
        print("Start loop")
        o = C(i)
        print("end loop")

print("before f()")
f()
print("after f()")

>>> class C:
...     pass
... 
>>> c = C(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: C() takes no arguments
>>> c = C()
>>> sys.getrefcount(c)
2
>>> sys.getrefcount(c)
2
>>> sys.getrefcount(c)
2
>>> import weakref
>>> proxy  = weakref.proxy(c)
>>> sys.getrefcount(c)
2
>>> proxy
<weakproxy at 0x7ff06997fc70 to C at 0x7ff069af0640>
>>> c.name = "Это ц"
>>> proxy.name
'Это ц'
>>> c.name
'Это ц'
>>> sys.getrefcount(c)
2
>>> del c
>>> proxy
<weakproxy at 0x7ff06997fc70 to NoneType at 0x563bdba3c360>
>>> proxy.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ReferenceError: weakly-referenced object no longer exists
>>> с = с()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'с' is not defined
>>> с = С()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'С' is not defined
>>> с = С()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'С' is not defined
>>> c = C()
>>> sys.getrefcount(c)
2
>>> c.c = c
>>> sys.getrefcount(c)
3
>>> del x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> del c
>>> sys.getrefcount(c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined
>>> c = C()
