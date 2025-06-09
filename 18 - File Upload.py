from nicegui import ui, events

def uploads(e:events.UploadEventArguments):
    text = e.content.read().decode('utf-8')
    markdown.set_content(text)

ui.upload(on_upload=uploads, on_rejected=lambda:ui.notify('Only text file accepted!')).props("accept=.txt").classes("max-w-full")

markdown = ui.markdown('Choose a text file!')


ui.run()