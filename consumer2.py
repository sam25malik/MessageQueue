import redis
import time
import json
from redis import Redis
r=redis.StrictRedis(host='localhost', port=6379, db=0)
p=r.pubsub()
p.subscribe('test')


while True:
	message = p.get_message()
	if message:
		#print(message)
		#r.sadd('test',message['data'])
		#print "Subscribe: %s" % message['data']
		if r.srem('test',message['data'])==1:
			print "Consumer 2 Subscribe: %s" % message['data']
	time.sleep(1)
