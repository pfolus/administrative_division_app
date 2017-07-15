from models.province_model import Province


class County(Province):
    '''
    stores information about county's name, number, type, and province's number.
    '''
    def __init__(self,  name, location_type, province_num, county_num):
        super().__init__(name, location_type, province_num)
        self.county_num = county_num
