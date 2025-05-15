from prompt_toolkit.key_binding import KeyBindings

kb= KeyBindings()

@kb.add("q")
def _(event):
    event.app.exit()
