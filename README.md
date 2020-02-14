# Redis Cluster + Python


This command will scan hostnames "redis[1-100]" and generate the string to initialize the cluster:
```docker exec -it python python init_cluster.py```

The command will look something like this: `docker exec -it redis1 redis-cli --cluster create 172.23.0.2:6379 ... --cluster-replicas 1`

We have to do this because Redis does not support hostnames, so we need to specify IPs. https://github.com/antirez/redis/issues/2410


This will show you the status of the cluster:
```docker exec -it redis1 redis-cli cluster info```
