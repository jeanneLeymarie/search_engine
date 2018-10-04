import pprint

from src.indexer import Indexer
from src.relevence_calculator import RelevenceCalculator

if __name__ == '__main__':

    indexer = Indexer()
    doc_list = indexer.doc_list
    word_base = indexer.index()

    query = 'Les vaches souviennent'

    pprint.pprint(RelevenceCalculator().calculate_salton_coefficient(doc_list=doc_list, word_base=word_base, query=query))

