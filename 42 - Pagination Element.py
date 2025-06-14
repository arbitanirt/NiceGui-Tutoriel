from nicegui import ui

image = ui.image('ronaldo.jpg').classes('w-40')
text = ui.label('''Cristiano Ronaldo dos Santos Aveiro, 
couramment appelé Cristiano Ronaldo ou Ronaldo et surnommé CR7, né le 5 février 1985 à Funchal, 
est un footballeur international portugais qui évolue au poste d'attaquant au Al-Nassr FC.''')

p = ui.pagination(1,3, direction_links=True, on_change=lambda : show())


def show():
    if p.value == 1:
        image.set_source('ronaldo.jpg')
        text.set_text('''Cristiano Ronaldo dos Santos Aveiro, 
        couramment appelé Cristiano Ronaldo ou Ronaldo et surnommé CR7, né le 5 février 1985 à Funchal, 
        est un footballeur international portugais qui évolue au poste d'attaquant au Al-Nassr FC.''')

    if p.value == 2:
        image.set_source('ibrahimovic.jpg')
        text.set_text('''Zlatan Ibrahimović, né le 3 octobre 1981 à Malmö en Suède, 
        est un footballeur international suédois ayant évolué au poste d'attaquant. 
        Il est considéré comme l'un des avants-centres les plus complets au monde et l'un des meilleurs attaquants de sa génération.''')

    if p.value == 3:
        image.set_source('messi.jpg')
        text.set_text('''Lionel Messi, parfois surnommé Leo Messi, né le 24 juin 1987 à Rosario en Argentine, 
        est un footballeur international argentin jouant au poste d'attaquant à l’Inter Miami CF en MLS. 
        Il est considéré comme l'un des plus grands footballeurs de l'histoire. ''')




ui.run()