import re
import sys
import time
import random

from python3ptbr.__main__ import Help

palavras_reservadas = {
    'se': 'if',
    'senão': 'else',
    'ouse': 'elif',
    'imprimir': 'print',
    'enquanto': 'while',
    'para': 'for',
    'em': 'in',
    'ou': 'or',
    'Verdadeiro': 'True',
    'Falso': 'False',
    'inteiro': 'int',
    'flutuante': 'float',
    'cadeia': 'str',
    'função': 'def',
    'retornar': 'return',
    'classe': 'class',
    'importar': 'import',
    'de': 'from',
    'Nada': 'None',
    'entrada': 'input',
    'tempo': 'time',
    'dormir': 'sleep',
    'sistema': 'system',
    'aleatório': 'random',
}


def traduzir_codigo_br_para_python(codigo_br):
    for palavra_br, palavra_python in palavras_reservadas.items():
        codigo_br = re.sub(rf'\b{palavra_br}\b', palavra_python, codigo_br)

    return codigo_br

def executar_script_br(arquivo_br):
    try:
        with open(arquivo_br, 'r') as arquivo:
            codigo_br = arquivo.read()
            codigo_python = traduzir_codigo_br_para_python(codigo_br)
            exec(codigo_python)
    except FileNotFoundError:
        print(f"O arquivo '{arquivo_br}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao executar o arquivo: {e}")


def main():
    if len(sys.argv) != 2:
        print("Uso: python3ptbr <arquivo.pybr>")
        sys.exit(1)

    arquivo_br = sys.argv[1]

    if arquivo_br.endswith(".pybr"):
        executar_script_br(arquivo_br)
    else:
        print(f"O arquivo '{arquivo_br}' não possui a extensão .pybr")


if __name__ == "__main__":
    main()
    
