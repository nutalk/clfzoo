# -*- coding: utf-8 -*-

import sys
sys.path.append('../..')


import clfzoo.textcnn as clf
from clfzoo.config import ConfigTextCNN
from clfzoo.data_prepare import process_text,data_enhance

class Config(ConfigTextCNN):
    def __init__(self):
        super(Config, self).__init__()

    batch_size = 8

    max_sent_num = 1
    max_sent_len = 60
    max_char_len = 10    

    train_file = '../data/news/TREC.train.txt'
    dev_file = '../data/news/TREC.test.txt'

clf.model(Config())
while True:
    datas = str(input('text:\n'))
    words=process_text(datas)
    enhanced_data=data_enhance(words)
    for words in enhanced_data:
        datas=' '.join(words)
        preds = clf.predict([datas])
        print(preds)
