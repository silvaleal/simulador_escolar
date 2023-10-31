import pandas as pd # pip install pandas
import plotly.express as px # pip install plotly
from dash import Dash, html, dcc # pip install dash
import sqlite3 # Note as importações do main.py

# https://dash.plotly.com/

# LEIA: 
# -> O "as" da importação serve para criar apelido para uma biblioteca. então não iremos usar "pandas" no código, e sim "pd".
# -> A biblioteca "pandas" é algo fundamental para a analise de dados.
# -> Existe +1 biblioteca de criação de gráfico, porém escolhi a plotly afinal ela cria gráficos com interações.
# -> A biblioteca "dash" literalmente cria um site para o dashboard. (Usando o Flask)

# Mão na mass... Ops, dedos no teclado!!!
 
# criando o site/dashboard
app = Dash(__name__) # Fundamental para a criação do dashboard. (Basicamente isso que cria o dashboard).

# Inserindo os dados
conexao_sql = sqlite3.connect('database.db')
query = 'SELECT instrutor_nome, instrutor_idade, instrutor_salario FROM instrutores'
df_professores = pd.read_sql(query, conexao_sql)

# Criando o gráfico
# Obs.: Irei chamar o gráfico de figura.
figura_professores = px.bar(df_professores, x="instrutor_nome", y="instrutor_idade")

# Inserindo os gráficos na página HTML
app.layout = html.Div(children=[
    html.H1(children='SIMULADOR ESCOLAR | AUTOBOTS'),

    html.Div(children='Graças a este dashboard, é possível fazer analises mais avançadas de força simples.'),

    dcc.Graph(
        id='nossos-professores',
        figure=figura_professores
    )
])

# Ligando o site/dashboard
if __name__ == '__main__':
    app.run(debug=True)