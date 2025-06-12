from nicegui import ui

name = ui.input("Enter your name: ")
age = ui.input("Enter your age: ")

save = ui.button("Save", on_click=lambda:save())

columns = [
    {'label': 'Name', 'field': 'name'},
    {'label': 'Age', 'field': 'age'},
]

rows = []

def save():
    new_dict = {'name': f'{name.value}', 'age': f'{age.value}'}
    rows.append(new_dict)
    table.update()
    name.value = ""
    age.value = ""

table = ui.table(rows=rows, columns=columns)



ui.run()