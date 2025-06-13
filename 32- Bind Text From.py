from nicegui import ui

data = {'number_1': 22, 'number_2': 20}

ui.label().bind_text_from(data, 'number_1' ,backward=lambda a: f'First Number {a}')
ui.label().bind_text_from(data, 'number_2' ,backward=lambda a: f'First Number {a}')


select = ui.select(['first number', 'second number'])

with ui.row():
    ui.button('UP', color='green', icon='trending_up', on_click=lambda :up())
    ui.button('DOWN', color='red', icon='trending_down', on_click=lambda :down())

def up():
    if select.value == 'first number':
        data.update(number_1 = data['number_1']+1)
    if select.value == 'second number':
        data.update(number_2 = data['number_2']+1)

def down():
    if select.value == 'first number':
        data.update(number_1 = data['number_1']-1)
    if select.value == 'second number':
        data.update(number_2 = data['number_2']-1)

ui.run()