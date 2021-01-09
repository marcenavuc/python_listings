s = "Hello, world!"
print("First" + "Second")
print("spam" * 3)
print(len("spam"))
s = "spam"
s[0] # 's'
s[0:2] # 'sp'
s[0:-1] # 'spa'
s[::-1] # 'maps'
print(s.find("pa"))
print(s.replace("pa", "ap"))
print("hello, world!".split())
print(s.startswith("sp"))

# Кодировки
print("\u0394")

# unicodedata
import unicodedata

print(unicodedata.name("s"))
print(unicodedata.lookup("LATIN SMALL LETTER S"))

# Регулярки
import re

result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result)

result = re.findall(r'AV', 'AV Analytics Vidhya AV')
print(result)

result = re.findall(r'\w+', 'AV is largest Analytics community of India')
print(result)

result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print(result)
