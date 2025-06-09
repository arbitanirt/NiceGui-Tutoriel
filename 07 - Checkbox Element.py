from nicegui import ui

ui.button('SAVE', on_click=lambda : set())

def set():

    x = 0
    #print('turtle code')
    if cb_female.value == True and cb_male.value == True:
        label.set_text('You cannot choose both options')
        image_gender.set_visibility(False)
        x = 1
    if cb_female.value == False and cb_male.value == False:
        label.set_text('You must choose at least 1 option')
        image_gender.set_visibility(False)
        x = 1

    if cb_female.value == True and x == 0:
        image_gender.set_visibility(True)
        label.set_text('I am Female')
        image_gender.set_source('women.png')

    if cb_male.value == True and x == 0:
        image_gender.set_visibility(True)
        label.set_text('I am Male')
        image_gender.set_source('men.png')

image_gender = ui.image('').classes('w-32')

cb_male = ui.checkbox('Male')
cb_female = ui.checkbox('Female')

#cb_male = ui.checkbox('Male', on_change=lambda : label.set_text('Male'))
#cb_female = ui.checkbox('Female', on_change=lambda : label.set_text('Female'))

label = ui.label('Turtle Code')



ui.run()