# import json

# class Foo():
#     def __init__(self):
#         self.x = 1
#         self.y = 2

# json.dump(Foo(), "file.json") # TypeError: Object of type Foo is not JSON serializable

import json

class Foo():
    def __init__(self):
        self.x = 1
        self.y = 2

foos = [Foo(), Foo(), Foo()]
with open("file.json", "w") as f:
    json.dump(foos, f, indent=4) # TypeError: Object of type Foo is not JSON serializable