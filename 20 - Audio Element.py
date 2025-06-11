from nicegui import ui

ui.label('Nicegui Audio Tutorial')

audio = ui.audio('music.mp3')

with ui.row():
    ui.button('play', color='green', on_click=audio.play)
    ui.button('pause', color='red', on_click=audio.pause)
    ui.button('Jump to 0:45', on_click=lambda : audio.seek(45))


ui.run()