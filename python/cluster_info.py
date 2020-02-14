from rediscluster import RedisCluster

startup_nodes = [{"host": "172.23.0.2", "port": "6379"}]

try:
    rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
except:
    print("error")
    exit(1)

