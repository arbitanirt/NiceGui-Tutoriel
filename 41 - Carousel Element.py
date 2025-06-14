from nicegui import ui

with ui.carousel(arrows=True, navigation=True).props('height=340px'):

    with ui.carousel_slide().classes('p-0'):
        with ui.card().tight():
            ui.label("Let's play football")
            with ui.card_section():
                ui.image('football.jpg').classes('w-[280px]')

    with ui.carousel_slide().classes('p-0'):
        with ui.card().tight():
            ui.label("Let's play Hockey")
            with ui.card_section():
                ui.image('hockey.jpg').classes('w-[280px]')

    with ui.carousel_slide().classes('p-0'):
        with ui.card().tight():
            ui.label("Let's play tennis")
            with ui.card_section():
                ui.image('tennis.jpg').classes('w-[280px]')






ui.run()