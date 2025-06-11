from nicegui import ui

ui.label('NiceGui Video Tutorial')

video = ui.video('drone.mp4').classes('w-96')

with ui.row():
    ui.button('play', color='green', icon='play_circle', on_click=video.play)
    ui.button('pause', color='red', icon='pause_circle', on_click=video.pause)
    ui.button('Jump to 0.05', on_click=lambda: video.seek(5))







ui.run()