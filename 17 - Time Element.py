from nicegui import ui

clock = ui.time(value='13:00', on_change=lambda: set())
date = ui.date(value='2024-01-20', on_change=lambda: set())

def set():
    label.set_text(f'{str(date.value)} {str(clock.value)}')



label = ui.label('Arbi Code')






ui.run()