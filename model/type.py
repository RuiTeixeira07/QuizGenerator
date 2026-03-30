from dataclasses import dataclass

@dataclass(frozen=True)
class Type:
    value: str

    @staticmethod
    def create_type_from(value: str) -> Type:
        for type in ALL:
            if type.value == value:
                return type

        return EMPTY

EMPTY = Type("")
MULTIPLE_CHOICE = Type("Multiple Choice")
TRUE_OR_FALSE = Type("True or False")
ALL = [MULTIPLE_CHOICE, TRUE_OR_FALSE]