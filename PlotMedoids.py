import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def DrawMedoids(X_embedded, clusters, words):
    matplotlib.use('WebAgg')

    fig, ax = plt.subplots()

    count = 0
    wordsasArray = np.array(words)
    for cluster in clusters:
        ax.scatter(X_embedded[cluster.elements, 0],X_embedded[cluster.elements, 1], label=count)

        print(wordsasArray[cluster.elements])
        count+=1

    for i, txt in enumerate(words[0:]):
         plt.text(X_embedded[i, 0], X_embedded[i, 1], txt)

    ax.legend()
    ax.grid(True)

    plt.show()
