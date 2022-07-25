## description

most projects frequently face to the operation system difference between developers who join in.

For the solution of the the operation system difference, docker is popular and often used with container management services.

However, learning docker is sometime complicated for who do not used to build infrastructures or Virtual environment on cloud services or on-premise.

this library is for developers who desire to avoid to spend time on building the environments on any projects.

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

# check that docker container can run

# download dockerfile
pywhale 

```

## MySQL

to start running the MySQL container

```:python

pywhale startmysql

```

