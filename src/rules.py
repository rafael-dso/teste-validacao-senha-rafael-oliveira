from abc import ABC, abstractmethod

class PasswordRule(ABC):
    @abstractmethod
    def is_valid(self, password: str) -> bool:
        pass
    @property
    @abstractmethod
    def error_message(self) -> str:
        pass


class MinimumLengthRule(PasswordRule):
    def __init__(self, min_length: int = 9):
        self.min_length = min_length
    def is_valid(self, password: str) -> bool:
        return len(password) >= self.min_length
    @property
    def error_message(self) -> str:
        return f"A senha deve ter pelo menos {self.min_length} caracteres."

class DigitRule(PasswordRule):
    def is_valid(self, password: str) -> bool:
        return any(char.isdigit() for char in password)
    @property
    def error_message(self) -> str:
        return "A senha deve conter ao menos 1 dígito numérico."

class CaseRule(PasswordRule):
    def is_valid(self, password: str) -> bool:
        has_lower = any(char.islower() for char in password)
        has_upper = any(char.isupper() for char in password)
        return has_lower and has_upper
    @property
    def error_message(self) -> str:
        return "A senha deve conter ao menos uma letra maiúscula e uma minúscula."

class SpecialCharacterRule(PasswordRule):
    ALLOWED = "@#$%^&*()-+"
    def is_valid(self, password: str) -> bool:
        return any(char in self.ALLOWED for char in password)
    @property
    def error_message(self) -> str:
        return f"A senha deve conter ao menos um caractere especial: {self.ALLOWED}"

class NoRepetitionRule(PasswordRule):
    def is_valid(self, password: str) -> bool:
        return len(set(password)) == len(password)
    @property
    def error_message(self) -> str:
        return "A senha não pode conter caracteres repetidos."