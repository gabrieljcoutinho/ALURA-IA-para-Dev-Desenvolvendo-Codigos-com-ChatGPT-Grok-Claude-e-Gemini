import re

def censurar_texto(texto_original, lista_palavras):
    """
    Substitui as palavras de uma lista por asteriscos no texto original.
    Mantém o mesmo número de caracteres da palavra original (ex: 'ruim' vira '****').

    Args:
        texto_original (str): O texto a ser processado.
        lista_palavras (list): Lista de strings com as palavras a serem censuradas.

    Returns:
        str: Texto com as palavras substituídas.
    """

    if not lista_palavras:
        return texto_original

    # Ordenamos a lista por tamanho (decrescente) para evitar que palavras curtas
    # que são prefixos de palavras longas causem conflito na substituição.
    lista_ordenada = sorted(lista_palavras, key=len, reverse=True)

    # Criamos uma expressão regular única.
    # re.escape garante que caracteres especiais nas palavras não quebrem o regex.
    # O uso de \b garante "fronteira de palavra", ou seja, só substitui a palavra exata.
    padrao = r'\b(' + '|'.join(re.escape(palavra) for palavra in lista_ordenada) + r')\b'

    # Função auxiliar que calcula quantos asteriscos usar baseado no tamanho da palavra encontrada
    def substituir(match):
        palavra_encontrada = match.group(0)
        return "*" * len(palavra_encontrada)

    # Faz a substituição ignorando maiúsculas/minúsculas (re.IGNORECASE)
    texto_censurado = re.sub(padrao, substituir, texto_original, flags=re.IGNORECASE)

    return texto_censurado

# Bloco principal para testar o código
if __name__ == "__main__":
    # Exemplo de texto
    texto = "Este é um texto com palavras sensíveis que precisam ser bloqueadas. O sistema é muito ruim e feio."

    # Lista de palavras para censurar
    palavras_para_censurar = ["sensíveis", "ruim", "feio", "bloqueadas"]

    print("-" * 50)
    print("TEXTO ORIGINAL:")
    print(texto)
    print("-" * 50)

    resultado = censurar_texto(texto, palavras_para_censurar)

    print("TEXTO CENSURADO:")
    print(resultado)
    print("-" * 50)

    # Teste interativo (Opcional)
    print("\n--- Teste Rápido ---")
    entrada_usuario = input("Digite uma frase para testar agora: ")
    if entrada_usuario:
        print("Resultado: ", censurar_texto(entrada_usuario, palavras_para_censurar))