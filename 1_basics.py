from collections import defaultdict, Counter, namedtuple
import heapq
import enum

# Tuple
a = tuple()
a = ()
a = 12, 13
a = ('s', )
a = tuple("Hello, world!")
print(a)

# Операции
print(a.index("l"))
print(a[0])
print(a[1:5])
print(a.count("l"))

# List
a = list()
a = list("Hello")
a = []
a = [1,2,3]

# Операции
a.append(1)
a.extend([1,2,3])
a.insert(0, 10)
a.pop()

# Set
a = set("hello")
b = set("world")
# Операции
a.issubset(b)
a.union(b)
a.intersection(b)
a.difference(b)
a.add("l")
print(a)

# Dict
d = {}
d = {"a": 1, "b": 2}
d = dict(short="dict", long="dict")

print(dict.keys())
print(dict.values())
print(dict.get("some key"))

# Collections
# Counter
c = collections.Counter()
for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'spam']:
    c[word] += 1
print(c)
print(Counter({'spam': 3, 'counter': 2, 'egg': 1}))


print(c.elements())
print(c.most_common())

# Defaultdict
defdict = collections.defaultdict(list)
print(defdict)
for i in range(5):
    defdict[i].append(i)
print(defdict)

#namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(p[0])
print(p[1])

# heapq
x = [15, 5, 10, 5, 2]
heapq.heapify(x)
heapq.heappush(x, 20)
print(x)

# Enum
class Shake(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3
