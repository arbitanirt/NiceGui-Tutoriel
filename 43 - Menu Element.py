from nicegui import ui

with ui.row().classes('w-full items-center'):
    result = ui.label().classes('Mr-auto')
    with ui.button(icon='menu'):
        with ui.menu() as menu:
            ui.menu_item('Germany', lambda:show_germany())
            ui.menu_item('France', lambda:show_france())
            ui.menu_item('England', lambda:show_england())
            ui.separator()
            ui.menu_item('Close', on_click=menu.close)

image = ui.image('').classes('w-24')
text = ui.label('''''')


def show_germany():
    image.set_source('germany.png')
    text.set_text('''L'Allemagne est un pays d'Europe de l'Ouest dont le paysage se compose de forêts, de rivières, 
    de chaînes montagneuses et de plages sur la mer du Nord. Son histoire remonte à plus de 2 000 ans en arrière. .''')
    pass


def show_france():
    image.set_source('france.png')
    text.set_text('''La France, pays de l'Europe occidentale, compte des villes médiévales, des villages alpins et des plages. 
    Paris, sa capitale, est célèbre pour ses maisons de mode, ses musées d'art classique, dont celui du Louvre, 
    et ses monuments comme la Tour Eiffel. Le pays est également réputé pour ses vins et sa cuisine raffinée.''')
    pass


def show_england():
    image.set_source('england.png')
    text.set_text('''Angleterre, berceau de Shakespeare et des Beatles, est un pays des îles britanniques, 
    à la frontière avec l'Écosse et le Pays de Galles. Londres, sa capitale située sur la Tamise, 
    abrite le Parlement, Big Ben et la tour de Londres, qui date du XIe siècle. ''')
    pass





ui.run()