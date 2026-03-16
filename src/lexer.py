# analisador léxico - aluno 1

from typing import List, Tuple
from string import ascii_uppercase

class LexError (Exception):
    ...


expression = r'((4.83 3 //) 12 *)' 

_OP = r"+-*/%^"
_ABC= ascii_uppercase

def parseExpressao(linha: str, _tokens_:List[Tuple[str, str, int]]) -> List[str]:
    length = len(linha)
    state = estadoEntrada
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

def estadoNumero(linha: str, index: int = 0, _tokens_=List[str]) -> int:
    full_num = ""
    index0 = index
    while (index < len(linha) and 
           (linha[index].isdecimal() or 
            linha[index] == '.')):
        
        full_num += linha[index]
        index += 1
    
    # tratar números malformados (e.g. 3.14.5)
    if full_num.count('.') > 1:
        return None
    
    _tokens_.append(("NUM", full_num, index0))

    return estadoEntrada, index, _tokens_

def estadoOperador(linha: str, index: int = 0, _tokens_=List[str]) -> int:
    # note que todos os operadores são de apenas um caracter, exceto
    # divisão inteira (//)
    if linha[index:index+2] == '//':
        _tokens_.append(("OP", '//', index))
        index += 2
    else:
        _tokens_.append(("OP", linha[index], index))
        index += 1
        
    return estadoEntrada, index, _tokens_

def estadoWhiteSpace(linha: str, index: int = 0, _tokens_=List[str]) -> int:
    # não tokenizamos whitespace
    while index < len(linha) and linha[index].isspace():
        index += 1
    
    return estadoEntrada, index, _tokens_

def estadoParenteses(linha: str, index: int = 0, _tokens_=List[str]) -> int:
    while index < len(linha) and linha[index] in '()':
        if linha[index] == '(':
            _tokens_.append(("LPAREN", linha[index], index))
        else:
            _tokens_.append(("RPAREN", linha[index], index))
        index += 1
        
    return estadoEntrada, index, _tokens_

def estadoRES(linha: str, index: int = 0, _tokens_=List[str]) -> int:
    index0 = index
    # o próximo valor de RES deve ser parenteses ou whitespace
    if index + 3 < len(linha) and not linha[index+3] in '() ':
        return None
    
    index += 3
    _tokens_.append(("RES", "RES", index0))
        
    return estadoEntrada, index, _tokens_

def estadoMEM(linha:str, index: int = 0, _tokens_=List[str]) -> int:
    full_MEM = ""
    index0 = index
    while index < len(linha) and linha[index] in _ABC:
        full_MEM += linha[index]
        index += 1
    
    _tokens_.append(("MEM", full_MEM, index0))
        
    return estadoEntrada, index, _tokens_