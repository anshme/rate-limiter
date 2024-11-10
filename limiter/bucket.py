import time
import logging

logging.basicConfig(level=logging.INFO)

class Bucket:
    def __init__(self, bucket_size, refiller_rate) -> None:
        self.bucket = [True] * bucket_size
        self.bucket_size = bucket_size
        self.refiller_rate = refiller_rate
        init_time = time.time()
        self.last_refill = int(init_time - init_time % 60)

    def get_current_bucket_status(self):
        return self.bucket
    
    def is_bucket_empty(self):
        return len(self.bucket) == 0
    
    def bucket_refill(self):
        if len(self.bucket) < self.bucket_size:
            cur_time = time.time()
            calculted_refill = ((int(cur_time - cur_time % 60)) - self.last_refill) / 60 * (self.refiller_rate)
            if calculted_refill != 0:
                token_refill = min(self.bucket_size, len(self.bucket) + calculted_refill)
                logging.info(f"adding token {token_refill}")
                self.bucket = [True] * int(token_refill)
                self.last_refill = cur_time - cur_time % 60

    def consume_token(self):
        self.bucket.pop()

    def token_bucket_algo(self):
        self.bucket_refill()
        if not self.is_bucket_empty():
            self.consume_token()
            return True
        else:
            return False





    