from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, Window, ConditionalContainer
from prompt_toolkit.widgets import Frame
from my_docker_manager.radio_list.manage_container import radio, image_radio
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.filters import Condition

# Create frames for containers and images
container_frame = Frame(title="Docker Containers", body=radio, style="class:frame.label")
image_frame = Frame(title="Docker Images", body=image_radio, style="class:frame.label")

# Output window for feedback
selected_output = FormattedTextControl(text="Selected: None")
output_window = Window(content=selected_output, height=1)

# Tab state to track active tab
class TabState:
    def __init__(self):
        self.active_tab = 0  # 0 for Containers, 1 for Images
    def focus_on(self, app):
        # Set focus to the appropriate RadioList based on active tab
        try:
            if self.active_tab == 0:
                app.layout.focus(radio)
            else:
                app.layout.focus(image_radio)
        except Exception as e:
            # Fallback in case of focus error
            pass
tab_state = TabState()

# Header to show active tab
header = Window(
    content=FormattedTextControl(
        text=lambda: f"Active Tab: {'Containers' if tab_state.active_tab == 0 else 'Images'} [Left/Right to switch, q to quit]"
    ),
    height=1,
    style="class:tab.active"
)

# Conditional containers for tabs
container_tab = ConditionalContainer(
    content=container_frame,
    filter=Condition(lambda: tab_state.active_tab == 0)
)
image_tab = ConditionalContainer(
    content=image_frame,
    filter=Condition(lambda: tab_state.active_tab == 1)
)

# Layout with header, tab content, and output
container = HSplit([
    header,
    Window(height=1, char="▩"),
    container_tab,
    image_tab,
    Window(height=1, char="▩"),
    output_window
])
layout = Layout(container)
