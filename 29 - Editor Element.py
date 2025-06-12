from nicegui import ui

editor = ui.editor(placeholder='Type Something Here', on_change=lambda:write())

def write():
    text.set_text(f'HTML Code : {editor.value}')


text = ui.label('T')



ui.run()