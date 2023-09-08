import csv

from article_original import count_Chinese_frequency
from article_trans import count_English_frequency


def divide_to_English_Chinese(filename):
    article_English = ""
    article_Chinese = ""
    
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if "zh" in row[0]:
                article_Chinese += f"{row[1]}\n" 
            else:
                article_English += f"{row[1]}\n" 
            
    return article_English, article_Chinese


if "__main__" == __name__:
    article_English, article_Chinese = divide_to_English_Chinese("dataset/court_original.tsv")
    count_English_frequency(article_English, "output/court_original_English.tsv")
    count_Chinese_frequency(article_Chinese, "output/court_original_Chinese.tsv")
