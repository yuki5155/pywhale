from pywhale.core.managers.base import BaseClass


class DownContainerClass(BaseClass):

    def __init__(self):
        self.containers_list = self.client.containers.list()
        self.is_process = True
        self.is_all_force = True
        self.is_no_volumes = True
    def show_container_list(self):
        self.containers_list = self.client.containers.list()
        for c, i in enumerate(self.containers_list):
            print(f"[{c}]:{i.name}")
        return len(self.containers_list)
    def delete_all(self):
        self.client.containers.prune()
    def delete_one(self, target:int):
        self.containers_list[int(target)].remove(force=self.is_all_force, v=self.is_no_volumes)
    def run_command(self):
        while self.is_process:
            if self.show_container_list() == 0:
                print("no containers are existed")
                break
            print("enter the command")
            print("[q]quit [d]delete a container [da]delete all containers")
            c = input("")
            
            if c == "q" or c =="quit":
                break
            if c == "d" or c =="delete":
                print("select the container will be deleted")
                self.show_container_list()
                target_container:int = input("")
                
                if isinstance(int(target_container), int):
                    self.delete_one(int(target_container))
                # delete
                continue
            if c == "da" or c== "deleteall":
                self.delete_all()
                break

        