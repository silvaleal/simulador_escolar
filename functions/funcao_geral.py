import random
import sqlite3
from datetime import datetime
from functions.funcao_geral import *
import pandas as pd
import os

# Neste projeto quero que os ids (identificados) tenham 5 digítos.
# E esses digitos sejam todos aleatórios.
def gerar_id():  # Função para gerar o id (identificador) dos cursos, professores e alunos.
    return random.randint(10000, 99999)

def pegar_id(nome, tipo): # Função para pegar o id de acordo com o tipo (usando nome)
    # TIPOS: CURSO, ALUNO, PROFESSOR
    try:
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        if tipo.lower() == 'curso':
            cursor.execute(f'SELECT curso_id FROM cursos WHERE curso_nome = "{nome}"')
            return int(cursor.fetchall()[0][0])
        elif tipo.lower() == 'aluno':
            cursor.execute(f'SELECT aluno_id FROM alunos WHERE aluno_nome = "{nome}"')
            return int(cursor.fetchall()[0][0])
        elif tipo.lower() == 'professor':
            cursor.execute(f'SELECT instrutor_id FROM instrutores WHERE instrutor_nome = "{nome}"')
            return int(cursor.fetchall()[0][0])
        else:
            return False
    except Exception as error:
        print(f'Erro encontrado: {error}')

def pegar_data_atual():
    data = datetime.now()
    return f"{data.day}/{data.month}/{data.year}"

def converter_para_excel():
    print('')
    print(' 1. ALUNOS')
    print(' 2. PROFESSORES')
    print(' 3. EVENTOS')
    print(' 4. CURSOS')
    print('')
    tipo = input('QUAL A ÁREA QUE DESEJA EXPORTAR? ')
    if tipo == '1':
        tipo = 'alunos'

    if tipo == '2':
        tipo = 'instrutores'

    if tipo == '3':
        tipo = 'eventos'

    if tipo == '4':
        tipo = 'cursos'
    
    df = pd.read_sql(f'SELECT * FROM {tipo}', sqlite3.connect('database.db'))
    data = pegar_data_atual().split('/')
    try:
        df.to_excel(f'./pdfs/{tipo}_{data[0]}_{data[1]}_{data[2]}.xlsx', index=False)
    except Exception as error:
        os.mkdir('./pdfs')
        df.to_excel(f'./pdfs/{tipo}_{data[0]}_{data[1]}_{data[2]}.xlsx', index=False)

# Criar um EXCEL com os dados do SQL (Perfeito para mandar emails ;c)

# Sistema para atualizar o SQL com oq foi editado no EXCEL. (Perfeito para quem prefere melhor em EXCEL)
# ATENÇÃO: É ALTAMENTE RECOMENDADO APENAS UMA PESSOA FICAR RESPONSÁVEL PELAS ATUALIZAÇÕES