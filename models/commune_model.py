from models.county_model import County


class Commune(County):
    '''
    Stores information about communes details
    '''
    def __init__(self,  name, location_type, province_num, county_num, commune_num, commune_type):
        super().__init__(name, location_type, province_num, county_num)
        self.commune_num = commune_num
        self.commune_type = commune_type
