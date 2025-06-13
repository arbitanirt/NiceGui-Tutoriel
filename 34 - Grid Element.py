from nicegui import ui

name_input = ui.input('Name ')
age_input = ui.input('Age : ')
height_input = ui.input('Weight : ')

ui.button(text='Save', icon='save', color='green', on_click=lambda:save())


with ui.grid(columns=2):
    name_title = ui.label('Name : ')
    name_value = ui.label()

    age_title = ui.label('Age : ')
    age_value = ui.label()

    height_title = ui.label('Weight : ')
    height_value = ui.label()



def save():
    name_value.set_text(name_input.value)
    age_value.set_text(age_input.value)
    height_value.set_text(height_input.value)
    pass



ui.run()