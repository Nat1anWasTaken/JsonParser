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
        Check if the value fit into this token type, if so, return the token and the last index of the token
        :param value:
        :return: Token and the last index of the token
        """
        raise NotImplementedError


class String(Token):
    priority: int = 0

    def __init__(self, value: str):
        super().__init__(value)

    @classmethod
    def match_next(cls, value: str) -> Tuple[Optional["Token"], int]:
        if value.startswith("\""):
            end_pos = value.find("\"", 1)

            if end_pos == -1:
                raise ValueError("Invalid string")

            return cls(value[0:end_pos + 1]), end_pos + 1

        return None, 0


class Number(Token):
    priority: int = 0

    def __init__(self, value: str):
        super().__init__(value)

    @classmethod
    def match_next(cls, value: str) -> Tuple[Optional["Token"], int]:
        if value[0].isdigit():
            end_pos = 1

            while end_pos < len(value) and value[end_pos].isdigit():
                end_pos += 1

            return cls(value[0:end_pos]), end_pos

        return None, 0


class LCurlyBracket(Token):
    regex: Pattern = re.compile(r"{")
    priority: int = 1

    def __init__(self, value: str):
        super().__init__(value)

    @classmethod
    def match_next(cls, value: str) -> Tuple[Optional["Token"], int]:
        if value.startswith("{"):
            return cls("{"), 1

        return None, 0


class RCurlyBracket(Token):
    priority: int = 1

    def __init__(self, value: str):
        super().__init__(value)

    @classmethod
    def match_next(cls, value: str) -> Tuple[Optional["Token"], int]:
        if value.startswith("}"):
            return cls("}"), 1

        return None, 0


class LSquareBracket(Token):
    priority: int = 1

    def __init__(self, value: str):
        super().__init__(value)

    @classmethod
    def match_next(cls, value: str) -> Tuple[Optional["Token"], int]:
        if value.startswith("["):
            return cls("["), 1

        return None, 0


class RSquareBracket(Token):
    regex: Pattern = re.compile(r"]")
    priority: int = 1

    def __init__(self, value: str):
        super().__init__(value)

    @classmethod
    def match_next(cls, value: str) -> Tuple[Optional["Token"], int]:
        if value.startswith("]"):
            return cls("]"), 1

        return None, 0


class Colon(Token):
    priority: int = 2

    def __init__(self, value: str):
        super().__init__(value)

    @classmethod
    def match_next(cls, value: str) -> Tuple[Optional["Token"], int]:
        if value.startswith(":"):
            return cls(":"), 1

        return None, 0


class Whitespace(Token):
    regex: Pattern = re.compile(r"\s+")
    priority: int = 5

    def __init__(self, value: str):
        super().__init__(value)

    @classmethod
    def match_next(cls, value: str) -> Tuple[Optional["Token"], int]:
        match = cls.regex.match(value)

        if match:
            return cls(match.group()), len(match.group())

        return None, 0


def get_tokens_in_order():
    return sorted(Token.__subclasses__(), key=lambda x: x.priority)
