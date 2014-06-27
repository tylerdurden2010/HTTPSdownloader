#!/usr/bin/env python

import os
import datetime,time

def TimeOutput(date,daycount):
    #generate 109738278 stuff
    timestamp = time.mktime(datetime.datetime.strptime(date,"%Y-%m-%d").timetuple())
    
    number = 3600*24*daycount
    
    timestamp = timestamp + number
    #generate 2014-03-03 stuff
    result = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    return result

def DownLoad(ssid,date):
    Curl = """ curl "https://10.0.1.5/dl_log.php?user=admin&type=0&ssid=""" + ssid+"&select_date=" 
    for i in range(0,14):
        downloaddate = TimeOutput(date,i)
    #print Curl + downloaddate
        command = Curl + downloaddate + '"' +" -k -b PHPSESSID=" + ssid+" >>" + "all.log"
        os.system(command)
def Summary():
    command = "cat all.log | mawk -F src\= '{print $2}' | awk '{print $1}' | sed '/^$/d' |  sort -n | uniq -c | sort -n"
    os.system(command)



if  __name__ == '__main__':
    
    ssid = raw_input("ssid:")
    date = raw_input("date:")
    DownLoad(ssid,date)
    Summary()

