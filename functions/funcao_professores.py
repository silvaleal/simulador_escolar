import sqlite3


# LOCAL RESERVADO PARA AS FUNÇÕES QUE ENVOLVEM OS PROFESSORES

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