from prompt_toolkit.styles import Style

style = Style.from_dict({
    # Frame
    "frame.border":        "bold #74c7ec",  # Sapphire (softer blue for borders)
    "frame.label":         "bold bg:#313244 #b4befe",  # Surface0 + Lavender (clear, readable label)

    # General text and output
    "":                    "bg:#1e1e2e #cdd6f4",  # Base + Text (consistent background and text)
    "label":               "bold #f5c2e7",        # Pink (vibrant for labels)
    "output-field":        "#a6e3a1",             # Green (unchanged, good for output)
    "key":                 "bold #fab387",        # Peach (warmer than yellow, good for keys)

    # Tabs
    "tab.active":          "bold bg:#45475a #cdd6f4",  # Surface1 + Text (slightly lighter for active tab)
    "tab.inactive":        "bg:#1e1e2e #7f849c",       # Base + Overlay1 (dimmer for inactive tabs)

    # Radio list items
    "radio":               "bg:#313244 #bac2de",       # Surface0 + Subtext1 (neutral, readable)
    "radio.selected":      "bold bg:#89dceb #181825",  # Sky + Mantle (bright cyan for selected, dark bg)

    # Buttons
    "button":              "bg:#585b70 #f5e0dc",       # Surface2 + Rosewater (subtle button styling)
    "button.focused":      "bold bg:#94e2d5 #181825",  # Teal + Mantle (vibrant focused button)

    # Input / text area
    "text-area":           "bg:#181825 #cdd6f4",       # Mantle + Text (darker bg for input areas)
    "text-area.focused":   "bg:#313244 #f5c2e7",       # Surface0 + Pink (highlight focused input)

    # Success / Warning
    "success":             "bold #a6e3a1",             # Green (unchanged, clear for success)
    "warning":             "bold #f38ba8",             # Red (unchanged, clear for warnings)

    # Inverted keys (e.g., hint keys)
    "keybinding":          "reverse #fab387",          # Peach (unchanged, good contrast for hints)
})
