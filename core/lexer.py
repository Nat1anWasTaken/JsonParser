from typing import Iterable

from core.token import Token, get_tokens_in_order


class Lexer:
    def __init__(self, code: str):
        self.code: str = code

        self.current_index: int = 0

        self.token_types = get_tokens_in_order()

    def lex(self) -> Iterable[Token]:
        while self.current_index < len(self.code):
            for token in self.__get_next_token():
                yield token

            continue

    def __get_next_token(self):
        for token_type in Token.__subclasses__():
            matched_token, end_pos = token_type.match_next(self.code[self.current_index:])

            if matched_token:
                self.current_index += end_pos
                yield matched_token

            continue
