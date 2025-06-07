from nicegui import ui

gender_image = ui.image('').classes('w-48')
radio_image = ui.image('').classes('w-48')

toggle_gender = ui.toggle(['WOMEN', 'MEN'], on_change = lambda : gender_image.set_source(f'{toggle_gender.value}.png'))
radio_country = ui.radio(['england', 'usa'], on_change = lambda : radio_image.set_source(f'{radio_country.value}.png'))
ui.run()