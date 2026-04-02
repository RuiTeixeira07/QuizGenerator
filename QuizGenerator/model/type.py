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

    @staticmethod
    def translate_type(type: Type) -> Type:
        match type.value:
            case MULTIPLE_CHOICE.value:
                return TRANSLATED_MULTIPLE_CHOICE
            case TRUE_OR_FALSE.value:
                return TRANSLATED_TRUE_OR_FALSE
            case _:
                return type

EMPTY = Type("")
MULTIPLE_CHOICE = Type("Multiple Choice")
TRUE_OR_FALSE = Type("True or False")
ALL = [MULTIPLE_CHOICE, TRUE_OR_FALSE]

TRANSLATED_MULTIPLE_CHOICE = Type("multichoice")
TRANSLATED_TRUE_OR_FALSE = Type("truefalse")