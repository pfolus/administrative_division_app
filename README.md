# know-your-neighbourhood-2017-1-pfolus

# FUNCTIONALITY


## 1. Main menu:


What would you like to do:

  (1) List statistics
  (2) Display 3 cities with longest names
  (3) Display county's name with the largest number of communities
  (4) Display locations, that belong to more than one category
  (5) Advanced search
  (0) Exit program


## CLASSES:

### Province

#### Attributes:

-name
-location_type
-province_num

#### Methods:

None

### County

### Parenting class:

Province

#### Attributes:

-name
-location_type
-province_num
-county_num

#### Methods:

None

### Commune

### Parenting class:

County

#### Attributes:

-name
-location_type
-province_num
-county_num
-commune_type
-commune_num

#### Methods:

None

### Units

### Parenting class:

None

#### Attributes:

-provinces (list of provinces)
-counties (list of counties)
-communes (list of communes)

#### Methods:

#### get_county_with_most_communes_num(self):

    iterater through counties list, and returns name of the county
    with the largest commune_num

    Returns:
    - county = obj of County class

#### get_commune_with_max_num(self):

    iterates through communes, searching for the commune with max number.
    Returns number of county.

    Returns:
    - commune_with_max_num.county_num = int

#### get_cities_with_longest_names(self, number=3):

    Returns a number of cities with a longest names.

    Args:
    - number = int (default=3)

    Return:
    - cities_list[:number] = list of strings

#### get_statistics(self):

    iterates through lists of provinces , counties and communes, and extract their
    type names to location_types list. Then counts occurencies of each type, and makes
    dictionary out of it. Then creates a list, and appends each dictionary key-value
    to that list.

    Return:
    - location_types_dict = nasted list

#### get_locations_dict(self):

    iterates through lists of provinces, counties and communes, and extract names of locations.
    Then returns a dictionary in which key = name of location, and value = number of occurencies
    of that location (number of categories it occurs in)

    Returns:
    - location_names_dict = dictionary
