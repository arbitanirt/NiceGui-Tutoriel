from nicegui import ui

company_name = ui.input('Company Name: ')
stock_price = ui.input('Stock Price: ')

save_button = ui.button('Save', on_click=lambda:save_button())

list_company = []

chart = ui.highchart({
    'title': False,
    'chart': {'type': 'bar'},
    'xAxis': {'categories': ['Companies']},
    'series': list_company,
}).classes("w-128")

def save_button():
    new_dict = { 'name' :f'{company_name.value}', 'data':[int(stock_price.value)]}
    list_company.append(new_dict)
    chart.update()



ui.run()