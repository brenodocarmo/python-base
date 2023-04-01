#!/bin/env python3
"""Cadastro de produto"""
__version__ = "0.1.0"

from pprint import pprint

produto = {
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "cor2": "branco",
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None
}

cliente = {
    "nome": "Breno do Carmo",
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
}

total_compra = compra["quantidade"] * compra["produto"]["preco"]


# pprint(compra)

print(
    f"O cliente {compra['cliente']['nome']} "
    f"e comprou R$ {compra['produto']['nome']}"
    f" e pagou o total de R${total_compra}"
    )

# print(
#     f"O cliente {compra[0]}  comprou {compra[1]} "
#     f"e pagou o total de R${total_compra}"
#     )
