from bucket import Bucket
import time

b = Bucket(20, 5)
print(b.get_current_status())
for i in range(10):
    b.consume_token()

print(b.get_current_status())
# time.sleep(70)
# b.bucket_refill()
# print(b.get_current_status())
print(time.time())
time.sleep(150)

for i in range(10):
    time.sleep(10)
    a = time.time()
    print(i,a-a%60)
    b.consume_token()
    b.bucket_refill()
    print(b.get_current_status())

