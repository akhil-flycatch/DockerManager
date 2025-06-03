from prompt_toolkit.widgets import RadioList
from my_docker_manager.services.manage import manager, image_manager
radio=RadioList(manager.fetch_containers())
image_radio=RadioList(image_manager.fetch_images())
