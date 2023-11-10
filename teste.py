from functions.funcao_faltas import *
from functions.funcao_geral import *
from functions.funcao_alunos import *

aluno = input('Qual o nome do aluno?')
if procurar_aluno(aluno):
    print(pegar_id('João', 'aluno'))
else:
    print('Aluno não encontrado.')