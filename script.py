import subprocess
from pywhale.core.managers import start_command
class DockerCommandClass():
    command = subprocess
    def run_command(self, command=None):
        # command.
        image_list = self.command.run(["docker","ps"], stdout=subprocess.PIPE, text=True, check=True)
        print(image_list.stdout)

def run_command():
    list_files = subprocess.run(["docker","ps"], stdout=subprocess.PIPE, text=True, check=True)

    print(type(list_files.stdout))  # He

def run_python_image():
    list_files = subprocess.run(["docker","ps"], stdout=subprocess.PIPE, text=True, check=True)

# d = DockerCommandClass()
# d.image_list()

start_command()

# 
# docker image build -t pywhale .

# docker run -itd pywhale /bin/sh  

# docker run --name pywhale -itd pywhale /bin/sh

# 1027  docker cp ./script.py pywhale:./script.py

# docker container exec -it pywhale bash