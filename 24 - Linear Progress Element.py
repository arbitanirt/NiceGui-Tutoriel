from nicegui import ui

name = ui.input("Enter your name: ", on_change=lambda:update())
surname = ui.input("Enter your surname: ", on_change=lambda:update())

gender = ui.radio(["Male", "Female"], on_change=lambda:update())

with ui.row():
    lab = ui.label('Entry your country : ')
    country = ui.select(["United States", "United Kingdom","India", 'Russia'], on_change=lambda:update())

button = ui.button("Save", icon='save', color='green', on_click=lambda : save())

slider = ui.slider(min=0, max=1, step=0.25, value=0)
linear_progress = ui.linear_progress().bind_value_from(slider, 'value')

def update():
    if name.value != "" and slider.value < 0.25:
        slider.value = slider.value + 0.25
    if surname.value != "" and slider.value <= 0.25:
        slider.value = slider.value + 0.25
    if gender.value != None and slider.value <= 0.50:
        slider.value = slider.value + 0.25
    if country.value != None and slider.value <= 0.75:
        slider.value = slider.value + 0.25

def save():
    ui.label(f'{name.value} {surname.value} {gender.value} {country.value}' )

ui.run()