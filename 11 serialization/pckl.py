import pickle
import pickletools


class Foo:
    attr = "Some attribute"

    def __init__(self, name):
        self.name = name


picklestring = pickle.dumps(Foo("boo"))
print(picklestring)
foo = pickle.loads(picklestring)
print(foo.name)
print(foo.attr)
print(pickletools.dis(picklestring))