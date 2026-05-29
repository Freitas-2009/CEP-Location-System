"""
Este módulo contém todas as ferramentas de comunicação com APIs do projeto.
"""

import requests

def buscar_cep(cep: str) -> dict:
    """
    Essa função recebe cep cpp parâmetro e devolve informações sobre o endereço.
    \n cep: string
    \n return: dict
    """
    if cep.isnumeric and len(cep) == 8:
        resposta = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}", timeout=10)
        return resposta.json()
    raise ValueError("Somente permitido CEPs numéricos com 8 digitos.")

