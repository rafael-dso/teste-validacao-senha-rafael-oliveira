# teste-validacao-senha-rafael-oliveira
- Desafio Técnico de Validação de Senhas para o processo seletivo PsicoAgenda
Este projeto consiste em um validador de senhas robusto, desenvolvido para o desafio técnico do PsicoAgenda. O objetivo principal foi criar uma solução que não apenas funcione, mas que seja legível, testável, e fácil de manter.

- Arquitetura e Design de Software
Para atender aos requisitos de extensibilidade e baixo acoplamento, utilizei o Pattern Strategy
Principios SOLID aplicados:
 - SRP (Single Responsibility Principle): Cada regra de validação (comprimento, caracteres especiais, repetição, etc.) possui sua própria classe dedicada.
 - OCP (Open/Closed Principle): O sistema está aberto para novas regras (basta criar uma nova classe que herda de PasswordRule) e fechado para modificação (não precisamos alterar o PasswordValidator para adicionar critérios).
 - DIP (Dependency Inversion Principle): O validador depende de uma interface abstrata (PasswordRule), e não de implementações concretas.

- Tecnologias Utilizadas
 - Linguagem: Python 3.x
 - Testes: Pytest (para testes de unidade automatizados)
 - Versionamento: Git & GitHub

Estrutura do Projeto
teste-validacao-senha-rafael-oliveira/
src/            # Lógica principal
    - rules.py  # Imprementação das regras (Strategy)
    - validator.py # Maestro que orquestra as validações
    __init__.py
tests/          # Testes de Unidade
    - test_rules.py
    - test_validator.py
    __init__.py
main.py         # Exemplo de uso real
README.md

- Como Executar o Projeto
    1. Clonar o repositório:
    git clone https://github.com/seu-usuario/teste-validacao-senha-rafael-oliveira.git
    cd teste-validacao-senha-rafael-oliveira2
    2. Executar a aplicação (Demonstração):
    python main.py

- Como Rodar os Testes
O projeto utiliza o Pytest para garantir a qualidade do código.
    python -m pytest -v

        Nota: Os testes cobrem casos de sucesso (senhas válidas), cada violação de regra individualmente e casos de limite, conforme solicitado no desafio.

- Clean Code
    - Nomes Semânticos: Variáveis e classes nomeadas para serem autoexplicativas.
    - Testes Expressivos: O nome de cada teste expressa claramente a intenção e o cenário validado.