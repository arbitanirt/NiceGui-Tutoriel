from nicegui import ui
from nicegui.elements import badge

ui.button('Click Me', color='blue', on_click=lambda : ui.label('You Click Me'))
ui.button('Show Link', color='red', on_click=lambda : ui.link('Button and Badge Elements - Python NiceGUI Tutorial 3', 'https://www.youtube.com/watch?v=u4-VTXwmYvM&list=PLMi6KgK4_mk1xZc45zEBxlByLhpbJK2Uy&index=3'))
ui.button('Click Me', color='green', on_click=lambda : ui.notify('You Click Me'))

with ui.button('Click Me', color='yellow', on_click=lambda : badge.set_text(int(badge.text)+ 1)):
    badge = ui.badge('0', color='red').props('floating')


ui.run()