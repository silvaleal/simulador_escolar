import sqlite3
from functions.funcao_geral import *

# LOCAL RESERVADO PARA AS FUNÇÕES QUE ENVOLVEM OS EVENTOS

def verificar_eventos(): # Todos os eventos
    try:
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM eventos')

        eventos_encontrados = ''

        for evento_id, evento_nome, evento_responsável, evento_data in cursor.fetchall():
            eventos_encontrados += f'ID: {evento_id} | EVENTO: {evento_nome}({evento_responsável}) - DATA: {evento_data}\n'
        return eventos_encontrados

    except Exception as error:
        print(f'Erro encontrado: {error}')

def verificar_evento(): # Algum evento específico
    pass

def registrar_evento(nome, responsavel_nome, data):
    try:
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute(f'''INSERT INTO eventos (
            evento_id, evento_nome, evento_responsável, evento_data) VALUES ({gerar_id()}, "{nome}", "{responsavel_nome}", "{data}")''') # 
        conexao.commit()
        conexao.close()

    except Exception as error:
        print(f'Erro encontrado: {error}')

def procurar_evento(nome): # Verificar se algum evento existe.
    try:
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute(f'SELECT evento_status FROM eventos WHERE evento_nome = "{nome}"')
        resultado = cursor.fetchone()
        conexao.close()
        if resultado:
            return resultado
        else:
            return False

    except Exception as error:
        print(f'Erro encontrado: {error}')