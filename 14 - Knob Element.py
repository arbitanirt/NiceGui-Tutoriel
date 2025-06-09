from nicegui import ui

knob = ui.knob(5, min=0, max=100, show_value=True, center_color="red", on_change=lambda : set(knob.value))

def set(e):
    if e > 0 and e < 25:
        image.set_source('football.jpg')
    if e > 25 and e < 50:
        image.set_source('basketball.jpg')
    if e > 50 and e < 75:
        image.set_source('tennis.jpg')
    if e > 75:
        image.set_source('hockey.jpg')
    label.set_text(f'{e}')


label = ui.label('Arbi')
image = ui.image('').classes('w-48')

ui.run()