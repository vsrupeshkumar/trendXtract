import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import nltk
from nltk.corpus import stopwords
import re

# Ensure stopwords are available
nltk.download('stopwords')

def preprocess(text):
    # Lowercase and remove non-alphabet characters
    text = re.sub(r'\W+', ' ', str(text).lower())
    tokens = text.split()
    # Remove English stopwords
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    return ' '.join(tokens)

def load_and_analyze(csv_path):
    # Load CSV with academic papers (must have 'title' and 'abstract' columns)
    df = pd.read_csv(csv_path)

    # Combine and preprocess the text
    df['text'] = (df['title'] + ' ' + df['abstract']).fillna('').apply(preprocess)

    # Convert to bag-of-words
    vectorizer = CountVectorizer(max_df=0.9, min_df=10, stop_words='english')
    X = vectorizer.fit_transform(df['text'])

    # Apply topic modeling with LDA
    lda = LatentDirichletAllocation(n_components=5, random_state=42)
    lda.fit(X)

    # Extract top keywords from each topic
    topics = {}
    for idx, topic in enumerate(lda.components_):
        keywords = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]]
        topics[f"Topic {idx+1}"] = keywords[::-1]  # Top 10 keywords

    return topics
