import os, socket
from glob import glob
from . import decorators

BASEDIR = "../"

def getDirs(path):
    """
    Get directories from path
    containing Dockerfile
    :return:
    """
    directories =  next(os.walk(path))[1]
    alldirs = filter(lambda x: x.startswith(".") == False, directories)
    for dir in alldirs:
        if getDockerfiles(dir):
            yield dir

def checkbaseportisopened(port):
    """
    Check if the given port is in use
    :param port:
    :return:
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def getDockerfiles(project):
    """
    Get a list of dockerfiles from the project
    :param project:
    :return:
    """
    return glob(os.path.abspath(BASEDIR + project + "/*ockerfile*"))

def buildDockerfiles(info, dockers, project, all = False):
    if all:
        count = 0
        for d in dockers:
            count += 1
            _build(info, d, project + "_" + str(count))
    else:
        _build(info, dockers[0], project)

@decorators.executeCommand("Building Dockerfile(s)")
def _build(info, path, name):
    #print("docker build -t " + name + " -f " + path + " " + os.path.dirname(path))
    return "docker build -t " + name + " -f " + path + " " + os.path.dirname(path)

@decorators.executeCommand("Starting project")
def _run(info, project, is_composer):
    if is_composer:
        return "docker stack deploy -c " + BASEDIR + project + "/docker-compose.yml " + project

@decorators.executeCommand("Project changed")
def getContainers(name):
    """
    getting the id of the container
    :param name:
    :return:
    """
    return "docker ps -aqf name={}".format(name)

def getWarnings():
    """
    Get the warnings
    :return:
    """
    ports = (80, 443)
    for p in ports:
        if checkbaseportisopened(p):
           yield "Warning: Port {} already in use \n".format(p)

@decorators.executeCommand("Executing system prune")
def sysPrune(info):
    """
    Execute docker system prune
    :return:
    """
    return "docker system prune -f"

@decorators.executeCommand("Inspecting the current project")
def inspectProject(info, project):
    """
    Inspect the project
    :param project:
    :return:
    """
    return "docker ps -f name=" + \
           project + " --format ID={{.ID}}\\nImage={{.Image}}\\nName={{.Names}}\\nPort={{.Ports}}\\n"

def checkIfComposerExists(dir):
    return "Project has docker-compose.yml\n" \
        if glob(BASEDIR + dir + '/docker-compose.yml') \
        else "Project doesn\'t have docker-compose.yml\n"

def checkIfComposerExistsBool(dir):
    return True \
        if glob(BASEDIR + dir + '/docker-compose.yml') \
        else False

@decorators.executeCommand("Removing stack for the project")
def stackRM(info, project):
    """
    Removing an docker stack for the current project
    :param info:
    :param project:
    :return:
    """
    return "docker stack rm " + project