from lark import Lark, tree

from model import AccessLevel, Attribute, CppClass
from transformer import MyTransformer

with open("grammar.lark") as file:
    parser = Lark(file, start="document")


sentence = \
"""\
Classes:
class Student : Hello, Jello {
   +int id
}
class tSudent : Hello, Jello {
   +int id
}
"""

# Inheritances:
# Student : Person

def make_png(filename):
    tree.pydot__tree_to_png( parser.parse(sentence), filename)

def make_transformed_png(filename):
    tree.pydot__tree_to_png( MyTransformer().transform(parser.parse(sentence)), filename)

# parser.parse(sentence)
o = MyTransformer().transform(parser.parse(sentence))

# o = CppClass("Hello", attributes=[Attribute(AccessLevel.PROTECTED, 'int', 'val')])
# print(o.children)
# make_transformed_png("hello.png")
with open("r.cpp", "w") as f:
    class_: CppClass
    for class_ in o.children:
        f.write(class_.gen_stmt())
# make_png("hello.png")