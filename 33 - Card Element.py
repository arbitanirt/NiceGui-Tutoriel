from nicegui import ui

with ui.row():
    with ui.card():
        ui.label('Welcome to Python Course')
        with ui.card().tight():
            ui.image('python.png').classes('w-48')
            with ui.card_section():
                ui.label('You will learn everthing you need about Python!')
                with ui.expansion('Go to Course!', icon='work').classes('w-full'):
                    ui.label('inside the expansion')
                    
    with ui.card():
        ui.label('Welcome to Javascript Course')
        with ui.card().tight():
            ui.image('javascript.png').classes('w-48')
            with ui.card_section():
                ui.label('You will learn everthing you need about Javascript!')
                with ui.expansion('Go to Course!', icon='work').classes('w-full'):
                    ui.label('inside the expansion')



ui.run()