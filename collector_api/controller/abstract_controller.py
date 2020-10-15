from collector_api.repository import abstract_dao
from collector_api.utils import utils

def get_all(table):

    nomes = [
        'focos_terrama2q_x19910810_1200.csv',
        'focos_terrama2q_19900214_1200.csv',
        'focos_terrama2q_19930813_1200.csv',
        'focos_terrama2q_x19900116_1200.csv',
        'focos_terrama2q_19960822_1200.csv',
        'focos_terrama2q_x19900228_1200.csv',
        'focos_terrama2q_19D70810_1200.csv',
        'focos_terrama2q_1998Y410_1200.csv',
        'focos_terrama2q_19901010_1200.csv',
    ]

    mascara = 'focos_terrama2q_%YYYY%MM%DD_%hh%mm.csv'

    nomes_validos = []

    for nome in nomes:
        isvalid = utils.validate_mask(nome, mascara)
        if(isvalid):
            nomes_validos.append(nome)
    
    #for nome_valido in nomes_validos:
        #print(nome_valido)
    
    utils.test_validate_date()

    result = abstract_dao.get_all(table)
    print(result)
    return result