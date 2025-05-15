from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.widgets import Frame
from my_docker_manager.radio_list.manage_container import radio

frame = Frame(title="Docker Containers", body=radio)
container= HSplit([
    frame,Window(height=1,char="▩ ")]
)
layout= Layout(container)
