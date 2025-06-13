from nicegui import ui


with ui.splitter().classes('w-64') as splitter:
    with splitter.before:
        ui.image('python.png').classes('w-12')
        ui.label('Python Course!')
    with splitter.after:
        ui.image('javascript.png').classes('w-12')
        ui.label('javascript Course!')




ui.run()