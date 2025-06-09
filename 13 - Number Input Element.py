from nicegui import ui


first_number = ui.number(label='First Number', placeholder='Enter a first number')
second_number = ui.number(label='Second Number', placeholder='Enter a second number')

add_button = ui.button('+', on_click=lambda : calculate(add_button.text))
sub_button = ui.button('-', on_click=lambda : calculate(sub_button.text))
mul_button = ui.button('*', on_click=lambda : calculate(mul_button.text))
div_button = ui.button('/', on_click=lambda : calculate(div_button.text))

result = ui.label('Result : ')

def calculate(e):
    if e == '+':
        result.set_text(f'Result : {first_number.value + second_number.value}')

    if e == '-':
        result.set_text(f'Result : {first_number.value - second_number.value}')

    if e == '*':
        result.set_text(f'Result : {first_number.value * second_number.value}')

    if e == '/':
        result.set_text(f'Result : {first_number.value / second_number.value}')




ui.run()