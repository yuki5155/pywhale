from pywhale.core.managers.base import BaseClass
import requests

class CreateDockerfileCLass(BaseClass):
    def run_command(self):
        
        res = requests.get(
            "https://7ndr69xe2m.execute-api.us-east-2.amazonaws.com/Prod/hello"
        )
        print(res.json())