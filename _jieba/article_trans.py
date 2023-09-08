from collections import Counter
import csv
import nltk
from nltk.corpus import stopwords
import re


nltk.download('stopwords')
function_words = set(stopwords.words('english'))


def count_words(article):
    words = re.findall(r'\b\w+\b', article.lower())
    word_count = Counter(words)
    word_count.pop(' ', None)
    word_count.pop('\n', None)
    return word_count


def insert_space_between_languages(article):
    article = re.sub(r'([a-zA-Z])([\u4e00-\u9fff])', r'\1 \2', article)
    article = re.sub(r'([\u4e00-\u9fff])([a-zA-Z])', r'\1 \2', article)    
    return article


def is_English(word):
    return re.search(r'[a-zA-Z]', word)


def write_to_tsv(word_count, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['Word', 'Type', 'Frequency'])
        for word, count in word_count.items():
            if is_English(word):
                word_type = "F" if word in function_words else "C"
                row = [word, word_type, count]
                writer.writerow(row)
                print(f'{row}')


def count_English_frequency(article, output_path):
    article = insert_space_between_languages(article)
    word_count = count_words(article)
    write_to_tsv(word_count, output_path)


if "__main__" == __name__:
    with open("dataset/article_trans.txt", 'r', encoding='utf-8') as file:
        article = file.read()
    count_English_frequency(article, "output/article_trans.tsv")
    # article = insert_space_between_languages(article)
    # word_count = count_words(article)
    # write_to_tsv(word_count, "output/article_trans.tsv")
