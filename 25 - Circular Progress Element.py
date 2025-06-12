from nicegui import ui

with ui.circular_progress(min=0, max=1, value=0, show_value=False) as progress:
    ui.button(
        icon='star',
        on_click=lambda:set_image()
    ).props('flat round')

def set_image():
    progress.set_value(progress.value + 0.25)
    if progress.value <= 0.25:
        image.set_source('football.jpg')
    if progress.value > 0.25 and progress.value <= 0.50:
        image.set_source('basketball.jpg')
    if progress.value > 0.50 and progress.value <= 0.75:
        image.set_source('tennis.jpg')
    if progress.value > 0.75:
        image.set_source('hockey.jpg')
    pass

image = ui.image('').classes('w-48')

"""
slider = ui.slider(min=0, max=1, step=0.25, value=0, on_change=lambda:set_image())
ui.circular_progress().bind_value_from(slider, 'value')

def set_image():
    if slider.value <= 0.25:
        image.set_source("football.jpg")
    if slider.value > 0.25 and slider.value <= 0.50:
        image.set_source("basketball.jpg")
    if slider.value > 0.50 and slider.value <= 0.75:
        image.set_source("tennis.jpg")
    if slider.value > 0.75:
        image.set_source("hockey.jpg")
    pass


image = ui.image('').classes('w-48')
"""

ui.run()