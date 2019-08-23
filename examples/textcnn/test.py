# -*- coding: utf-8 -*-

import sys
sys.path.append('../..')

import clfzoo
import clfzoo.textcnn as clf
from clfzoo.config import ConfigTextCNN
from clfzoo.data_prepare import process_text

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

datas = ['今天大盘的走势属于强势整理，主动调整的依然是创业板。其起到了领涨领跌的作用。但无论如何创业板一波新的行情宣告启动，随着大盘两根中阳线的诞生，与之共存的就是新题材，深圳板块，这次题材与指数共振，接下来将会走出第一波，第二波，出现最少一个月的短线投资机会，8月15日是行情启动的第一天，接下来就是好好选股，好好学会买入时机，把握赚钱机会的时候，把握住这次新题材的好机会。主要的操作战场还在创业板，但是主板当中一些由主力控盘资金走强的个股也要坚决在回调过程当中关注。',
         '今日(8月21日)A股三大股指开盘涨跌不一，盘初震荡之后快速拉升，又遭遇“回落—>拉升—>回落”反复震荡，沪指相对表现强势，而创业板指回调明显，不过局部赚钱效应仍存。从盘面上来看，炒地图行情又起风！深圳本地股之后，上海自贸板块开始骚动。截止午间收盘，飞乐音响涨停，电达股份股价一度封涨停，招商轮船、中远海能、张江高科等个股大涨。']
datas = [' '.join(process_text(item)) for item in datas]
print(datas)
labels = ['1028', '1028']
preds, metrics = clf.test(datas, labels)
print(preds)
print(metrics)
