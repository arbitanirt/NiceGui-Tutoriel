from nicegui import ui

with ui.stepper().props('vertical').classes('w-full') as stepper:
    with ui.step('Enter your name :'):
        name = ui.input('Name :')
        with ui.stepper_navigation():
            ui.button('NEXT', on_click=stepper.next)
    with ui.step('Enter your age :'):
        age = ui.input('Age :')
        with ui.stepper_navigation():
            ui.button('NEXT', on_click=stepper.next)
            ui.button('BACK', on_click=stepper.previous).props('flat')
    with ui.step('Enter your country :'):
        country = ui.input('Country :')
        with ui.stepper_navigation():
            ui.button('DONE', on_click=lambda: ui.notify('Complete!', type='positive'))
            ui.button('BACK', on_click=stepper.previous).props('flat')
            ui.button('SHOW INPUT', on_click=lambda:show())

def show():
    ui.label(f'Name: {name.value} - Age: {age.value} - Country: {country.value}')





ui.run()