import re
import jieba
from os.path import abspath, dirname, join


def get_stop_words():
    stop_words = set()
    current_path = abspath(dirname(__file__))
    with open(join(current_path, 'dict/stop_words.txt'), 'r') as f:
        for line in f:
            stop_words.add(line.strip('\n'))
    return stop_words


def text_clean(text):
    date_pattern = re.compile(r'\d{0,4}年{0,1}\d{1,2}月\d{0,2}日{0,1}')
    num_pattern = re.compile(r'\d+')
    eng_pattern = re.compile(r'[a-zA-Z]+')
    text = re.sub(date_pattern, 'DATE', text)
    text = re.sub(num_pattern, 'NUM', text)
    text = re.sub(eng_pattern, 'ENG', text)
    return text


def process_text(text):
    """
    对文本进行清理，包括：1，替换英文字符，数字，日期。2，分词，去停用词。。
    :param text: 需要处理的文本
    :return: 词组成的列表
    """
    stop_words = get_stop_words()
    text = text_clean(text)
    words = jieba.cut(text)
    useful_words = [word for word in words if word not in stop_words]
    return useful_words
