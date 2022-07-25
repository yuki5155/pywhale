## description

most projects frequently face to the problem of the operation system difference between developers who join in.

For the solution of the the operation system difference, docker is one of the popular and often used on the cloud with container management services.

However, without docker-compose and dockerfiles someone already created, learning docker is sometime complicated for who have never built infrastructures or Virtual environment on cloud services or on-premise.

this library is for developers who desire to avoid to spend time on building the environments on any projects and beginner developpers.

### for example

- to avoid to install required libraries or softwares for the usage of aws-cli and cdk.
- to create the cache(redis) and database containers with one command that are connectable from other containers.
- no requirements to provide dockerfile by yourself if your projects use dockerfile from this libularies.
    - provided dockerfiles can be searched via the command.

## get-started

before the beginning, those installations are recommended.

- VSCode
- RemoContainer(the plugin of VSCode)
- docker

only python3 supported!!, not python2!!
run docker before running commands below


```
pip install git+https://github.com/yuki5155/pywhale.git

# check that docker container can run or not

# comining soon
# download dockerfile
# pywhale 

```

## MySQL

to start running the MySQL container

```:python

pywhale startmysql

```

