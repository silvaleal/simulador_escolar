# Programador: @ojoser1 - AUTOBOTS 2023
# Contato: joseeer27@gmail.com

import os # Não requer instalação
import sqlite3  # pip install db-sqlite3.
import random  # Não requer instalação.
import time  # Não requer instalação
# import dashboard

# Observações:
# -> No banco de dados (SQLite3), chamei os professores de instrutores, então fique obvío que, professor = instrutor :)
# -> ID = Identificador
# -> Caso queira ler mais sobre analise de dados, vá para a linha 205, lá você irá encontrar comentários.
# -> Novato na programação? Não se esqueça de assistir vídeos-aulas e ler códigos de algo com o seu nível. Exemplo: Dev novato ler códigos básicos.

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
        print('')
        print('inicie o  arquivo chamado "dashboard.py" para obter um gráfico dos nossos professores.')
        print('')
        input('PRESSIONE "ENTER" PARA CONTINUAR.')

# Neste projeto quero que os ids (identificados) tenham 5 digítos.
# E esses digitos sejam todos aleatórios.
def gerar_id(): # Função para gerar o id (identificador) dos cursos, professores e alunos.
    return random.randint(10000, 99999)

def procurar_curso(curso_id): # Também irá verificar se o curso procurado existe.
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

def contar_faltas(pessoa):
    pass

def verificar_eventos():
    pass

while True:
    escolha_menu()
