import pprint

from src.indexer import Indexer
from src.weight_calculator import WeightCalculator

if __name__ == '__main__':

    indexer = Indexer()
    doc_list = indexer.doc_list
    word_base = indexer.index()

    query = 'Les vaches souviennent'

    pprint.pprint(WeightCalculator().calculate_weights(doc_list=doc_list, word_base=word_base, query=query))

