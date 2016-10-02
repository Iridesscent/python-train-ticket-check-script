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

import requests

from station_map import stations
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
    print(r.json()['start_train_date'])
if __name__ == '__main__' :
    cli()