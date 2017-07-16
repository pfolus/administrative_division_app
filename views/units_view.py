from models.units_model import Units


def show_menu():
    '''
    prints program menu
    '''
    menu = ["\nWhat would you like to do:\n",
            "(1) List statistics",
            "(2) Display 3 cities with longest names",
            "(3) Display county's name with the largest number of communities",
            "(4) Display locations, that belong to more than one category",
            "(5) Advanced search",
            "(0) Exit program\n"]

    for line in menu:
        print(line)


def print_file_not_found():
    print("File 'malopolska.csv' not found")


def get_choice():
    return input('Choose option: ')


def print_bad_choice():
    print('\nBad choice, try again: \n')


def display_longest_name_cities(malopolska):
    '''
    Args:
    - malopolska = obj of Units class
    '''
    print('\nCities with a longest name: ')
    for city in malopolska.get_cities_with_longest_names():
        print(city)


def display_largest_counties(malopolska):
    print("\nPowiat z największą liczbą gmin to powiat {}".format(malopolska.get_county_with_most_communes_num().name))


def display_multicategory_locations(malopolska):
    '''
    Displays locations that belongs to more than 1 category
    '''
    location_occurency_dict = malopolska.get_locations_dict()

    for key, value in location_occurency_dict.items():
        if value > 1:
            print("{:25} l.kategorii: {}".format(key, value))


def print_table(table, title_list):
    """
    Prints table with data.

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """
    # Appends dictionary with widest record's length
    column_widths = {}
    total_width = 0

    for i in range(len(title_list)):
        widths = []
        widths.append(len(str(title_list[i])))
        for item in table:
            widths.append(len(str(item[i])))
        max_column_width = get_max_number(widths) + 4
        column_widths["column_" + str(i)] = max_column_width
        total_width += max_column_width
    total_width += len(title_list) + 1

    # Printing
    print("/" + "-" * (total_width - 2) + "\\")
    print("|", end="")
    for i in range(len(title_list)):
        print("{:^{}}".format(title_list[i], column_widths["column_" + str(i)]), "|", end="", sep="")
    print()
    for i in range(len(table)):
        print("|", end="")
        for j in range(len(table[i])):
            print("{:-^{}}".format("", column_widths["column_" + str(j)]), "|", end="", sep="")
        print()
        print("|", end="")
        for j in range(len(table[i])):
            print("{:^{}}".format(table[i][j], column_widths["column_" + str(j)]), "|", end="", sep="")
        print()
    print("\\" + "-" * (total_width - 2) + "/")
    print()


def get_max_number(numbers):
    '''
    Takes list of strings and returns longest strings

    Args:
    -numbers = list of strings

    Returns:
    - max_number = string
    '''
    max_number = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
    return max_number


def get_phrase():
    return input('Searching for: ')


def print_not_found():
    print('\nEntered phrase not found.')


def print_found(score_table):
    print("\nFound {} location(s):\n".format(len(score_table)))
