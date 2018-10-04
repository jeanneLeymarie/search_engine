# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:52:31 2018

@author: leymarie
"""

from src.indexer import Indexer
from src.weight_calculator import WeightCalculator

class Search :
    def __init__(self):
        self._indexer = Indexer()
        self._doc_list = {}
        self._query = ""        

    def __enter_query(self) : 
        _query = input("Request : ")
        print(_query)
        
    def __list_salton(self) : 
        _orderedDict = WeightCalculator.calculate_weights(self._doc_list, self.indexer.word_base, self._query)
        WeightCalculator.__sort_results(_orderedDict)
    
    #def __most_relevant_docs(self) :
        #_doc_list = self._indexer.doc_list()

    def test_salton(self) :
        _queryTest = "automne";
        _index = Indexer();
        _orderedDict = WeightCalculator.calculate_weights(self, _index.doc_list, _index._word_base, _queryTest)
        WeightCalculator.__sort_results(_orderedDict)



if __name__ == '__main__':
    search = Search()
    search.test_salton()