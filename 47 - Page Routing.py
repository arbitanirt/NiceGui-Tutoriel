from nicegui import ui

@ui.page('/login')
def login_page():
    ui.query('body').style('background-color:#c6ff7c')
    ui.label('Welcome to login Form!')
    usename = ui.input('Username')
    password = ui.input('Password')
    login_button = ui.button('Login')

@ui.page('/signup')
def signup_page():
    ui.query('body').style('background-color:#c6ff7c')
    usename = ui.input('Username')
    password = ui.input('Password')
    signup_button = ui.button('Signup')



ui.link('Visit Login Form', login_page)
ui.link('Visit Signup Form', signup_page)






ui.run()