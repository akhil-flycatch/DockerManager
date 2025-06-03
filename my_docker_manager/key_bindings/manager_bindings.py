from prompt_toolkit.key_binding import KeyBindings
from my_docker_manager.radio_list import radio
from my_docker_manager.layout import selected_output, tab_state
from my_docker_manager.radio_list.manage_container import image_radio
from subprocess import run
import shutil, platform, os
from prompt_toolkit.application import run_in_terminal, get_app



kb= KeyBindings()

@kb.add("q")
def _(event):
    event.app.exit()

@kb.add("s")
def _(event):
    if tab_state.active_tab == 0:  # Containers tab
        selected = radio.current_value
        if selected and selected != "none":
            result = run(["docker", "start", selected], capture_output=True, text=True)
            output = result.stdout.strip() or result.stderr.strip()
            selected_output.text = f"Started container: {output}"
        else:
            selected_output.text = "No container selected."
    else:  # Images tab
        selected = image_radio.current_value
        if selected and selected != "none":
            selected_output.text = f"Images tab active. Selected image: {selected}. (No start action defined for images.)"
        else:
            selected_output.text = "No image selected."
    event.app.invalidate()

@kb.add('x')
def _(event):
    if tab_state.active_tab == 0:  # Containers tab
        selected = radio.current_value
        if selected and selected != "none":
            result = run(["docker", "stop", selected], capture_output=True, text=True)
            output = result.stdout.strip() or result.stderr.strip()
            selected_output.text = f"Stopped container: {output}"
        else:
            selected_output.text = "No container selected."
    else:  # Images tab
        selected_output.text = "Images tab active. Stop action only available in Containers tab."
    event.app.invalidate()

@kb.add('l')
def _(event):
    if tab_state.active_tab == 0:  # Containers tab
        selected = radio.current_value
        if selected and selected != "none":
            result = run(["docker", "logs", selected], capture_output=True, text=True)
            output = result.stdout.strip() or result.stderr.strip()
            selected_output.text = output if output else "No logs found."
        else:
            selected_output.text = "No container selected."
    else:
        selected_output.text = "Images tab active. Logs action only available in Containers tab."
    event.app.invalidate()


@kb.add('r')
def _(event):
    if tab_state.active_tab == 1:
        selected = image_radio.current_value
        if selected and selected != "none":
            result = run(["docker", "image", "rm", selected], capture_output=True, text=True)
            output = result.stdout.strip() or result.stderr.strip()
            selected_output.text = f"Removed Image: {output}"
        else:
            selected_output.text = "No image selected"
    else:
        selected_output.text = "Images tab active. Stop action only available in Containers tab."
    event.app.invalidate()



@kb.add('t')
def _(event):
    selected = radio.current_value
    if selected:
        def run_shell():
            for shell in ["bash","sh"]:
                result= os.system(f"docker exec -it {selected} {shell}")
                if result == 0:
                    break
        selected_output.text = f"Opening container: {selected}"
        # Suspend prompt_toolkit, run the shell, and resume
        run_in_terminal(run_shell)

        # Manually refresh the app when done (on next iteration)
        get_app().invalidate()
    else:
        selected_output.text = "No container selected"
    event.app.invalidate()

@kb.add("left")
def _(event):
    tab_state.active_tab = max(0, tab_state.active_tab - 1)
    tab_state.focus_on(event.app)
    event.app.invalidate()

@kb.add("right")
def _(event):
    tab_state.active_tab = min(1, tab_state.active_tab + 1)
    tab_state.focus_on(event.app)
    event.app.invalidate()

