from nicegui import ui

name = ui.input('Name')
surname = ui.input('Surname')

save_button = ui.button('Save', icon='save', color='green', on_click=lambda:save())


def save():
    json = {'name': name.value, 'surname': surname.value}
    ui.json_editor({'content': {'json': json}})
    pass




ui.run()