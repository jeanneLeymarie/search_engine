import pprint
from collections import OrderedDict
from math import sqrt


class WeightCalculator:

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
        pprint.pprint(unordered_results)
        return OrderedDict(sorted(unordered_results.items(), reverse=True))