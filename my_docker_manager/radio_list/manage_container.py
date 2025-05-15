from prompt_toolkit.widgets import RadioList
from my_docker_manager.services.manage import manager
radio=RadioList(manager.fetch_containers())
