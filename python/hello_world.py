import random
import string
from rediscluster import RedisCluster

startup_nodes = [{"host": "redis1", "port": "6379"}]
rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


key1 = randomString(5)
val1 = randomString(10)

print(f"Random Key/Val: {key1} -> {val1}")

rc.set(key1, val1)

print("Checking key:")
print(rc.get(key1))
