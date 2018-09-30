# -*- coding: utf-8 -*-
"""
@author Julian EASTERLY
"""
import math
import os
from pprint import pprint
from src.doc_tokenizer import DocTokenizer

class Indexer:
    """
    Takes a list of documents from a given location and indexes them
    """

    def __init__(self, doc_location=''):
        """
        :param doc_location: str. location of the documents that will be indexed
        """
        if doc_location:
            self._doc_location = doc_location
        else:
            self._doc_location = os.path.join(os.path.dirname(__file__), '..', 'docs')

        self._word_base = {}
        self._nb_files = 0
        self._tokenier = DocTokenizer()
        self._doc_list = os.listdir(self._doc_location)

    def index(self):
        """
        Indexes files from the doc_location and returns a dictionary of words with their frequency
        and the docs that contain the word
        ex. { 'hi' : {'frequency': 1, 'docs': {'hey buddy.txt': 2.302}}
        :return: Dict[str, IndexedWord]
        """
        for filename in self._doc_list:
            self._nb_files += 1
            self.__create_word_set(filename)
        self.__add_index_weights()

        return self._word_base

    @property
    def doc_list(self):
        return self._doc_list

    def __create_word_set(self, filename):
        """
        :param filename: str
        :return: None
        """
        abs_filename = os.path.join(self._doc_location, filename)
        tmp = self._tokenier.tokenize(path=abs_filename)
        self.__calculate_frequencies(filename, tmp)

    def __calculate_frequencies(self, filename, tmp):
        while tmp:
            word = tmp.pop()
            if word not in self._word_base:
                self._word_base[word] = IndexedWord(word, frequency=1, docs={filename: 1})
            else:
                self._word_base.get(word).augment_doc_frequency(filename)

    def __add_index_weights(self):
        for key, word in self._word_base.items():
            word_frequency = word.frequency
            for doc, word_frequency_in_doc in word.docs.items():
                word.docs[doc] = self.__calculate_weight(self._nb_files, word_frequency, word_frequency_in_doc)

    def __calculate_weight(self, number_of_docs, word_frequency, word_frequency_in_doc):
        """
        :param number_of_docs: int
        :param word_frequency: int
        :param word_frequency_in_doc: int
        :return: float
        """
        return word_frequency_in_doc * math.log(number_of_docs / word_frequency)


class IndexedWord:

    def __init__(self, word, frequency=1, docs=None):
        if docs is None:
            docs = {}

        self.word = word
        self.frequency = frequency
        self.docs = docs

    def augment_frequency(self):
        self.frequency += 1

    def add_new_doc(self, doc):
        self.docs[doc] = 1

    def augment_doc_frequency(self, doc):
        if doc not in self.docs:
            self.add_new_doc(doc)
            self.augment_frequency()
        else:
            self.docs[doc] += 1

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str({'frequency': self.frequency, 'docs': self.docs})


#pprint(Indexer().index())
