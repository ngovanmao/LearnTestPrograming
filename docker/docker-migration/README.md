Build tcpserver docker image
and start the docker container normally as following
 
```
  sudo docker run --name tcpMao -p 9999:9999 -d tcpserver5
```

Query several time from the client to make sure the index is increased.

```
$ ./tcp-client.py haha3
Sent:     haha3
Received: HAHA3 1

$ ./tcp-client.py haha3
Sent:     haha3
Received: HAHA3 2
```

Do a checkpoint:

```
$ sudo docker checkpoint create tcpMao checkpoint1
```

Query again to make sure the container is down.
Then restore the container from this computer, and start query again.
The expectation is that the return index is started from the previous index.

```
$ sudo docker start --checkpoint checkpoint1 tcpMao

$ sudo docker ps -a
 CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS                        PORTS                    NAMES
 c657ce58d157        tcpserver5          "/bin/sh -c 'pytho..."   About a minute ago   Up 1 second                   0.0.0.0:9999->9999/tcp   tcpMao

$ ./tcp-client.py haha4
Sent:     haha4
Received: HAHA4 5

```
