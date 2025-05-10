from dataclasses import dataclass, field
from enum import Enum, auto
from os import access


class AccessLevel(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()
    
    PUBLIC = auto()
    PROTECTED = auto()
    PRIVATE = auto()


@dataclass
class Attribute:
    access_level: AccessLevel
    data_type: str
    name: str
    
    def gen_getter_setter(self) -> str:
        getter = f"""\
            {self.data_type} get{self.name.capitalize()}() {{
                return {self.name};
            }}\
            """
        setter = f"""\
            void set{self.name.capitalize()}({self.data_type} {self.name}) {{
                this->{self.name} = {self.name}
            }}\
            """
        return f"{getter}\n{setter}"
    
    def gen_decl(self) -> str:
        return f"{self.data_type} {self.name};"


@dataclass
class CppClass:
    name: str
    inherits_from: list[str] = field(default_factory=list)
    attributes: list[Attribute] = field(default_factory=list)
    
    def gen_stmt(self) -> str:
        class_name = f"class {self.name}"
        if self.inherits_from:
            access_level_added = ["public " + _class_name for _class_name in self.inherits_from]
            class_name += ": "
            class_name += ", ".join(access_level_added)
        class_name += " {\n"
        
        # attributes
        private_attrs = [attribute for attribute in self.attributes if attribute.access_level == AccessLevel.PRIVATE]
        protected_attrs = [attribute for attribute in self.attributes if attribute.access_level == AccessLevel.PROTECTED]
        public_attrs = [attribute for attribute in self.attributes if attribute.access_level == AccessLevel.PUBLIC]
        
        
        for attr in private_attrs:
            class_name += "\t" + attr.gen_decl() + "\n"
        
        if protected_attrs:
            class_name += "protected:\n"        
            for attr in protected_attrs:
                class_name += "\t" + attr.gen_decl() + "\n"
        
        if public_attrs:
            class_name += "public:\n"
            for attr in public_attrs:
                class_name += "\t" + attr.gen_decl() + "\n"
        
        # getters and setters
        if "public:" not in class_name:
            class_name += "public:\n"
        
        for attr in private_attrs + protected_attrs:
            class_name += attr.gen_getter_setter() + "\n"
        
        return class_name + "};"
