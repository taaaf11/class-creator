from lark import Transformer

from model import AccessLevel, Attribute, CppClass


class MyTransformer(Transformer):
    def class_def(self, children):
        class_name = children[0]
        inherits_from = children[1]
        attributes = children[2:]
        
        return CppClass(class_name, inherits_from, attributes)
        
    def inheritance_def(self, children):
        return children
        
    def attr_def(self, children):
        return children[0]

    def public_attr_def(self, children):
        return Attribute(access_level=AccessLevel.PUBLIC, data_type=children[0], name=children[1])
    
    def protected_attr_def(self, children):
        return Attribute(access_level=AccessLevel.PROTECTED, data_type=children[0], name=children[1])
    
    def private_attr_def(self, children):
        return Attribute(access_level=AccessLevel.PRIVATE, data_type=children[0], name=children[1])
    
    def ATTR_NAME(self, token: str):
        return token.value
    
    def DATA_TYPE(self, token: str):
        return token.value

    def CLASS_NAME(self, token):
        # print("Class name!", token)
        return token.value
    ...