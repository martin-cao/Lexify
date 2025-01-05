# This file includes data from the project "DictionaryData" (https://github.com/LinXueyuanStdio/DictionaryData)
# licensed under the Apache-2.0 License.

# Please clone the repository mentioned above into Lexify/dict before running this file.
# The data from "DictionaryData" is not included in this repo.

import pandas as pd

book = pd.read_csv('DictionaryData/book.csv', sep=">")
word = pd.read_csv('DictionaryData/word.csv', sep=">")
relation_book_word = pd.read_csv('DictionaryData/relation_book_word.csv', sep=">")
word_translation = pd.read_csv('DictionaryData/word_translation.csv', sep=',')


