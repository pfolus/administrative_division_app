from collections import Counter


class Units:
    '''
    Stores list of provinces, counties, and communes
    '''

    def __init__(self):
        self.provinces = []
        self.counties = []
        self.communes = []

    def get_county_with_most_communes_num(self):
        '''
        iterater through counties list, and returns name of the county
        with the largest commune_num

        Returns:
        - county = obj of County class
        '''
        for county in self.counties:
            if county.county_num == self.get_commune_with_max_num():
                return county

    def get_commune_with_max_num(self):
        '''
        iterates through communes, searching for the commune with max number.
        Returns number of county.

        Returns:
        - commune_with_max_num.county_num = int
        '''
        commune_with_max_num = self.communes[0]
        for item in self.communes:
            if item.commune_num >= commune_with_max_num.commune_num:
                commune_with_max_num = item

        return commune_with_max_num.county_num

    def get_cities_with_longest_names(self, number=3):
        '''
        Returns a number of cities with a longest names.

        Args:
        - number = int (default=3)

        Return:
        - cities_list[:number] = list of strings
        '''
        cities_list = []
        for commune in self.communes:
            if commune.location_type == 'miasto':
                cities_list.append(commune.name)

        cities_list.sort(key=lambda item: len(item), reverse=True)

        return cities_list[:number]

    def get_statistics(self):
        '''
        iterates through lists of provinces , counties and communes, and extract their
        type names to location_types list. Then counts occurencies of each type, and makes
        dictionary out of it. Then creates a list, and appends each dictionary key-value
        to that list.

        Return:
        - location_types_dict = nasted list
        '''
        location_types = []
        for unit in self.provinces + self.counties + self.communes:
            location_types.append(unit.location_type.rstrip())

        location_types_dict = dict(Counter(location_types))

        location_types_sorted = []
        for key, value in location_types_dict.items():
            location_types_sorted.append([value, key])
            location_types_sorted.sort()

        return location_types_sorted

    def get_locations_dict(self):
        '''
        iterates through lists of provinces, counties and communes, and extract names of locations.
        Then returns a dictionary in which key = name of location, and value = number of occurencies
        of that location (number of categories it occurs in)

        Returns:
        - location_names_dict = dictionary
        '''
        location_names = []
        for unit in self.provinces + self.counties + self.communes:
            location_names.append(unit.name)

        location_names_dict = dict(Counter(location_names))

        return location_names_dict
