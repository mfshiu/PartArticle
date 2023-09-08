from collections import Counter
import nltk
from nltk.corpus import stopwords
import re


nltk.download('stopwords')
function_words = set(stopwords.words('english'))


def count_words(article):
    words = re.findall(r'\b\w+\b', article.lower())
    word_count = Counter(words)
    return word_count


if "__main__" == __name__:
    article = """A word frequency counter can be useful if you're doing cross-browser testing. For example, if you have made a web application that accepts user comments, you may want to prevent users from repeating the same words in the comments too many times. You can use this utility to write test cases for catching comments with many repeated words. Also, this program can be useful if you're doing statistical text analysis or optimizing the text for SEO. Additionally, you can use this program to tell which language the given text is written in. Each language has some words appearing more often than others and this distribution of words is unique to each language."""
    word_count = count_words(article)
    for word, count in word_count.items():
        print(f'{word}: {count}')
        

if "1__main__" == __name__:
    word = "Book"
    word = "is"
    is_function_word = word.lower() in function_words
    print(f"is_function_word: {is_function_word}")