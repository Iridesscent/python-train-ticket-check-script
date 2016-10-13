# python-train-ticket-check-script
python实现火车票查询  
This is a simple python script to check realtime train ticket information

#python依赖库 / library dependency
```
request  
prettytable  
docopt  
pprint  
```

```
$sudo pip3 install requests prettytable docopt pprint
```

#使用 / API
```
python tickets.py 出发城市拼音 到达城市拼音 时间 1>out.txt 2>/dev/null
```
#示例  / example
```
python tickets.py jinan beijing 2016-10-15 1>out.txt 2>/dev/null
```

就可以在out.txt里查看列车信息了~  

The information will be saved as out.txt in the same location of your python script :)