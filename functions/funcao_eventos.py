import sqlite3
from functions.funcao_geral import *

# LOCAL RESERVADO PARA AS FUNÇÕES QUE ENVOLVEM OS EVENTOS

def verificar_eventos(): # Todos os eventos
    try:
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT * FROM eventos')
        return cursor.fetchall()

    except Exception as error:
        print(f'Erro encontrado: {error}')

def verificar_evento(): # Algum evento específico
    pass

def registrar_evento(nome, responsavel_nome, data):
    try:
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute(f'''INSERT INTO eventos (
            evento_id, evento_nome, evento_responsável, evento_data, evento_status) VALUES ({gerar_id()}, "{nome}", "{responsavel_nome}", "{data}", False)''') # 
        conexao.commit()
        conexao.close()

    except Exception as error:
        print(f'Erro encontrado: {error}')

def pegar_status(nome): # Função para pegar o status de um evento.
    try:
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute(f'SELECT evento_status FROM eventos WHERE evento_nome = "{nome}"')
        resultado = cursor.fetchall()
        conexao.close()
        return resultado

    except Exception as error:
        print(f'Erro encontrado: {error}')

def mudar_status(nome): # Função que mudará o status do evento.
    try:
        resultado = procurar_evento(nome)
        if resultado:
            if resultado == True:
                # Mudar para "False"
                pass
            else:
                # Mudar para "True"
                pass
        else:
            return None

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