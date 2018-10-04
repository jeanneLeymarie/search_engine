# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:52:31 2018

@author: leymarie
"""
import pprint
from src.indexer import Indexer
from src.relevence_calculator import RelevenceCalculator

class Search :
    def __init__(self):
        self._indexer = Indexer()
        self._query = ""    
        self._orderedDict = {}

    def list_salton_coef(self) : 
        """
        Calculates the Salton cosine coef of all the documents according to the query entered by the user
        Displays the list
        """
        self._query = input("Input query : ")
        print("The results for your query \"", self._query, "\" : \n")
        self._orderedDict = RelevenceCalculator.calculate_salton_coefficient(self, self._indexer.doc_list, self._indexer.index(), self._query)
            
    
    def most_relevant_documents(self) :
        """
        Based on the Salton coefficient, selects the k most relevant documents
        k depends on the value of the Salton coefficient, a document is relevant when the Salton coefficient is superior to 0.05 
        (value arbitrarily chosen)
        :return: a list containing the tiltes of the documents ordered by relevence
        """        
        _result = {}
        i = 0
        for doc in self._orderedDict :
            if doc >= 0.05:
                _result[i] = self._orderedDict.get(doc)
                i += 1
        return _result
        

    def test_salton(self) :
        _queryTest = "automne"
        _index = Indexer()
        _orderedDict = RelevenceCalculator.calculate_salton_coefficient(self, _index.doc_list, _index.index(), _queryTest)
        pprint.pprint(_orderedDict.values())


if __name__ == '__main__':
    search = Search()
    search.list_salton_coef()
    _result = search.most_relevant_documents()
    pprint.pprint(_result)