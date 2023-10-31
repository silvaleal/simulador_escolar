# Programador: @ojoser1 - AUTOBOTS 2023
# Contato: joseeer27@gmail.com

import os # Não requer instalação
import sqlite3  # pip install db-sqlite3.
import random  # Não requer instalação.
import time  # Não requer instalação

# Observações:
# -> No banco de dados (SQLite3), chamei os professores de instrutores, então fique obvío que, professor = instrutor :)
# -> ID = Identificador
# -> Caso queira ler mais sobre analise de dados, vá para a linha 205, lá você irá encontrar comentários.
# -> Novato na programação? Não se esqueça de assistir vídeos-aulas e ler códigos de algo com o seu nível. Exemplo: Dev novato ler códigos básicos.

# NOTA DO DEV:
# -> Note que eu não irei usar o EXCEL, prefiro usar SQL.

# Aprender é bom, mas aprender a programar é melhor ainda.

def menu(): # Atual menu do simulador
    print('')
    print(' Simulador escolar - 2023')
    print(' 1. Verificar alunos')
    print(' 2. Verificar professores')
    print(' 3. Verificar cursos')
    print(' 4. Registrar aluno')
    print(' 5. Registrar professor')
    print(' 6. Registrar curso')
    print(' 7. Analisar os dados ★')


def escolha_menu(): # Responsável pela escolha do usuário.
    menu()
    escolha = input('Digite o número: ')

    if escolha == '1':
        print('')
        print(verificar_alunos())
        input('PRESSIONE "ENTER" PARA CONTINUAR.')
    elif escolha == '2':
        print('')
        print(verificar_professores())
        input('PRESSIONE "ENTER" PARA CONTINUAR.')
    elif escolha == '3':
        print('')
        print(verificar_cursos())
        input('PRESSIONE "ENTER" PARA CONTINUAR.')
    elif escolha == '4':
        nome = input('Digite o nome COMPLETO do aluno. \n')
        print('')
        print('Nossos cursos disponíveis.')
        print(verificar_cursos())

        try:
            curso = int(input('Digite o ID do curso escolhido. \n'))
            pesquisa_curso = procurar_curso(curso)
            if pesquisa_curso:
                registrar_aluno(nome, pesquisa_curso[1])
                print('')
                print(f' Aluno "{nome}" foi registrado no sistema.')
                print('')
                input('PRESSIONE "ENTER" PARA CONTINUAR.')
            else:
                print('')
                print('Curso não encontrado')
                input('PRESSIONE "ENTER" PARA CONTINUAR.')

        except Exception as error:
            print(f'Erro encontrado: {error}')
    elif escolha == '5':
        nome = input('Digite o nome COMPLETO do professor. \n')
        idade = int(input('Digite a idade do professor. \n'))
        salario = int(input('Digite o salário do professor. \n'))
        registrar_professor(nome, idade, salario)
        print('')
        print(f' Professor "{nome}" foi registrado no sistema.')
        print('')
        input('PRESSIONE "ENTER" PARA CONTINUAR.')
    elif escolha == '6':
        nome = input('Digite o nome do curso. \n')
        professor = input('Digite o nome COMPLETO do professor. \n')
        registrar_curso(nome, professor)
        print('')
        print(f' Curso "{nome}"foi registrado no sistema.')
        print(f' Responsável: {professor}.')
        print('')
        input('PRESSIONE "ENTER" PARA CONTINUAR.')
    elif escolha == '7':
        print('Algo feito ;c. Sorry')

# Neste projeto quero que os ids (identificados) tenham 5 digítos.
# E esses digitos sejam todos aleatórios.
def gerar_id(): # Função para gerar o id (identificador) dos cursos, professores e alunos.
    return random.randint(10000, 99999)

def registrar_aluno(nome, curso):
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conex = sqlite3.connect('database.db')
        cursor = conex.cursor()

        cursor.execute(
            f'INSERT INTO alunos (aluno_id, aluno_nome, aluno_curso) VALUES ({gerar_id()}, "{nome}", "{curso}")')
        conex.commit()
    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')
    finally:  # Ação que irá acontecer no final, é opcional, afinal eu poderia fechar a conexão no "try".
        conex.close()


def registrar_professor(nome, idade, salario):
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conex = sqlite3.connect('database.db')
        cursor = conex.cursor()

        cursor.execute(
            f'INSERT INTO instrutores (instrutor_id, instrutor_nome, instrutor_idade, instrutor_salario) VALUES ({gerar_id()}, "{nome}", {idade}, {salario})')
        conex.commit()
    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')
    finally:  # Ação que irá acontecer no final, é opcional, afinal eu poderia fechar a conexão no "try".
        conex.close()


def registrar_curso(nome, instrutor):
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conex = sqlite3.connect('database.db')
        cursor = conex.cursor()

        cursor.execute(
            f'INSERT INTO cursos (curso_id, curso_nome, curso_instrutor) VALUES ({gerar_id()}, "{nome}", "{instrutor}")')
        conex.commit()
    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')
    finally:  # Ação que irá acontecer no final, é opcional, afinal eu poderia fechar a conexão no "try".
        conex.close()


def verificar_alunos():
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conex = sqlite3.connect('database.db')
        cursor = conex.cursor() 

        cursor.execute('SELECT * FROM alunos')

        alunos_encontrados = '' # String que irá receber o ID e o NOME dos cursos.
        
        for aluno_id, aluno_nome, aluno_curso in cursor.fetchall():
            alunos_encontrados += f'ID: {aluno_id} | ALUNO: {aluno_nome} - CURSO: {aluno_curso}\n'
        return alunos_encontrados

    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')
    finally:  # Ação que irá acontecer no final, é opcional, afinal eu poderia fechar a conexão no "try".
        conex.close()


def verificar_professores():
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conex = sqlite3.connect('database.db')
        cursor = conex.cursor() 

        cursor.execute('SELECT * FROM instrutores')

        professores_encontrados = '' # String que irá receber o ID e o NOME dos cursos.
        
        for professor_id, professor_nome, professor_idade, professor_salario in cursor.fetchall():
            professores_encontrados += f'ID: {professor_id} | PROFESSOR: {professor_nome} de {professor_idade} anos - R${professor_salario}\n'
        return professores_encontrados

    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')
    finally:  # Ação que irá acontecer no final, é opcional, afinal eu poderia fechar a conexão no "try".
        conex.close()


def verificar_cursos():
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conex = sqlite3.connect('database.db')
        cursor = conex.cursor() 

        cursor.execute('SELECT curso_id, curso_nome FROM cursos')

        curso_encontrados = '' # String que irá receber o ID e o NOME dos cursos.
        
        for curso_id, curso_nome in cursor.fetchall():
            curso_encontrados += f'ID: {curso_id} | CURSO: {curso_nome}\n'
        return curso_encontrados

    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')
    finally:  # Ação que irá acontecer no final, é opcional, afinal eu poderia fechar a conexão no "try".
        conex.close()

def procurar_curso(curso_id):
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conex = sqlite3.connect('database.db')
        cursor = conex.cursor() 

        cursor.execute(f'SELECT curso_id, curso_nome FROM cursos WHERE curso_id = {curso_id}')
        resultado = cursor.fetchone()
        if resultado:
            return resultado
        else:
            return None

    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')
    finally:  # Ação que irá acontecer no final, é opcional, afinal eu poderia fechar a conexão no "try".
        conex.close()

while True:
    escolha_menu()
