from __future__ import annotations
from lark import Lark

from model import CppClass
from transformer import MyTransformer
# from utils import make_png, make_transformed_png


with open("grammar.lark") as file:
    parser = Lark(file, start="document")


sentence = \
"""\
Classes:
class Vehicle {
   +int id
}
class Car: Vehicle {
   +int id
}
"""

o = MyTransformer().transform(parser.parse(sentence))

with open("r.cpp", "w") as f:
    class_: CppClass
    for class_ in o.children:
        f.write(class_.gen_stmt())
