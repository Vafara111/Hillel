# x = b"test"
#
# x = "test"
#
# x = x.encode("utf-8")
# print(type(x))
# print(x)
#
# x = x.decode("utf-8")
# print(type(x))
# print(x)
#
from collections import OrderedDict

x = {"name": "ab", "age": 21, "height": 2.1, "a": [{"abv" : 1234, "vba": 4321}, {"jty":7980}]}
# print(x["name"])
# x["city"] = "Dnipro"
# print(x)
# print(x["city"])
# x = dict(name= "ab", age= 21, height= 2.1, city= "Dnipro")
# print(x)
#
# print(hash("test"))
#
# print(x.get("a4", False))
# print(x.keys())
# print(x.values())
# print(x.items())
#
# print(x.pop("name"))
# print(x)
# x.popitem()
# print(x)

x.update({"khf": 19})
print(x)

# from collections import OrderedDict, defaultdict, namedtuple
# OrderedDict(x)
# defdict = defaultdict(list)
# print(defdict["qwerty"])
#
# point = namedtuple("Point", "name, x y")
# p = point("AB", 1, 2)
# print(p.name)