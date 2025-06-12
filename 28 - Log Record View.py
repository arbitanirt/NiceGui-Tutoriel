from nicegui import ui
from datetime import datetime


name = ui.input('Name')
surname = ui.input('Surname')

button = ui.button('Save', icon='save', color='green', on_click=lambda:save())
log = ui.log(max_lines=10).classes('w-full h-20')


def save():
    log.push(f"you entered -> Name : {name.value} Surname : {surname.value}\
            {datetime.now().strftime('%X.%f')[:-5]}")



ui.run()