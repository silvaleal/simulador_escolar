import sqlite3

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