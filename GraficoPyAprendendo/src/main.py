import pandas as pd
import plotly.graph_objects as go
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Read the Excel file
df = pd.read_excel('RespostasFormularioDesigualdade.xlsx')

# Start from the target column (index 5)
start_col = 5
columns_to_analyze = df.columns[start_col:]

# Define keywords to search for (excluding 'pública' and 'particular')
keywords = ['método', 'apostila', 'recursos', 'infraestrutura', 'desafio', 'aluno', 'professor', 'diferença', 'ensino', 'material', 'familia', 'apoio']

# Column to split by school type
type_col = 'A escola que você leciona atualmente é pública ou particular?'

# Prepare sub-dataframes for each school type
groups = {}
for school_type in ['pública', 'particular']:
    groups[school_type] = df[df[type_col].str.strip().str.lower() == school_type]

# Count keyword occurrences for each group
results = {}
for school_type, group_df in groups.items():
    counts = Counter()
    for col in columns_to_analyze:
        for reply in group_df[col].dropna().astype(str):
            for kw in keywords:
                if kw.lower() in reply.lower():
                    counts[kw] += 1
    results[school_type] = counts

# Sentiment analysis for each group using Vader
analyzer = SentimentIntensityAnalyzer()
sentiment_results = {}
for school_type, group_df in groups.items():
    sentiments = []
    for col in columns_to_analyze:
        for reply in group_df[col].dropna().astype(str):
            score = analyzer.polarity_scores(reply)['compound']
            sentiments.append(score)
    if sentiments:
        avg_sentiment = sum(sentiments) / len(sentiments)
    else:
        avg_sentiment = 0
    sentiment_results[school_type] = avg_sentiment

# Create an interactive dashboard using Plotly
fig = go.Figure()

# Add bar traces for keyword frequencies
for school_type in ['pública', 'particular']:
    counts = results[school_type]
    fig.add_trace(go.Bar(
        x=list(counts.keys()),
        y=list(counts.values()),
        name=school_type.capitalize(),
        text=list(counts.values()),
        textposition='auto'
    ))

# Update layout
fig.update_layout(
    title='Frequência de Palavras-chave por Tipo de Escola',
    xaxis_title='Palavra-chave',
    yaxis_title='Frequência',
    barmode='group'
)

# Show average sentiment polarity
for school_type, avg_sentiment in sentiment_results.items():
    print(f"{school_type.capitalize()}: {avg_sentiment:.2f}")

# Show the dashboard
fig.show()