import re
from abc import ABC
from re import Pattern
from typing import Optional, Tuple


class Token(ABC):
    regex: Pattern = re.compile(r"")
    priority: int = 0

    def __init__(self, value: str):
        self.value: str = value

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.value}>"

    @classmethod
    def match_next(cls, value: str) -> Tuple[Optional["Token"], int]:
        """
        Check if the value matches the regex, if it does, return the token.
        :param value:
        :return: LCurlyBracket and the last index of the token
        """
        result = cls.regex.search(value)

        if (not result) or (not result.start() == 0):
            return None, 0

        return cls(result.group(0)), result.end()

    @classmethod
    def get_tokens_in_order(cls):
        return sorted(cls.__subclasses__(), key=lambda x: x.priority)


class String(Token):
    regex: Pattern = re.compile(r'".*?"')
    priority: int = 0

    def __init__(self, value: str):
        super().__init__(value)


class Number(Token):
    regex: Pattern = re.compile(r"\d+")
    priority: int = 0

    def __init__(self, value: str):
        super().__init__(value)


class LCurlyBracket(Token):
    regex: Pattern = re.compile(r"{")
    priority: int = 1

    def __init__(self, value: str):
        super().__init__(value)


class RCurlyBracket(Token):
    regex: Pattern = re.compile(r"}")
    priority: int = 1

    def __init__(self, value: str):
        super().__init__(value)


class LSquareBracket(Token):
    regex: Pattern = re.compile(r"\[")
    priority: int = 1

    def __init__(self, value: str):
        super().__init__(value)


class RSquareBracket(Token):
    regex: Pattern = re.compile(r"]")
    priority: int = 1

    def __init__(self, value: str):
        super().__init__(value)


class Colon(Token):
    regex: Pattern = re.compile(r":")
    priority: int = 2

    def __init__(self, value: str):
        super().__init__(value)


class Whitespace(Token):
    regex: Pattern = re.compile(r"\s+")
    priority: int = 5

    def __init__(self, value: str):
        super().__init__(value)
