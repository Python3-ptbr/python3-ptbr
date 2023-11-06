import re

# Dicionário de palavras reservadas
palavras_reservadas = {
    'se': 'if',
    'senão': 'else',
    'imprimir': 'print',
    'enquanto': 'while',
    'para': 'for',
    'em': 'in',
    'verdadeiro': 'True',
    'falso': 'False',
    'inteiro': 'int',
    'flutuante': 'float',
    'cadeia': 'str',
    'função': 'def',
    'retornar': 'return',
    'classe': 'class',
    'importar': 'import',
    'de': 'from',
    'senão_se': 'elif',
    'nada': 'None',
    'entrada': 'input',
}


# Função para traduzir código .br para código Python
def traduzir_codigo_br_para_python(codigo_br):
    for palavra_br, palavra_python in palavras_reservadas.items():
        codigo_br = re.sub(rf'\b{palavra_br}\b', palavra_python, codigo_br)

    return codigo_br

# Função para executar um script .br
def executar_script_br(arquivo_br):
    with open(arquivo_br, 'r') as arquivo:
        codigo_br = arquivo.read()
        codigo_python = traduzir_codigo_br_para_python(codigo_br)
        exec(codigo_python)

# Exemplo de uso
if __name__ == "__main__":
    arquivo_br = "exemplo.br"
    executar_script_br(arquivo_br)
