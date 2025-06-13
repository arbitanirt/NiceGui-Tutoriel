from nicegui import ui

with ui.tabs().classes('w-64') as tabs:
    login = ui.tab('Login')
    signup = ui.tab('Sign Up')


with ui.tab_panels(tabs, value=login).classes('w-96'):
    with ui.tab_panel(login) :
        username = ui.input('Username')
        password = ui.input('Password', password=True)
        login_button = ui.button('Login', icon='login', color='green')
    with ui.tab_panel(signup) :
        username = ui.input('Username')
        password = ui.input('Password', password=True)
        login_button = ui.button('SignUp')




ui.run()