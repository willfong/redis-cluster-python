import socket

found_nodes = []

for x in range(1, 100):
    try: 
        found_nodes.append(socket.gethostbyname(f"redis{x}"))
    except socket.error:
        continue

found_nodes.sort()

addrs = ":6379 ".join(found_nodes)

print(f"docker exec -it redis1 redis-cli --cluster create {addrs}:6379 --cluster-replicas 1")

