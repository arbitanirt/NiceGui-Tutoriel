from nicegui import ui

with ui.timeline(side='right'):
    with ui.row():
        ui.image('ronaldo.jpg').classes('w-24')
        ui.timeline_entry('Rolando',
                        title='Footbleur',
                        subtitle='14 juin 2025',)
        ui.image('ibrahimovic.jpg').classes('w-2')
        ui.timeline_entry('Ibrahimovic',
                        title='Footbleur',
                        subtitle='14 juillet 2023', )
        ui.image('liz.truss.jpg').classes('w-24')
        ui.timeline_entry('Liz Truss',
                        title='Primer Minister',
                        subtitle='10 Aout 2018', )




ui.run()