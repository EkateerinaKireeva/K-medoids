import numpy as np

from Lowenstein import distance

def delete_row_in_list(a, index_row):
    for row in a:
        del row[index_row]


def get_min_and_max_index(a):
    sum_array = [np.sum(l) for l in a]
    return (np.argmin(sum_array), np.argmax(sum_array))


def createDistanceMetrix(words) :
  max = 1 #<--  will be use to normilize
  distances = np.zeros((len(words), len(words)))

  for i in range(0, len(words)):
    for j in range(i +1, len(words)):
      d = distance(words[i].lower(), words[j].lower())
      if max < d:
        max = d
      distances[i,j] = d
      distances[j,i] = d

  return distances


def meadiana(a):
    sum = 0
    count = 1
    for i in range(len(a)):
        for j in range(len((a[i]))):
            if i != j:
                sum += a[i][j]
                count+=1

    return  sum/count