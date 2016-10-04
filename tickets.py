#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# coding="utf-8"

""" Train tickets query via command-line

Usage:
    tickets [-gdtkz] <from> <to> <date>
    
Opthons:
    -h, --help  显示帮助
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达
Example tickets beijing shanghai 2016-10-1
"""
from docopt import docopt
from pprint import pprint
from station_map import stations
from prettytable import PrettyTable
import requests

class TrainCollection(object):
    #显示车次、出发/到达站、出发/到达时间、历时、一等座、二等座、软卧、硬卧、硬座
    header = 'train station time duration first second softsleep headsleep hardsit'.split()
    def __init__(self, rows):
        self.rows = rows
    def __get_duration(self, row):
        #获取车次运行时间
        duration = row['lishi'].replace(':', 'h') + 'm'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration
    
    

def cli():
    #cmd interface
    arguments = docopt(__doc__)
    from_station = stations[arguments['<from>']]
    to_station = stations[arguments['<to>']]
    date = arguments['<date>']
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date, from_station, to_station
    )
    r = requests.get(url,verify=False)
    pprint(r.json(), indent=2)
if __name__ == '__main__' :
    cli()