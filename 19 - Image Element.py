from nicegui import ui

#ui.link("football", "https://www.kooora.com/")

with ui.row():
    with ui.link(target="https://www.kooora.com/"):
        with ui.image("football.jpg").classes("w-48"):
            ui.label('Football').classes('absolute-bottom text-subtitle2 text-center')

    with ui.link(target="https://www.kooora.com/"):
        with ui.image("basketball.jpg").classes("w-48"):
            ui.label('Basketball').classes('absolute-bottom text-subtitle2 text-center')

with ui.row():
    with ui.link(target="https://www.kooora.com/"):
        with ui.image("tennis.jpg").classes("w-48"):
            ui.label('Tennis').classes('absolute-bottom text-subtitle2 text-center')

    with ui.link(target="https://www.kooora.com/"):
        with ui.image("hockey.jpg").classes("w-48"):
            ui.label('Hockey').classes('absolute-bottom text-subtitle2 text-center')


ui.run()
