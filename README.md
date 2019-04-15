## Python docker interface

## Prerequisites
Make sure that python3 and docker / docker-compose are installed. That's all :) 

## Usage
In order to use this package, perform a git clone and then run the following command:
`python3 main.py`

## Options

### - Inspect
The inspect button inspects the current selected project, returning containers that exists for it.
Inspect checks also whether ports 80 and 443 are in use.

### - Build
The build button will check how many files named like `Dockerfile` exists and it will ask if to build the first one 
or all of them. If an project doesn't have dockerfile, it will not appear in the projects list.

### - Run
The run button performs two different tasks, based on your local project configuration.
- deploys a stack using the `docker-compose` package (if exists);
@TODO: check if docker-compose exists
- starts an container based on the image with the project's name

### - Remove
The remove button will check whether there is docker-compose.yml within the project and perfom the following tasks:
- if the project has the file, it will perform execute the `docker stack rm` command
- if it doesn't, it will forcely remove the container with the project's name 

### - Prune
It will execute the command `docker system prune`

### - Clear
It will clear the console screen

### - Close
Close the application

#Contributing
For any contribution, you know what you have to do :)


