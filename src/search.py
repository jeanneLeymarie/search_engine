# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:52:31 2018

@author: leymarie
"""

from src.indexer import Indexer
from src.relevence_calculator import RelevenceCalculator

class Search :
    def __init__(self):
        self._indexer = Indexer()
        self._query = ""        

    def enter_query(self) : 
        self._query = input("Input query : ")
        
    def list_salton(self) : 
        print("The results for your query \"", self._query, "\" : \n")
        _orderedDict = RelevenceCalculator.calculate_salton_coefficient(self, self._indexer.doc_list, self._indexer.index(), self._query)
        print("Coefficient list (ordered) : ")        
        for item in _orderedDict : 
            print(item)
    
#    def most_relevant_documents(self) :
        

    def test_salton(self) :
        _queryTest = "automne"
        _index = Indexer()
        _orderedDict = RelevenceCalculator.calculate_salton_coefficient(self, _index.doc_list, _index.index(), _queryTest)
        for item in _orderedDict : 
            print(item)


if __name__ == '__main__':
    search = Search()
    search.enter_query()
    _list = search.list_salton()