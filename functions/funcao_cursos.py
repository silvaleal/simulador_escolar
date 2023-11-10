import sqlite3
from functions.funcao_geral import *

# LOCAL RESERVADO PARA AS FUNÇÕES QUE ENVOLVEM OS CURSOS

def registrar_curso(nome, instrutor):
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute(
            f'INSERT INTO cursos (curso_id, curso_nome, curso_instrutor) VALUES ({gerar_id()}, "{nome}", "{instrutor}")')
        conexao.commit()
        conexao.close()
    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')
        
def verificar_cursos():
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor() 

        cursor.execute('SELECT curso_id, curso_nome FROM cursos')

        curso_encontrados = '' # String que irá receber o ID e o NOME dos cursos.
        
        for curso_id, curso_nome in cursor.fetchall():
            curso_encontrados += f'ID: {curso_id} | CURSO: {curso_nome}\n'
        conexao.close()
        return curso_encontrados

    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')

def procurar_curso(curso_id):
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor() 

        cursor.execute(f'SELECT curso_id, curso_nome FROM cursos WHERE curso_id = {curso_id}')
        resultado = cursor.fetchone()
        conexao.close()
        if resultado:
            return resultado
        else:
            return None

    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')