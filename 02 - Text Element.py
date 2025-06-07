from nicegui import ui


ui.link('Text Elements - Python NiceGUI Tutorial 2 : ', 'https://www.youtube.com/watch?v=YJcsmwP9tJM')

ui.chat_message('Hello World', name='Robot', stamp='now', avatar='https://robohash.org/ui')

ui.chat_message('Hello World', name='Robot', stamp='now', avatar='https://robohash.org/ui')

ui.markdown('This is a **markdown** message')

ui.mermaid('''
graph LR;
    A --> B;
    A --> C;
''')

ui.html('This is a <strong>HTML </strong> message')

ui.run()