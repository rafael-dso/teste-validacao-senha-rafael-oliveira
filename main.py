from src.rules import (MinimumLengthRule, DigitRule, CaseRule, 
                       SpecialCharacterRule, NoRepetitionRule)
from src.validator import PasswordValidator

regras = [
    MinimumLengthRule(9),
    DigitRule(),
    CaseRule(),
    SpecialCharacterRule(),
    NoRepetitionRule()
]

validator = PasswordValidator(regras)

testes = ["Abc@123Aa", "Ab@1CdEfG"]
for senha in testes:
    valida = validator.validate(senha)
    print(f"Senha: {senha} | Válida: {valida}")
    if not valida:
        print(f"Erros: {validator.errors}")