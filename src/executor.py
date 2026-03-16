# Executor de expressões RPN e gerenciamento de memória


def executarExpressao():
    """
    Avalia uma expressão RPN a partir dos tokens gerados por parseExpressao.
    Usa uma pilha para resolver as operações.
    """
    pass

def testar_executor():
    """
    Testa a execução de expressões e comandos especiais.
    Deve cobrir operações simples, aninhadas e comandos RES/MEM.
    """
    pass
from lexer import parseExpressao, LexError

"""
executarExpressao.py

Avalia as expressões produzidas em lexer.py

Formato do Token esperado: tupla (tipo, valor, posição)
    ("NUM", "3.14", 2)
    ("OP", "+", 7)
    ("LPAREN", "(", 0)
    ("RPAREN", ")", 9)
    ("RES", "RES", 5)
    ("MEM", "VAR", 3)

Depende de:
    lexer.py -> parseExpressao, LexError

"""

# Constantes - tipos de token do lexer

T_NUM = "NUM"
T_OP = "OP"
T_LPAREN = "LPAREN"
T_RPAREN = "RPAREN"
T_RES ="RES"
T_MEM = "MEM"


# Funções para auxiliar na identificaçãomdos itens do token

def tipo(token: tuple) -> str:
    return token[0]

def valor(token: tuple) -> str:
    return token[1]

def index(token: tuple) -> int:
    return token[2]


# Exceções específicas de execução

class ErroDivisaoPorZero(Exception):
    pass

class ErroExpressaoInvalida(Exception):
    pass

class ErroMemoriaNaoInicializada(Exception):
    pass
class ErroHistoricoInvalido(Exception):
    pass

#Converter linha em tokens utilizando o lexer

def tokenizar(linha : str) -> str:
    """Chama a parseExpressao do Lexer e retorna lista de de tokens
        propaga LexError se tiverem símbolos inválidos
    """

    tokens = []
    parseExpressao(linha, tokens)
    return tokens


def encontrar_fechamento(tokens: list, inicio: int) -> int:
    """
    tokens[inicio] é um LPAREN, a função retorna o RPAREN
    correspondente (mesmo nível de profundidade)
    """
    profundidade = 0
    i = inicio

    while i < len(tokens):
        if tipo(tokens[i]) == T_LPAREN:
            profundidade += 1
        elif tipo(tokens[i]) == T_RPAREN:
            profundidade -= 1
            if profundidade == 0:
                return i
        i += 1
    raise ErroExpressaoInvalida(
        f"Parêntese aberto na posição {tokens[inicio]} não foi fechado!"
    )