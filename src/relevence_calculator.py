# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 13:44:26 2018

@author: easterly1
"""
from collections import OrderedDict
from math import sqrt


class RelevenceCalculator:

    def calculate_salton_coefficient(self, doc_list, word_base, query):
        # type: (str, Dict[str, Dict[str, Union[str, float]]]) -> OrderedDict[float, str]
        """
        Calculates the Salton cosine coef
        :param doc_list:
        :param word_base:
        :param query:
        :return: OrderedDict[float, str]
        """
        query_size = len(query.split(' '))
        unordered_results = {}

        for doc in doc_list:
            denominator = 0
            numerator = 0
            for word, word_information in word_base.items():
                if word_information.docs.get(doc):
                    denominator += word_information.docs.get(doc) * word_information.docs.get(doc)
                    if word in query:
                        numerator += word_information.docs.get(doc)

            denominator *= query_size
            index = numerator / sqrt(denominator)
            unordered_results[index] = doc

        return OrderedDict(sorted(unordered_results.items(), reverse=True))
