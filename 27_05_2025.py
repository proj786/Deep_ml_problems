#https://www.deep-ml.com/problems/90
'''BM25 Ranking

Implement the BM25 ranking function to calculate document scores for a query in an information retrieval context. BM25 is an advanced variation of TF-IDF that incorporates term frequency saturation, document length normalization, and a configurable penalty for document length effects.

Example:
Input:
corpus = [['the', 'cat', 'sat'], ['the', 'dog', 'ran'], ['the', 'bird', 'flew']], query = ['the', 'cat']
Output:
[0.693, 0., 0. ]
Reasoning:
BM25 calculates scores for each document in the corpus by evaluating how well the query terms match each document while considering term frequency saturation and document length normalization.
'''

import numpy as np 
from collections import Counter