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
    def __init__(self, rows):
        self.rows = rows
        self.header = '车次 出发/到达站 出发/到达时间 历时 商务座 一等座 二等座 软卧 硬卧 软座 硬座 无座'.split()
    def __get_duration(self, row):
        #获取车次运行时间
        if row['lishi'] == '99:59':
            return '列车停运'
        duration = row['lishi'].replace(':', 'h') + 'm'
        if duration.startswith('00'):
            return duration[3:]
        if duration.startswith('0'):
            return duration[1:]
        return duration
    
    @property
    def trains(self):
        for Row in self.rows:
            row = Row['queryLeftNewDTO']
            train = [
                # 车次
                row['station_train_code'],
                # 出发，终点站
                ' '.join([row['from_station_name'], row['to_station_name']]),
                # 出发，到达时间
                ' '.join([row['start_time'], row['arrive_time']]),
                # 历时
                self.__get_duration(row),
                # 商务座
                row['swz_num'],
                # 一等座
                row['zy_num'],
                # 二等座
                row['ze_num'],
                # 软卧
                row['rw_num'],
                # 硬卧
                row['yw_num'],
                # 软座
                row['rz_num'],
                # 硬座
                row['yz_num'],
                # 无座
                row['wz_num']
            ]
            if train[3] == '列车停运':
                train[2] = '--- ---'
            yield train
    
    def prettyprint(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print pt
def cli():
    #cmd interface
    arguments = docopt(__doc__)
    from_station = stations[arguments['<from>'].lower()]
    to_station = stations[arguments['<to>'].lower()]
    date = arguments['<date>']
    date = date.split('-')
    date = '%04d-%02d-%02d' % (int(date[0]), int(date[1]), int(date[2]))
    print date
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date, from_station, to_station
    )
    r = requests.get(url,verify=False)
    #lishi                  历时
    #arrive_time            到达时间
    #start_time             发车时间
    #station_train_code     车次
    #rw_num                 软卧
    #
    #
    #

    if 'data' not in r.json():
        print '未找到相应信息！'
        return
    arr = r.json()['data']
    #pprint(arr, indent=2)

    #for item in arr:
    #    print(item['queryLeftNewDTO']['station_train_code'] + ' ' + item['queryLeftNewDTO']['start_time'] + ' ' + item['queryLeftNewDTO']['arrive_time'] \
    #    + item['queryLeftNewDTO']['lishi'])
    trains = TrainCollection(arr)
    trains.prettyprint()
if __name__ == '__main__' :
    cli()