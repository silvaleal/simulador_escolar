import sqlite3
from functions.funcao_geral import *

# LOCAL RESERVADO PARA AS FUNÇÕES QUE ENVOLVEM OS ALUNOS

def verificar_alunos(): # Quem a lista de todos os alunos.
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor() 

        cursor.execute('SELECT * FROM alunos')

        alunos_encontrados = '' # String que irá receber o ID e o NOME dos cursos.
        
        for aluno_id, aluno_nome, aluno_curso in cursor.fetchall():
            alunos_encontrados += f'ID: {aluno_id} | ALUNO: {aluno_nome} - CURSO: {aluno_curso}\n'
        conexao.close()
        return alunos_encontrados

    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')

def verificar_um_aluno(nome): # Quem a lista de um aluno.
     # Quem a lista de todos os alunos.
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor() 

        cursor.execute(f'SELECT * FROM alunos WHERE aluno_nome = "{nome}"')
        resultado = cursor.fetchall()
        conexao.close()
        return resultado

    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')

def registrar_aluno(nome, curso):
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute(
            f'INSERT INTO alunos (aluno_id, aluno_nome, aluno_curso) VALUES ({gerar_id()}, "{nome}", "{curso}")')
        conexao.commit()
    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')
        
def procurar_aluno(nome):
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute(f'SELECT * FROM alunos WHERE aluno_nome = "{nome}"')
        resultado = cursor.fetchone()
        conexao.close()
        if resultado:
            return resultado
        else:
            return None

    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')