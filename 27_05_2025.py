import numpy as np
from collections import Counter
import math

def calculate_bm25_scores(corpus, query, k1=1.5, b=0.75):
    N = len(corpus)
    avgdl = sum(len(doc) for doc in corpus) / N

    # Correct IDF formula
    idf = {}
    for term in query:
        df = sum(1 for doc in corpus if term in doc)
        idf[term] = math.log((N + 1) / (df + 1))  # Standard BM25 IDF

    scores = []
    for doc in corpus:
        doc_len = len(doc)
        term_freq = Counter(doc)
        score = 0.0

        for term in query:
            if term in term_freq:
                f = term_freq[term]
                numerator = f * (k1 + 1)
                denominator = f + k1 * (1 - b + b * doc_len / avgdl)
                score += idf[term] * (numerator / denominator)

        scores.append(score)

    return np.round(scores, 3)  # Match expected format

if __name__ == "__main__":
    corpus = [['the', 'cat', 'sat'], ['the', 'dog', 'ran'], ['the', 'bird', 'flew']]
    query = ['the', 'cat']
    print("calling BM25 function")
    print(calculate_bm25_scores(corpus, query))
