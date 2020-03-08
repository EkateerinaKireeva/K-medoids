import numpy as np

from Memento import save_to_db, get_close_words
from PlotMedoids import DrawMedoids
np.random.seed(19680801)
from sklearn.manifold import TSNE
from kmedoids import ToCluster

words = [
    'cat',
    'waytruncate',
    'cot',
    "saytruncate",
    "accommodate",
    "accomodate",
    "acommodate",
    "acknowledge",
    "acknowlege",
    "aknowledge",
    "aquit",
    "achieve",
    "acheive",
	"acquaintance",
    "acquaintence",
    "aquaintance",
    "acquire",
    "aquire"
   ]

def Train():
    (distances , clusters) = ToCluster(words)
    save_to_db(clusters, words)
    X_embedded = TSNE(metric="precomputed").fit_transform(distances)
    DrawMedoids(X_embedded,clusters,words)

def Test(word):
    answers = get_close_words(word,1)
    for a in answers:
        print(a.name)

Test("acheive")