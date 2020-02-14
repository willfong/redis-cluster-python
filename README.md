# redis-cluster-python


https://github.com/antirez/redis/issues/2410


docker exec -it redis1 redis-cli --cluster create 172.23.0.2:6379 172.23.0.3:6379 172.23.0.4:6379 172.23.0.5:6379 172.23.0.6:6379 172.23.0.7:6379 --cluster-replicas 1