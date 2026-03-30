from dataclasses import dataclass

@dataclass(frozen=True)
class Difficulty:
    value: str

    @staticmethod
    def create_difficulty_from(value: str) -> Difficulty:
        for difficulty in ALL:
            if difficulty.value == value:
                return difficulty

        return EMPTY

EMPTY = Difficulty("")
EASY = Difficulty("Easy")
INTERMEDIATE = Difficulty("Intermediate")
HARD = Difficulty("Hard")
ALL = [EASY, INTERMEDIATE, HARD]