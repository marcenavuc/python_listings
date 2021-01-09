# globals()
# locals()

a = 1

def f():
    # print(globals())
    # global a 
    a = 2
    print(locals())
    def g():
        print(globals())
        nonlocal a # Если этой переменной нет, то вызовет ошибку
        print(locals())
        a = 3
        print(locals())
        print(a)
    g()
    print(a)

f()
print(a)


def scope_test():
    def do_local():
        spam = "lcoal spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print(spam)
    do_nonlocal()
    print(spam)
    do_global()
    print(spam)

scope_test()
print(spam)