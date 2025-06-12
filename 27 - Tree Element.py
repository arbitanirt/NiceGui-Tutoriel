from nicegui import ui

topic = ui.input('Topic')
description = ui.textarea(label='Description')

save_button = ui.button('Save', icon='save', color='green', on_click=lambda:save())


dict_list = []

def save():
    new_dict = {'id': f'{topic.value}', 'description': f'{description.value}'}
    dict_list.append(new_dict)
    tree.update()

tree = ui.tree([
    {'id': 'Topic', 'description': 'description', 'children' :dict_list}
])

tree.add_slot('default-header', '''
    <span :props="props">Node <strong>{{ props.node.id}}</strong></span>
''')

tree.add_slot('default-body', '''
    <span :props="props">Description : "{{props.node.description}}"</span>
''')



ui.run()