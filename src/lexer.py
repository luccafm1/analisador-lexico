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

def estadoEntrada(linha: str, index: int = 0, _tokens_=List[str]) -> int:
    if linha[index].isdecimal() : return estadoNumero, index, _tokens_
    if linha[index] in _OP      : return estadoOperador, index, _tokens_
    if linha[index] in '()'     : return estadoParenteses, index, _tokens_
    if (index + 2 < len(linha)) and \
        linha[index:index + 3] == 'RES': 
        return estadoRES, index, _tokens_
    if linha[index] in _ABC     : return estadoMEM, index, _tokens_
    if linha[index].isspace()   : return estadoWhiteSpace, index, _tokens_
    
    
    return None # <- token inválido

def estadoNumero():
    pass

def estadoOperador():
    pass

def estadoParenteses():
    pass

def estadoMEM():
    pass

def estadoRES():
    pass

def estadoWhiteSpace():
    pass
