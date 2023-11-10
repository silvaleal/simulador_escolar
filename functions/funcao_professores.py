import sqlite3
from functions.funcao_geral import *

# LOCAL RESERVADO PARA AS FUNÇÕES QUE ENVOLVEM OS PROFESSORES

def verificar_professores():
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor() 

        cursor.execute('SELECT * FROM instrutores')

        professores_encontrados = '' # String que irá receber o ID e o NOME dos cursos.
        
        for professor_id, professor_nome, professor_idade, professor_salario in cursor.fetchall():
            professores_encontrados += f'ID: {professor_id} | PROFESSOR: {professor_nome} de {professor_idade} anos - R${professor_salario}\n'
        conexao.close()
        return professores_encontrados

    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')

def registrar_professor(nome, idade, salario):
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute(
            f'INSERT INTO instrutores (instrutor_id, instrutor_nome, instrutor_idade, instrutor_salario) VALUES ({gerar_id()}, "{nome}", {idade}, {salario})')
        conexao.commit()
        conexao.close()
    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')

def procurar_professor(nome):
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        cursor.execute(f'SELECT * FROM instrutores WHERE instrutor_nome = "{nome}"')
        resultado = cursor.fetchone()
        conexao.close()

        if resultado:
            return resultado
        else:
            return None

    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')