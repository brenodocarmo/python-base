#!/bin/env python3
"""Exibi relatorio de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades
"""
__version__ = "0.1.0"

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

for atividade in atividades:
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in aula_ingles:
        # print(aluno)
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print("Atividade de ", atividade[0])
    print("-" * 33)
    print("sala 1", atividade_sala1)
    print("sala 2", atividade_sala2)
    print("=" * 33)
