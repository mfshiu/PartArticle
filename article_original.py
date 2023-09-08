from collections import Counter
import csv
import jieba
import re
import string


def is_chinese(word):
    # Check if word is a digital number
    if re.search(r'\d+', word):
        return False
    
    # Check if word contains common punctuation marks
    if re.search(r'[.,!?;\'"(){}[\]-]', word):
        return False
    
    # Check if word contains specific Chinese punctuation
    if re.search(r'[：。，「」’ 、（）　○？！…˙ㄧ；]', word):
        return False
    
    # Check if word contains English letters
    if re.search(r'[a-zA-Z]', word):
        return False
    
    return True


def count_chinese_words(article):
    words = jieba.cut(article)
    word_count = Counter(words)
    word_count.pop(' ', None)
    word_count.pop('\n', None)
    return word_count


def replace_punctuation_and_english_letters(article):
    article = re.sub(r'[：。，「」’ 、（）　○？！]', ' ', article)

    pattern = f"[{string.ascii_letters}{string.punctuation}{string.digits}]"
    return re.sub(pattern, ' ', article)


def write_to_tsv(word_count, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['Word', 'Frequency'])
        for word, count in word_count.items():
            row = [word, count]
            writer.writerow(row)
            print(row)


def count_Chinese_frequency(article, output_path):
    article = replace_punctuation_and_english_letters(article)
    word_count = count_chinese_words(article)
    write_to_tsv(word_count, output_path)


if "__main__" == __name__:
    with open("dataset/article_original.txt", 'r', encoding='utf-8') as file:
        article = file.read()
    count_Chinese_frequency(article, "output/article_original.tsv")
    # article = replace_punctuation_and_english_letters(article)
    # word_count = count_chinese_words(article)
    # write_to_tsv(word_count, "output/article_original.tsv")
