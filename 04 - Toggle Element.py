from nicegui import ui


label = ui.label('ARBI')
toggle_text = ui.toggle(['text_1', 'text_2', 'text_3', 'text_4'], value='text_1', on_change=lambda : label.set_text(f'You clicked {toggle_text.value}'))
image = ui.image('javascript.png').classes('w-64')
toggle_image = ui.toggle(['javascript','Python'], on_change=lambda : image.set_source(f'{toggle_image.value}.png'))


ui.run()