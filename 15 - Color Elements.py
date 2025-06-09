from nicegui import ui

label = ui.markdown('***Welcome to Arbi Code***')
color_input = ui.color_input(label='Color Input', value='#000000', on_change=lambda:set())

def set():
    label.style(f'color:{color_input.value}')

button = ui.button(icon='colorize', on_click=lambda:picker())

def picker():
    ui.color_picker(on_pick=lambda
                    e : button.style(f'background-color:{e.color}!important'))

ui.run()