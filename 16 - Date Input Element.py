from nicegui import ui
import datetime

first_date = ui.date(value='2000-01-01' , on_change=lambda:calculate())

def calculate():
    first_date_value = first_date.value
    current_date = str(datetime.datetime.now())

    t1 = datetime.datetime(year=int(first_date_value[0:4]),
                           month=int(first_date_value[5:7]),
                           day=int(first_date_value[8:10]))

    t2 = datetime.datetime(year=int(current_date[0:4]),
                           month=int(current_date[5:7]),
                           day=int(current_date[8:10]))

    label.set_text(str(t2-t1)[:-9])

label = ui.label('Arbi Code')




ui.run()