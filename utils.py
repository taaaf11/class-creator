# Inheritances:
# Student : Person

from main import parser


from lark import tree


def make_png(sentence, filename):
    tree.pydot__tree_to_png( parser.parse(sentence), filename)

def make_transformed_png(transformer, sentence, filename):
    tree.pydot__tree_to_png(transformer.transform(parser.parse(sentence)), filename)