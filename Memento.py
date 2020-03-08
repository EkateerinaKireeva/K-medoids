import numpy as np
from peewee import *

from Lowenstein import distance

db = PostgresqlDatabase(database="Test", user="postgres", password="123", host="localhost");


class Word(Model):
    name = CharField()
    cluster = IntegerField()
    isMedoid = BooleanField()

    class Meta:
        database = db


def save_to_db(clusters, words):
    words = np.array(words)
    db.connect()
    Word.delete()
    Word.create_table()

    count = 0
    for cl in clusters:
        count += 1
        db_model_clusters = []

        for w in words[cl.elements]:
            db_model_clusters.append({'name': w, 'cluster': count, 'isMedoid': False})

        db_model_clusters.append({'name': words[cl.medoid], 'cluster': count, 'isMedoid': True})

        Word.insert_many(db_model_clusters).execute()


def get_all_medoids():
    query = (
        Word.select()
            .where(Word.isMedoid))

    return query


def get_all_cluster_items(cluster):
    query = (
        Word.select()
            .where(Word.cluster == cluster))

    return query


def get_cluster(word):
    return min(get_all_medoids(), key=lambda x: distance(x.name, word))


def get_close_words(word, dis):
    words = get_all_cluster_items(get_cluster(word).cluster)
    return list(filter(lambda x: distance(x.name, word) == dis, words))
