# Leitura de arquivo e gerador de Assembly ARMv7
import sys

def lerArquivo():
    """
    Lê o arquivo passado via argumento de linha de comando linha a linha
    e retorna lista de strings (uma por linha, sem '\n').
    """
    if len(sys.argv) < 2:
        print("Erro: nenhum arquivo fornecido. Passe um arquivo como parametro", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]

    try:
        with open(path, "r", encoding="utf-8") as f:
            linhas = [linha.rstrip("\n") for linha in f]

    except FileNotFoundError:
        print(f"Erro: arquivo '{path}' não encontrado.", file=sys.stderr)
        sys.exit(1)

    except OSError as e:
        print(f"Erro ao abrir '{path}': {e}", file=sys.stderr)
        sys.exit(1)

    return linhas

def gerarAssembly(tokens):
    """
    Recebe lista de tuplas ('TIPO', 'valor', posição) do parseExpressao e gera código Assembly ARMv7.
    Tipos possíveis: NUM, OP, LPAREN, RPAREN, MEM, RES.
    """
    linhas = []

    # Cabeçalho
    linhas.append(".global _start")
    linhas.append(".data")
    linhas.append("")
    linhas.append(".text")
    linhas.append("_start:")

    # Habilitar VFP via FPEXC
    linhas.append("    @ Habilitar VFP")
    linhas.append("    VMRS r0, FPEXC")
    linhas.append("    ORR  r0, r0, #0x40000000")
    linhas.append("    VMSR FPEXC, r0")
    linhas.append("")

    # Rodapé
    linhas.append("_end:")
    linhas.append("    B _end")

    return "\n".join(linhas)