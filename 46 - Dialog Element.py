from nicegui import ui
from nicegui.html import dialog

with ui.dialog() as dialog, ui.card():
    ui.label('Are you sure!')
    with ui.row() as row:
        ui.button('Yes', on_click=lambda:dialog.submit('Yes'))
        ui.button('No', on_click=lambda:dialog.submit('No'))



async def show():
    result = await dialog
    #ui.notify(f'You chose {result}')
    if result == 'Yes':
        text.set_text(f'{name.value} {country.value}.')
        name.value = ''
        country.value = ''
    if result == 'No':
        text.set_text('')

name = ui.input('Name')
country = ui.input('Country')
ui.button('Show', on_click=show)
text = ui.label('Info!')


ui.run()