from collections import OrderedDict
from math import sqrt


class WeightCalculator:

    def __init__(self):
        self._query_results = OrderedDict()

    def calculate_weights(self, doc_list, word_base, query):
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
            self.__sort_results(unordered_results=unordered_results)

        return self._query_results

    def __sort_results(self, unordered_results):
        for key in sorted(unordered_results, reverse=True):
            print(key)
            self._query_results[key] = key
