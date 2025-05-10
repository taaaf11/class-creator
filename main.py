from __future__ import annotations
from lark import Lark

from model import CppClass
from transformer import MyTransformer
# from utils import make_png, make_transformed_png

from argparse import ArgumentParser


def parse_args():
    arg_parser = ArgumentParser(prog='class-creator', description="Create class using mermaid's classDiagram like slntax.")
    arg_parser.add_argument(
        "FILE_NAME",
        help="Name of file containing code for generating class.",
    )
    arg_parser.add_argument(
        "-o",
        "--output",
        default="class.cpp",
        help="Name of output file. Optional, defaults to class.cpp.",
    )
    
    return arg_parser.parse_args()


cmd_args = parse_args()

with open("grammar.lark") as file:
    parser = Lark(file, start="document")

with open(cmd_args.FILE_NAME, "r") as f:
    transformed_tree = MyTransformer().transform(parser.parse(f.read()))

with open(cmd_args.output, "w") as f:
    class_: CppClass
    for class_ in transformed_tree.children:
        f.write(class_.gen_stmt())
        f.write("\n")
