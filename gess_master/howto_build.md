## Build

```
$ docker build --tag rmoff/gess .
Sending build context to Docker daemon  750.6kB
Step 1/5 : FROM python:2.7
 ---> 8972b8902495
Step 2/5 : ADD scripts /scripts
 ---> 1bfcbb7ef9c8
Step 3/5 : ADD data /data
 ---> bc9f663f6e30
Step 4/5 : ADD gess.conf /gess.conf
 ---> 7d61e66dbba1
Step 5/5 : CMD ["python","/scripts/gess-main.py"]
 ---> Running in 4f6d1c0fb668
Removing intermediate container 4f6d1c0fb668
 ---> 7a2ef3f05207
Successfully built 7a2ef3f05207
Successfully tagged rmoff/gess:latest
```

## Push

```
$ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: rmoff
Password:
Login Succeeded
[~/g/d/ksql-atm-fraud-detection] Robin@asgard02.moffatt.me  (connect-jdbc|✚1)
$
[~/g/d/ksql-atm-fraud-detection] Robin@asgard02.moffatt.me  (connect-jdbc|✚1)
$ docker push rmoff/gess
The push refers to repository [docker.io/rmoff/gess]
3feda90c4bfd: Layer already exists
730cad7d84c6: Pushing [==================================================>]  69.63kB
3f80cb8128bd: Pushing [==================================================>]  19.46kB
2b5901b57751: Layer already exists
6ab6861db2d4: Layer already exists
130f23df7a35: Layer already exists
0d184ba72737: Layer already exists
a19cb627cc73: Waiting
ab016c9ea8f8: Layer already exists
2eb1c9bfc5ea: Layer already exists
0b703c74a09c: Layer already exists
b28ef0b6fef8: Waiting
```
