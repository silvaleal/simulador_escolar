# Programador: @ojoser1 - AUTOBOTS 2023
# Contato: joseeer27@gmail.com
# Simulador Escolar V1 (terminal)

import sqlite3  # pip install db-sqlite3.
import random  # Não requer instalação.
import time  # Não requer instalação
from functions.funcao_alunos import *
from functions.funcao_cursos import *
from functions.funcao_eventos import *
from functions.funcao_professores import *
from functions.cores import *

# Observações:
# -> No banco de dados (SQLite3), chamei os professores de instrutores, então fique obvío que, professor = instrutor :)
# -> ID = Identificador
# -> Novato na programação? Não se esqueça de assistir vídeos-aulas e ler códigos de algo com o seu nível. Exemplo: Dev novato ler códigos básicos.

# Aprender é bom, mas aprender a programar é melhor ainda.
# Leia para descobrir mais informações do projeto em nosso PDF oficial. (apresentação/autobots.pdf)

def menu_faltas():
    print()
    print(' MENU FALTA ')
    print(' 1. Verificar faltas')
    print(' 2. Remover faltas')
    print(' 3. Adicionar faltas')

def menu():  # Atual menu do simulador
    print(corYELLOW) # Além de criar um espaço, irá colocar o menu amarelo.
    print(' Simulador escolar - 2023')
    print(' 1. Verificar alunos')
    print(' 2. Verificar professores')
    print(' 3. Verificar cursos')
    print(' 4. Verificar eventos')
    print(' 5. Registrar aluno')
    print(' 6. Registrar professor')
    print(' 7. Registrar curso')
    print(' 8. Registrar evento')

def escolha_menu():  # Responsável pela escolha do usuário.
    menu()
    escolha = input(f' -> Digite o número: {corDefault}')

    if escolha == '1': # Verificar alunos
        print('')
        print(verificar_alunos())
        escolha = input(f'{corYELLOW} PRESSIONE "ENTER" PARA VOLTAR AO MENU.{corDefault} ')

    elif escolha == '2': # Verificar professores 
        print('')
        print(verificar_professores())
        input(f'{corYELLOW} PRESSIONE "ENTER" PARA VOLTAR AO MENU.{corDefault}')

    elif escolha == '3': # Verificar cursos
        print('')
        print(verificar_cursos())
        input(f'{corYELLOW} PRESSIONE "ENTER" PARA VOLTAR AO MENU.{corDefault}')

    elif escolha == '4': # Verificar eventos
        print('')
        print(verificar_eventos())
        input(f'{corYELLOW} PRESSIONE "ENTER" PARA VOLTAR AO MENU.{corDefault}')

    elif escolha == '5': # Registrar aluno
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
    
    elif escolha == '6': # Registrar professor
        nome = input('Digite o nome COMPLETO do professor. \n')
        idade = int(input('Digite a idade do professor. \n'))
        salario = int(input('Digite o salário do professor. \n'))
        registrar_professor(nome, idade, salario)
        print('')
        print(f' Professor "{nome}" foi registrado no sistema.')
        print('')
        input('PRESSIONE "ENTER" PARA VOLTAR AO MENU.')
    
    elif escolha == '7': # Registrar curso
        nome = input('Digite o nome do curso. \n')
        professor = input('Digite o nome COMPLETO do professor. \n')
        registrar_curso(nome, professor)
        print('')
        print(f' Curso "{nome}"foi registrado no sistema.')
        print(f' Responsável: {professor}.')
        print('')
        input('PRESSIONE "ENTER" PARA VOLTAR AO MENU.')
    
    elif escolha == '8': # Registrar evento
        print('')
        nome = input("Digite o nome do evento. ")
        print(verificar_professores())
        responsavel_nome = input("Digite o NOME COMPLETO do responsável. ")
        data = input("Digite a data que irá ocorrer. Exemplo: 10/11/2023 ")
        registrar_evento(nome, responsavel_nome, data)
        print('')
        print(f' Evento "{nome}" foi registrado com sucesso')
        print(f' Data marcado: {data} | Responsável: {responsavel_nome}')
        print('')
        input('PRESSIONE "ENTER" PARA VOLTAR AO MENU.')

    elif escolha == '9': # Converter dados SQL para excel.
        converter_para_excel()

while True:
    escolha_menu()
