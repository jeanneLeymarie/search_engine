import pprint
from src.search import Search

if __name__ == '__main__':
    search = Search()
    search.list_salton_coef()
    _result = search.most_relevant_documents()
    pprint.pprint(_result)