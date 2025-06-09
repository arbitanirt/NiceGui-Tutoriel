from nicegui import ui


joystick = ui.joystick(color='blue', on_move=lambda e:set(e), on_end=lambda : coordinates.set_text('0, 0'))


def set(e):
    coordinates.set_text(f"{e.x:.3f}, {e.y:.3f}")

    if e.x > 0 and e.y > 0:
        image.set_source('football.jpg')

    if e.x < 0 and e.y > 0:
        image.set_source('tennis.jpg')

    if e.x < 0 and e.y < 0:
        image.set_source('hockey.jpg')

    if e.x > 0 and e.y < 0:
        image.set_source('basketball.jpg')

coordinates = ui.label('0, 0')
image = ui.image('').classes('w-48')
ui.run()