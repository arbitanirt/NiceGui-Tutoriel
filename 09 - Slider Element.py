from nicegui import ui
from nicegui.binding import refresh_loop

label = ui.label('value : 0')
slider = ui.slider(min=0, max=4, on_change=lambda : refresh()).props('label-always')

def refresh():
    if slider.value == 0:
        image.set_visibility(False)

    if slider.value == 1:
        image.set_visibility(True)
        image.set_source('basketball.jpg')

    if slider.value == 2:
        image.set_visibility(True)
        image.set_source('tennis.jpg')

    if slider.value == 3:
        image.set_visibility(True)
        image.set_source('hockey.jpg')

    if slider.value == 4:
        image.set_visibility(False)
        slider.set_enabled(False)



    label.set_text(f'value : {slider.value}')



image = ui.image('basketball.jpg').classes('w-64')

ui.run()