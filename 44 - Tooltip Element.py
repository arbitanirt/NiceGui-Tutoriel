from nicegui import ui

with ui.row():
    with ui.image('germany.png').classes('w-16'):
        ui.tooltip("""L'Allemagne est un pays d'Europe de l'Ouest dont le paysage se compose de forêts, de rivières, 
    de chaînes montagneuses et de plages sur la mer du Nord. Son histoire remonte à plus de 2 000 ans en arrière.""").classes('w-48')
    with ui.image('france.png').classes('w-16'):
        ui.tooltip("""La France, pays de l'Europe occidentale, compte des villes médiévales, des villages alpins et des plages. 
    Paris, sa capitale, est célèbre pour ses maisons de mode, ses musées d'art classique, dont celui du Louvre, 
    et ses monuments comme la Tour Eiffel. Le pays est également réputé pour ses vins et sa cuisine raffinée.""").classes('w-48')
    with ui.image('england.png').classes('w-16'):
        ui.tooltip("""Angleterre, berceau de Shakespeare et des Beatles, est un pays des îles britanniques, 
    à la frontière avec l'Écosse et le Pays de Galles. Londres, sa capitale située sur la Tamise, 
    abrite le Parlement, Big Ben et la tour de Londres, qui date du XIe siècle.""").classes('w-48')




ui.run()