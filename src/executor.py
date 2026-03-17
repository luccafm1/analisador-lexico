# Executor de expressões RPN e gerenciamento de memória
from lexer import parseExpressao, LexError

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

def preprocessar_aninhamento(tokens: list, memoria: dict, historico: list) -> list:
    """
    Resolve expressões aninhadas de dentro para fora. Cada iteração:

    - Lê a lista completa de tokens da esquerda para a direita
    - Ao encontrar um LPAREN cujointerior não tem outros LPAREN, identifica
      como o mais interno, avalia com a pilha e substitui o segmento com o 
      valor calculado token NUM
    - Reinicia a varredura
    - Para quando o único LPAREN restante é da função externa
    
    """

    while True:
        encontrou = False

        for i in range(len(tokens)):
            if tipo(tokens[i]) != T_LPAREN:
                continue
            fechamento = encontrar_fechamento(tokens, i)
            interior = tokens[ i+1 : fechamento]

            #Procura outro aninhamento; se tiver, pula pra próxima iteração
            tem_aninhado = any(tipo(t) == T_LPAREN for t in interior)

            if tem_aninhado:
                continue
            
            #Verifica se tem LPAREN fora do aninhamento
            externos = [
                t for t in (tokens[:i] + tokens[fechamento + 1])
                if tipo(t) == T_LPAREN
            ]
            if not externos:
                # Final da expressão
                break
            #Avalia expressão plana mais interna
            sub_tokens = tokens[i : fechamento + 1]
            resultado = _avaliar_expressao_plana(sub_tokens, memoria, historico) #falta implementar

            #Cria token NUM com o resultado (posição 0 como placeholder)
            token_resultado = (T_NUM, repr(resultado), 0)

            #Substitui o segmento pelo token resultado
            tokens = tokens[:i] + [token_resultado] + tokens[fechamento + 1]
            encontrou = True
            break
        if  not encontrou:
            break
    return tokens

