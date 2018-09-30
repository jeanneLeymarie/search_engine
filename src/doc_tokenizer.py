# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 13:44:26 2018

@author: leymarie
"""
import re


class DocTokenizer:

    def tokenize(self, path):
        # type: (str) -> List[str]
        """
        Opens a file contained at a specific path and returns the test as a list of tokens
        :param path: str
        :return: List[str]
        """
        doc = open(path, 'r', encoding='ISO-8859-1')
        doc_string = doc.read()
        doc_clean = self.__supp_punctuation_mark(doc_string)
        word_list = re.findall(r"[\w']+", doc_clean)
        return word_list

    def __supp_punctuation_mark(self, string_with_punctionations):
        # type: (str) -> List[str]
        """
        Substitutes puctionation marks in a given string and returns it
        :param string_with_punctionations: str
        :return: str
        """
        new_str = re.sub('(\.|\?|\!|\,|\;)', ' ', string_with_punctionations)
        return new_str

    def test_supp_punctuation_mark(self, str):
        doc_test = open(str, "r", encoding='ISO-8859-1')
        str_clean = self.__supp_punctuation_mark(doc_test.read())

        has_punctuation_mark = re.findall('\?|\!|\.|\,|\;', str_clean)
        if not has_punctuation_mark:
            print('No Punctuation Mark ------ Test OK \n')
        else:
            print('Still Punctuation ------- Test KO \n')

    def test_tokenize(self, path):
        word_list = self.tokenize(path)
        print(word_list)

# def test() :
#     print('\n')
#     x = DocTokenizer()
#     test_file = './Corpus_2018/Automne_GA.txt'
#     x.test_suppPunctuationMark(test_file)
#     x.test_tokenize(test_file)
#
# test()
