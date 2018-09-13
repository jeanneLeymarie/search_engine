# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 13:44:26 2018

@author: leymarie
"""
import re

class DocTokenizer :
    
    def tokenize(self, path) :
        doc = open(path, 'r', encoding = 'ISO-8859-1')
        doc_string = doc.read()
        doc_clean = self.suppPunctuationMark(doc_string)
        word_list = re.findall(r"[\w']+", doc_clean)
        return word_list
      
      
    def suppPunctuationMark(self, str) : 
        newstr = re.sub('(\.|\?|\!|\,|\;)', ' ', str)
        return newstr
        
        
    def test_suppPunctuationMark(self, str) :         
        doc_test = open(str, "r", encoding = 'ISO-8859-1')
        str_clean = self.suppPunctuationMark(doc_test.read())

        hasPunctuationMark = re.findall('\?|\!|\.|\,|\;', str_clean)
        if not hasPunctuationMark :
            print('No Punctuation Mark ------ Test OK \n')
        else : 
            print('Still Punctuation ------- Test KO \n')


    def test_tokenize(self,path) :
        word_list = self.tokenize(path)
        print(word_list)
        
def test() : 
    print('\n')
    x = DocTokenizer()
    test_file = './Corpus_2018/Automne_GA.txt'
    x.test_suppPunctuationMark(test_file)
    x.test_tokenize(test_file)
    
test()