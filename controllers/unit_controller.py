from controllers import data_manager
from models.units_model import Units
from views import units_view


def start_controller():
    try:
        malopolska = data_manager.load_database()
    except FileNotFoundError:
        units_view.print_file_not_found()
        return None

    choice = ''
    while choice != '0':
        units_view.show_menu()
        choice = units_view.get_choice()
        if choice == '1':
            table = malopolska.get_statistics()
            title_list = ['', 'MAŁOPOLSKIE']
            units_view.print_table(table, title_list)
        elif choice == '2':
            units_view.display_longest_name_cities(malopolska)
        elif choice == '3':
            units_view.display_largest_counties(malopolska)
        elif choice == '4':
            units_view.display_multicategory_locations(malopolska)
        elif choice == '5':
            phrase = units_view.get_phrase()
            score_table = search_for_phrase(phrase, malopolska)
            headers = ['LOCATION', 'TYPE']
            if score_table != []:
                units_view.print_found(score_table)
                units_view.print_table(score_table, headers)
            else:
                units_view.print_not_found()
        elif choice != '0':
            units_view.print_bad_choice()


def search_for_phrase(phrase, malopolska):
    '''
    searching for phrase in lists, and if finds it returns a table
    made of name and a type of location

    Args:
    - phrase = string
    - malopolska = obj of Units class

    Returns:
    - table = nested list
    '''
    table = []
    for unit in malopolska.provinces + malopolska.counties + malopolska.communes:
        if phrase in unit.name:
            table.append([unit.name, unit.location_type])
    table.sort(key=lambda x: (x[0], x[1]))
    return table
