import sqlite3

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