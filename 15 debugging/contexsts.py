####
class File:
    def __init__(self, filename, method):
        self.file_obj = open(filename, method)

    # Когда, мы заходим в with
    def __enter__(self):
        return self.file_obj

    # Когда выходим из with
    def __exit__(self, exc_type, exc_value, traceback):
        self.file_obj.close()


with File('example.txt', 'w') as file:
    file.write('Hello')

with File("1.txt") as f1:
    with File("1_fail.txt") as f2:
        pass

with File("1.txt") as f1, File("1_fail.txt") as f2:
    pass

#####

from contextlib import contextmanager

@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print("We had an error!")
    finally:
        print('Closing file')
        f_obj.close()