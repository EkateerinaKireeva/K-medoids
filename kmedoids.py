import numpy as np

from Helper import delete_row_in_list, get_min_and_max_index, createDistanceMetrix, meadiana

class Cluster:
    def __init__(self, elements, centerIndex):
        self.medoid = elements[centerIndex]
        del elements[centerIndex]
        self.elements = np.array(elements)


def assign_labels(S):
    sum = 0
    labels = np.zeros(len(S[0]), dtype=float)
    for ind in range(0, len(S[0])):
        labels[ind] = np.argmin(S[:, ind])
        sum += S[int(labels[ind]),ind]
    return (sum, labels)


def update_medoids(distances, initial_medoid_changing, initial_medoid_fixed):
    inputArray = np.array([distances[initial_medoid_changing, :],  distances[initial_medoid_fixed, :]])
    (avsum , avlabels) = assign_labels( inputArray)

    for index, value in enumerate(distances):
        if avlabels[index] == 1 or index == initial_medoid_changing:
            continue

        inputArray = np.array([distances[index, :],  distances[initial_medoid_fixed, :]])
        (sum, labels) = assign_labels(inputArray)

        if sum < avsum:
            avlabels = labels
            avsum = sum

    return (avsum , avlabels)


def ToCluster(words):
    distances = createDistanceMetrix(words)
    print(distances)
    working_distances = distances.tolist()
    indexes = np.arange(0, len(distances), 1).tolist()
    Clusters = []

    while meadiana(working_distances) > 2 and len(working_distances) != 1:
        (firstItemNumber, lastItemNumber) = get_min_and_max_index(working_distances)
        (sum, labels) = update_medoids(np.asarray(working_distances), firstItemNumber, lastItemNumber)

        elements = []
        count = 0
        # it's crunch
        # SHOULD BE REWRITING
        for ind, value in enumerate(labels):
            if value != 0:
                index = ind - count
                elements.append(indexes[index])
                del indexes[index]
                del working_distances[index]
                delete_row_in_list(working_distances, index)
                count += 1

        cluster_distance_columns = distances[elements]
        Clusters.append(Cluster(elements, calculate_medoid(cluster_distance_columns[:, elements])))

    Clusters.append(Cluster(indexes,calculate_medoid(working_distances)))
    return (distances, Clusters)


def calculate_medoid(distances):
    minIndex = 0
    minValue = 0

    for i, d in enumerate(distances):
        if minIndex == i:
            minValue  = sum(d)
            continue

        s = sum(d)
        if s < minValue:
            minValue = s
            minIndex = i

    return  minIndex