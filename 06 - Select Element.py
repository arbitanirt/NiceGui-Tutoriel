from nicegui import ui

teams = ['Real Madrid', 'Barcelona', 'Liverpool']

selects_teams = ui.select(teams)

team_image = ui.image('real madrid.png').classes('w-48')

ui.button('Click Me', on_click = lambda : team_image.set_source(f'{selects_teams.value}.png'))

ui.run()