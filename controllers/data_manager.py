from models.province_model import Province
from models.county_model import County
from models.commune_model import Commune
from models.units_model import Units
import csv


def load_database():
    '''
    Creates object of Units class and loads database from malopolska.csv to
    lists as objects of Province, County and Commune classes.
    '''
    WOJ = 0
    POW = 1
    GMI = 2
    RGMI = 3
    NAZWA = 4
    TYP = 5

    malopolska = Units()

    with open('database/malopolska.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')

        for item in reader:
            # appends province to list if 'powiat' is blank
            if item[POW] == '':
                malopolska.provinces.append(Province(item[NAZWA],
                                                     item[TYP],
                                                     item[WOJ]))
            # appends county to list if 'gmina' is blank
            elif item[GMI] == '':
                malopolska.counties.append(County(item[NAZWA],
                                                  item[TYP],
                                                  item[WOJ],
                                                  item[POW]))
            # appends communes to list, excludint title line
            elif item[WOJ] != 'woj':
                malopolska.communes.append(Commune(item[NAZWA],
                                                   item[TYP],
                                                   item[WOJ],
                                                   item[POW],
                                                   item[GMI],
                                                   item[RGMI]))

    print("liczba województw w bazie: {}".format(len(malopolska.provinces)))
    print("liczba powiatów w bazie: {}".format(len(malopolska.counties)))
    print("liczba gmin w bazie: {}".format(len(malopolska.communes)))
