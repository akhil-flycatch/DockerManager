from subprocess import run

class Manage:
    def __init__(self):
        self.container=[]
        self.option=[]
    def fetch_containers(self):
        result=run(["docker","ps","-a","--format","{{.ID}} {{.Image}} {{.Status}}"], capture_output=True, text=True)
        self.container=[line.strip() for line in result.stdout.splitlines()]
        if self.container:
            self.option=[(line.split(maxsplit=2)[0],line)for line in self.container]
        else:
            self.option=[("none","no containers found")]
        return self.option
manager=Manage()
