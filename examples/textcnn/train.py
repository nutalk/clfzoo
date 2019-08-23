# -*- coding: utf-8 -*-

import sys
sys.path.append('../..')

import clfzoo
import clfzoo.textcnn as clf
from clfzoo.config import ConfigTextCNN

class Config(ConfigTextCNN):
    def __init__(self):
        super(Config, self).__init__()

    batch_size = 16
    epochs = 20

    max_sent_num = 1
    max_sent_len = 100
    max_char_len = 10

    train_file = '../data/news/TREC.train.txt'
    dev_file = '../data/news/TREC.test.txt'


clf.model(Config(), training=True)
clf.train()
