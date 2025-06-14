from nicegui import ui

name = ui.input('Name')
country = ui.input('Country')
age = ui.input('Age')


ui.button('Show', color='green', on_click=lambda:show())


def show():
    value = 0
    if name.value == "" and country.value == "" and age.value == "":
        value = 1
        ui.notify('You entered none of them!', type='negative')

    if (name.value == "" or country.value == "" or age.value == "") and value == 0:
        ui.notify('You did not enter one of them!', type='warning')

    if name.value != "" and country.value != "" and age.value != "":
        ui.notify('That is okay', type='positive')

    pass




ui.run()