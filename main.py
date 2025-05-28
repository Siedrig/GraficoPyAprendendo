# The following code requires pandas and matplotlib. Uncomment after installing them.
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob
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

# Print average sentiment polarity by school type
print('Average sentiment polarity by school type:')
for school_type, avg_sentiment in sentiment_results.items():
    print(f"{school_type.capitalize()}: {avg_sentiment:.2f}")

# Plot the keyword frequencies for each group
fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)
for idx, school_type in enumerate(['pública', 'particular']):
    ax = axes[idx]
    counts = results[school_type]
    bars = ax.bar(counts.keys(), counts.values())
    ax.set_title(f'Frequência de Palavras-chave ({school_type.capitalize()})')
    ax.set_xlabel('Palavra-chave')
    ax.set_ylabel('Frequência')
    ax.set_xticks(range(len(counts)))
    ax.set_xticklabels(list(counts.keys()), rotation=45)
    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
plt.tight_layout()
plt.show()

