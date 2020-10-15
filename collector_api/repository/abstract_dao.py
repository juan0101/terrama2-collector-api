from collector_api.ext.database import db

def get_all(table_name):
    response = db.engine.execute('select * from public.'+table_name)
    for r in response:
        first = r[0]
        second = r[1]
        tres = r[2]
    return response