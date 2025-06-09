from nicegui import ui

file_input = ui.input(label='File Name', placeholder='Enter a file name', password=False)
pwd_input = ui.input(label='Password', placeholder='Enter your password', password=True)

button = ui.button(text='Show Image', on_click=lambda : set())

def set():
    image.set_source(str(file_input.value))


image = ui.image('').classes('w-48')


ui.run()