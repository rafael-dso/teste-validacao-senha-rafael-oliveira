import pytest
from src.rules import (MinimumLengthRule, DigitRule, CaseRule, SpecialCharacterRule, NoRepetitionRule)
from src.validator import PasswordValidator

def test_deve_validar_senha_correta_do_desafio():
    regras = [
        MinimumLengthRule(9), 
        DigitRule(),
        CaseRule(),
        SpecialCharacterRule(),
        NoRepetitionRule()
    ]
    validator = PasswordValidator(regras)
    assert validator.validate("Ab@1CdEfG") is True
    assert len(validator.errors) == 0

def test_deve_rejeitar_senha_com_caractere_repetido():
    regras = [NoRepetitionRule()]
    validator = PasswordValidator(regras)
    assert validator.validate("Abc@123Aa") is False
    assert len(validator.errors) > 0
