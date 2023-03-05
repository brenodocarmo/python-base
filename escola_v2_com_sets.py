#!/bin/env python3
"""Exibi relatorio de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades
"""
__version__ = "0.1.1"

# Dados
sala1 = ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erick", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("ingles", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança", aula_danca),
]

# Requerimentos
# Listar alunos em cada ativiade por sala

for nome_atividade, atividade in atividades:
    # sala1 que tem interseção ocm a atividade
    
    # Primeira forma
    atividade_sala1 = set(sala1).intersection(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)


    # Segunda forma
    # atividade_sala1 = set(sala1) & set(atividade)
    # atividade_sala2 = set(sala2) & set(atividade)



    print("Atividade de ", nome_atividade)
    print("-" * 33)
    print("sala 1", atividade_sala1)
    print("sala 2", atividade_sala2)
    print("=" * 33)
