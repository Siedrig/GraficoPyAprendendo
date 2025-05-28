# The following code requires pandas and matplotlib. Uncomment after installing them.
import pandas as pd
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import dash
from dash import dcc, html
import plotly.graph_objs as go

# Read the Excel file
df = pd.read_excel('RespostasFormularioDesigualdade.xlsx')

start_col = 5
columns_to_analyze = df.columns[start_col:]
keywords = ['método', 'apostila', 'recursos', 'infraestrutura', 'desafio', 'aluno', 'professor', 'diferença', 'ensino', 'material', 'familia', 'apoio']
type_col = 'A escola que você leciona atualmente é pública ou particular?'

groups = {}
for school_type in ['pública', 'particular']:
    groups[school_type] = df[df[type_col].str.strip().str.lower() == school_type]

results = {}
for school_type, group_df in groups.items():
    counts = Counter()
    for col in columns_to_analyze:
        for reply in group_df[col].dropna().astype(str):
            for kw in keywords:
                if kw.lower() in reply.lower():
                    counts[kw] += 1
    results[school_type] = counts

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Frequência de Palavras-chave por Tipo de Escola"),
    dcc.Graph(
        id='keyword-bar',
        figure={
            'data': [
                go.Bar(
                    x=list(results['pública'].keys()),
                    y=list(results['pública'].values()),
                    name='Pública'
                ),
                go.Bar(
                    x=list(results['particular'].keys()),
                    y=list(results['particular'].values()),
                    name='Particular'
                )
            ],
            'layout': go.Layout(
                barmode='group',
                xaxis={'title': 'Palavra-chave'},
                yaxis={'title': 'Frequência'}
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)

