# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line


def create_passport(name, birth, place, height, nationality):

    dict = {
        'name': name,
        'date_of_birth': birth,
        'place_of_birth:': place,
        'height': height,
        'nationality': nationality
    }

    return dict


countries = get_countries()
portugal = [country for country in countries if 'Portugal' in country]


print(create_passport('Rómulo',
                      '1978-11-23',
                      'Lavos - Figueira da Foz',
                      1.80,
                      portugal[0]))
