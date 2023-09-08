import re

from ckiptagger import WS, POS, NER
from collections import Counter
import csv
import nltk
from nltk.corpus import stopwords


ws = WS("./data")
pos = POS("./data")

nltk.download('stopwords')
english_function_words = set(stopwords.words('english'))
chinese_poses_dict = {}


def count_words(words):
    word_count = Counter(words)
    word_count.pop(' ', None)
    word_count.pop('\n', None)

    return word_count


def filter_out_chinese(words):
    chinese_words = []
    for word in words:
        word = re.sub(r"[：。，「」’、（）　○？！…˙ㄧ；]", "", word.strip())
        word = word.replace("'", "").replace('"', '')
        if is_chinese_or_digit(word):
            chinese_words.append(word)
    return chinese_words


def filter_out_english(words):
    english_words = []
    for word in words:
        word = word.strip().replace("'", "").replace('"', '')
        word = re.sub(r'[^a-zA-Z0-9]', ' ', word)
        if not word.isdigit():
            english_words.append(word)
    return english_words


def gen_chinese_poses(ws_results):
    global chinese_poses_dict

    pos_results = pos(ws_results)
    words = [item for sublist in ws_results for item in sublist]
    poses = [item for sublist in pos_results for item in sublist]
    # print(poses)

    # for word_list, pos_list in zip(ws_results, pos_results):
    #     for word, tag in zip(word_list, pos_list):
            # print(f"{word} ({tag})")
            # print(f"{word} ({tag}): {classify_ckip_pos_tag(tag)}")
    for i, word in enumerate(words):
        chinese_poses_dict[word] = poses[i]


def is_chinese(word):
    return bool(re.fullmatch(r'[\u4e00-\u9fff]+', word))


def is_chinese_or_digit(word):
    if re.search(r'^[\u4e00-\u9fff0-9]+$', word):
        return not re.fullmatch(r'[0-9]+', word)
    return False


def is_english(word):
    return re.fullmatch(r'[a-zA-Z]+', word)


def is_english_or_digit(word):
    if re.search(r'^[a-zA-Z0-9]+$', word):
        return not re.fullmatch(r'[0-9]+', word)
    return False


chinese_content_tags = ["Na", "Nb", "Nc", "VA", "VD", "VAC", "VH", "VHC"]
chinese_function_tags = ["P", "Cbb", "Nep", "D", "T", "Di", "Dk", "P", "Caa", "Cab", "Cba", "Cbb"]

def get_word_type(word):
    if is_english(word):
        return "F" if word in english_function_words else "C"
    elif is_chinese(word):
        tag = chinese_poses_dict.get(word, "")
        if tag in chinese_content_tags:
            return f"C-{tag}"
        elif tag in chinese_function_tags:
            return f"F-{tag}"
        else:
            return f"X-{tag}"
    return "X"


def part_to_english_and_chinese(filename):
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


def write_to_tsv(word_count, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['Word', 'Type', 'Frequency'])
        for word, count in word_count.items():
            row = [word, get_word_type(word), count]
            writer.writerow(row)
            print(row)


if "__main__" == __name__:
    with open("dataset/article_original.txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 文章原文
    ws_results = ws(lines)
    gen_chinese_poses(ws_results)
    words = [item for sublist in ws_results for item in sublist]
    write_to_tsv(count_words(filter_out_chinese(words)), "output/article_original-1.tsv")

    # 文章譯文
    with open("dataset/article_trans.txt", 'r', encoding='utf-8') as file:
        article = file.read()
    words = re.findall(r'\b\w+\b', article.lower())
    write_to_tsv(count_words(filter_out_english(words)), "output/article_trans-1.tsv")

    # 法庭原文
    article_English, article_Chinese = part_to_english_and_chinese("dataset/court_original.tsv")

    ws_results = ws(article_Chinese.splitlines())
    gen_chinese_poses(ws_results)
    words = [item for sublist in ws_results for item in sublist]
    write_to_tsv(count_words(filter_out_chinese(words)), "output/court_original_Chinese-1.tsv")

    words = re.findall(r'\b\w+\b', article_English.lower())
    write_to_tsv(count_words(filter_out_english(words)), "output/court_original_English-1.tsv")

    # # 法庭譯文
    article_English, article_Chinese = part_to_english_and_chinese("dataset/court_trans.tsv")

    ws_results = ws(article_Chinese.splitlines())
    gen_chinese_poses(ws_results)
    words = [item for sublist in ws_results for item in sublist]
    write_to_tsv(count_words(filter_out_chinese(words)), "output/court_trans_Chinese-1.tsv")

    words = re.findall(r'\b\w+\b', article_English.lower())
    write_to_tsv(count_words(filter_out_english(words)), "output/court_trans_English-1.tsv")
