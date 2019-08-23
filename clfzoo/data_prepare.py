import random
import re
from os.path import abspath, dirname, join

import jieba


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
    text = re.sub(r'DATE', '1月1日', text)
    text = re.sub(r'POSMONEY', '100', text)
    text = re.sub(eng_pattern, 'ENG', text)
    text = re.sub(date_pattern, 'DATE', text)
    text = re.sub(num_pattern, 'NUM', text)

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


def data_enhance(words, times=3):
    """
    对词进行随机采样，实现单词乱序、丢弃部分单词。
    :param words: list
    :param times: 采样次数
    :return: list of list
    """
    assert isinstance(words, list), 'expect a list but get:\n {}'.format(words)
    output = []
    for i in range(times):
        try:
            sample = random.sample(words, min(100, len(words)))
        except Exception as err:
            print(words)
            print(err)
            return words
        output.append(sample)
    return output


if __name__ == '__main__':
    text = text_clean('DATE HKDE, 好的。POSMONEY, 100元')
    print(text)
