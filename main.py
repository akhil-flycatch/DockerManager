from prompt_toolkit.application import Application
from my_docker_manager.key_bindings import kb
from my_docker_manager.layout import layout
from my_docker_manager.create_ui import style

app = Application(layout=layout,key_bindings=kb,style=style,full_screen=True)
app.run()
