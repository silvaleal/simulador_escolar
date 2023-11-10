import sqlite3
from functions.funcao_geral import *

# LOCAL RESERVADO PARA AS FUNÇÕES QUE ENVOLVEM OS EVENTOS

def verificar_faltas(aluno_nome): # Veja quantas faltas um aluno/professor possui.
    try:
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute(f'SELECT * FROM faltas WHERE pessoa_nome = "{aluno_nome}"')
        resultado = cursor.fetchall()
        conexao.close()
        return resultado # Para contar as faltas, use o len().

    except Exception as error:
        print(f'Erro encontrado: {error}')

def aumentar_falta(nome, tipo, data):
    try:
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute(f'''INSERT INTO faltas (
            pessoa_id, pessoa_nome, pessoa_tipo, data) VALUES ({pegar_id(nome, tipo)}, "{nome}", "{tipo}", "{pegar_data_atual()})''')
        resultado = cursor.fetchall()
        conexao.close()
        return resultado # Para contar as faltas, use o len().

    except Exception as error:
        print(f'Erro encontrado: {error}')

def remover_falta(data): # Mude de "FALTA" para "FALTA JUSTIFICADA"
    # REMOÇÃO IRÁ ACONTECER PELA DATA
    try:
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute(f'DELETE FROM faltas WHERE data = "{data}"')
        resultado = cursor.fetchall()
        conexao.close()
        return resultado # Para contar as faltas, use o len().

    except Exception as error:
        print(f'Erro encontrado: {error}')