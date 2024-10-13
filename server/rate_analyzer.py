
from datetime import datetime


infile = r"C:\SystemDesign\rate-limiter\server\server.log"

important = []
temp =[]

def get_unix_timestamp(timestamp):
    # Convert the string to a datetime object
    dt_object = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S") 

    # Convert the datetime object to Unix time
    unix_time = int(dt_object.timestamp())
    return unix_time

def get_readable_timestamp(unix_timestamp):
    return datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')

with open(infile) as f:
    f = f.readlines()

timer = {}
for line in f:
    if "has pinged at" in line:
        temp=line.split()
        time_stamp = temp[-2] + " " + temp[-1].split(".")[0]
        time_stamp_unix = get_unix_timestamp(time_stamp)
        min_time_number = time_stamp_unix - time_stamp_unix%60
        if min_time_number in timer:
            timer[min_time_number]+=1
        else:
            timer[min_time_number]=1


for key in timer.keys():
    print(f"{get_readable_timestamp(key)}-->{timer[key]}")
