import dash
from dash import dcc, html
import plotly.express as px
import sqlite3
import pandas as pd


conn = sqlite3.connect('application.db')


def top_spenders():
    query = '''SELECT u.name, SUM(t.amount) AS total_spent
               FROM users u
               JOIN transactions t ON u.user_id = t.user_id
               GROUP BY u.name
               ORDER BY total_spent DESC
               LIMIT 3'''
    return pd.read_sql_query(query, conn)


top_users = top_spenders()


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('User Transaction Dashboard'),

    dcc.Graph(
        id='top-spenders-bar-chart',
        figure=px.bar(top_users, x='name', y='total_spent', title='Top 3 Users by Amount Spent')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
