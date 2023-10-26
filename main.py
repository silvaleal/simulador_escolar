# Programador: @ojoser1
import os
import sqlite3  # pip install db-sqlite3.
import random  # Não requer instalação.
import time  # Não requer instalação

# Obs.: No banco de dados, chamei os professores de instrutores, então fique obvío que, professor = instrutor :)


def menu():
    print('')
    print(' Simulador escolar - 2023')
    print(' 1. Verificar alunos')
    print(' 2. Verificar professores')
    print(' 3. Verificar curso')
    print(' 4. Registrar aluno')
    print(' 5. Registrar professor')
    print(' 6. Registrar curso')
    print('')


def escolha_menu():
    menu()
    escolha = input('Digite o número: ')

    if escolha == '1':
        pass
    elif escolha == '2':
        pass
    elif escolha == '3':
        pass
    elif escolha == '4':
        pass
    elif escolha == '5':
        nome = input('Digite o nome COMPLETO do professor. \n')
        idade = int(input('Digite a idade do professor. \n'))
        salario = int(input('Digite o salário do professor. \n'))
        registrar_professor(nome, idade, salario)
        print('')
        print(f' Professor "{nome}" foi registrado no sistema.')
        print('')
        time.sleep(1) # Estarei usando o delay de 1s, fazendo assim, o menu só voltar a aparecer dps de um 1 segundo que a mensagem acima for enviada.
        
    elif escolha == '6':
        nome = input('Digite o nome do curso. \n')
        professor = input('Digite o nome COMPLETO do professor. \n')
        registrar_curso(nome, professor)
        print('')
        print(f' Curso "{nome}"foi registrado no sistema.')
        print(f' Responsável: {professor}.')
        print('')
        time.sleep(1) # Estarei usando o delay de 1s, fazendo assim, o menu só voltar a aparecer dps de um 1 segundo que a mensagem acima for enviada.


def gerar_id():
    return random.randint(10000, 99999)


def registrar_aluno():
    pass


def registrar_professor(nome, idade, salario):
    try:  # Isto é um tratamento de erro, caso o código dentro do "try" esteja certo, ele vai acontecer normalmente.
        conex = sqlite3.connect('database.db')
        cursor = conex.cursor()

        cursor.execute(
            f'INSERT INTO instrutores (instrutor_id, instrutor_nome, instrutor_idade, instrutor_salario) VALUES ({gerar_id()}, "{nome}", {idade}, {salario})')
        conex.commit()
    except Exception as error:  # Caso o código dentro do "try" esteja errado, ele irá entrar aqui. :)
        print(f'Erro encontrado: {error}')
    finally:  # Ação que irá acontecer no final, é opção, afinal eu poderia ficar a conexão no "try".
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
    finally:  # Ação que irá acontecer no final, é opção, afinal eu poderia ficar a conexão no "try".
        conex.close()


def verificar_aluno():
    pass


def verificar_professor():
    pass


def verificar_curso():
    try:
        conex = sqlite3.connect('database.db')
    except Exception as error:
        print(f'Erro encontrado: {error}')
    finally:
        conex.close

while True:
    escolha_menu()
