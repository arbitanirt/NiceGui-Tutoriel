from nicegui import ui

switch_basketball = ui.switch('Basketball', on_change=lambda : set())
switch_football = ui.switch('Football', on_change=lambda : set())

def set():
    #print('Turtle Code')
    #ui.label(f'{switch_basketball.value}')
    #ui.label(f'{switch_football.value}')
    if switch_basketball.value == True and switch_football.value == False:
        label.set_visibility(True)
        image.set_visibility(True)
        image.set_source('basketball.jpg')
        label.set_text('I love Basketball')

    if switch_basketball.value == False and switch_football.value == True:
        label.set_visibility(True)
        image.set_visibility(True)
        image.set_source('football.jpg')
        label.set_text('I love Football')

    if switch_basketball.value == True and switch_football.value == True:
        label.set_visibility(False)
        image.set_visibility(False)

    if switch_basketball.value == False and switch_football.value == False:
        label.set_visibility(False)

image = ui.image('').classes('w-64')
image.set_visibility(False)



label = ui.label('')


ui.run()