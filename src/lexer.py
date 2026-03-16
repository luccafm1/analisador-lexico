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

def parseExpressao(linha: str, _tokens_:List[Tuple[str, str, int]]) -> List[str]:
    length = len(linha)
    state = ...
    idx = 0
    while idx < length:
        res = state(linha, idx, _tokens_)
        if res is None:
            raise LexError(f'caractere inválido ou malformado: `{linha[idx]}` na posição {idx}')
        state, idx, _tokens_ = res
    
    _tokens_.sort(key=lambda f: f[2]) 

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

def testar_lexer():
    """
    Testa o analisador léxico com entradas válidas e inválidas.
    Deve cobrir todos os casos exigidos pelo enunciado.
    """
    pass