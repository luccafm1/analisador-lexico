# Analisador Léxico — Autômato Finito Determinístico (AFD)
# ATENÇÃO: uso de expressões regulares é PROIBIDO.
# Cada estado do AFD deve ser implementado como uma função separada.

from typing import List, Tuple
from string import ascii_uppercase

class LexError (Exception):
    ...


expression = r'((4.83 3 //) 12 *)' 

_OP = r"+-*/%^"
_ABC= ascii_uppercase

def estado_inicial():
    pass

def estado_numero():
    pass

def estado_ponto():
    pass

def estado_decimal():
    pass

def estado_sinal():
    pass

def estado_barra():
    pass

def estado_identificador():
    pass

def estado_erro():
    pass


def parseExpressao():
    """
    Analisa uma linha de expressão RPN e retorna uma lista de tokens.
    Implementado como AFD, cada estado é uma função.
    NÃO usa expressões regulares.
    """
    pass

def testar_lexer():
    """
    Testa o analisador léxico com entradas válidas e inválidas.
    Deve cobrir todos os casos exigidos pelo enunciado.
    """
    pass