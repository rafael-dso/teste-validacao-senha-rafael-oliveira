from typing import List
from src.rules import PasswordRule

class PasswordValidator:
    def __init__(self, rules: List[PasswordRule]):
        self._rules = rules
        self._errors = []

    def validate(self, password: str) -> bool:
        self._errors = []
        for rule in self._rules:
            if not rule.is_valid(password):
                self._errors.append(rule.error_message)
        return len(self._errors) == 0

    @property
    def errors(self) -> List[str]:
        return self._errors
