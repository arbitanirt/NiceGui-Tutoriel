from nicegui import ui


name_input = ui.input(label='Name', placeholder='Enter your Name')
text_area = ui.textarea(label='Message', placeholder='Enter a message')
button = ui.button(text='Send Message', on_click=lambda:send())

def send():
    ui.chat_message(f'{text_area.value}', name=f'{name_input.value}', avatar='https://robohash.org/ui')
    name_input.value = ''
    text_area.value = ''


ui.run()