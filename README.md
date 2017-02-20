# python-train-ticket-check-script
python实现火车票查询  

#python依赖库
```
request  
prettytable  
docopt  
pprint  
```

```
$sudo pip3 install requests prettytable docopt pprint
```

#使用
```
python tickets.py 出发城市拼音 到达城市拼音 时间 1>out.txt 2>/dev/null
```
#示例
```
python tickets.py jinan beijing 2016-10-15 1>out.txt 2>/dev/null
```

就可以在out.txt里查看列车信息了~  


