from collector_api.repository import abstract_dao

def get_all(table):
    result = abstract_dao.get_all(table)
    print(result)
    return result