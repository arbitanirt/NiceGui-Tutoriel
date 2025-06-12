from nicegui import ui
from nicegui.elements import leaflet

map = ui.leaflet(center=(48.964, 2.349))
ui.label().bind_text_from(map, 'center', lambda center: f'Center: {center[0]:.3f}, {center[1]:.3f}')

ui.label().bind_text_from(map, 'zoom', lambda zoom: f'Zoom: {zoom}')

with ui.row():
    ui.button('New York', color='red', on_click=lambda:map.set_center((40.730, -73.935)))
    ui.button('London', color='green', on_click=lambda:map.set_center((51.509, -0.118)))

with ui.row():
    ui.button(icon='zoom_in', on_click=lambda:map.set_zoom(map.zoom + 1))
    ui.button(icon='zoom_out', on_click=lambda:map.set_zoom(map.zoom - 1))


ui.run()