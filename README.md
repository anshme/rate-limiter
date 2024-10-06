# rate-limiter
Rate limiter implementation given in System design by Alex Xu

2024-10-06:
$ nohup python server.py > server.log 2>&1 & (for backgroud running of server)
$ tail -f server.log (to check for server.log)
-> Write a python program to read server.log and calculate requests per minute