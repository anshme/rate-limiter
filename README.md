# rate-limiter
Rate limiter implementation given in System design by Alex Xu

2024-10-06:
$ nohup python server.py > server.log 2>&1 & (for backgroud running of server)
$ tail -f server.log (to check for server.log)
-> Write a python program to read server.log and calculate requests per minute

epoch time : Sunday, October 13, 2024 7:30:00 AM  -- > 1728804600
epoch time : Sunday, October 13, 2024 7:31:00 AM  -- > 1728804660

2024-10-13:
->Rerouting for rate limiter middleware
 start.py ---> rate_limiter.py --->server.py
->rate_limiter.py

2024-11-03
Routing done through rate limiter.
1st start the main server by running the python file server/server.py. This would start a server at localhost 2002
Then start the rate limiter by running the python file rate_limiter/rate_limiter.py. This would start service at localhost 2022.