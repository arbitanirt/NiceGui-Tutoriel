from nicegui import ui

text_area = ui.textarea('Text', placeholder='Type your codes here!')

button = ui.button('Save', icon='save', color='green', on_click=lambda :save())


def save():
    ui.code(text_area.value)
    pass



ui.run()