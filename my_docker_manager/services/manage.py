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

class ManageImages:
    def __init__(self):
        self.image=[]
        self.image_option=[]
    def fetch_images(self):
        result=run(["docker","images", "--format", "{{.ID}} {{.Repository}} {{.Tag}} {{.Size}}"], capture_output=True, text=True)
        self.image=[line.strip() for line in result.stdout.splitlines()]
        if self.image:
            self.image_option=[(line.split(maxsplit=2)[0],line)for line in self.image]
        else:
            self.image_option=[("none", "no image selected")]
        return self.image_option
manager=Manage()
image_manager=ManageImages()
