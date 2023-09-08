import csv

from article_original import count_Chinese_frequency
from article_trans import count_English_frequency
from court_original import divide_to_English_Chinese


if "__main__" == __name__:
    article_English, article_Chinese = divide_to_English_Chinese("dataset/court_trans.tsv")
    count_English_frequency(article_English, "output/court_trans_English.tsv")
    count_Chinese_frequency(article_Chinese, "output/court_trans_Chinese.tsv")
