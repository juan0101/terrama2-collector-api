from datetime import datetime, timezone

def validate_mask(file_name, mask):
    mask_replaced = mask.replace('%','')
    if(len(file_name) == len(mask_replaced)):
        index = 0
        for letter in file_name:
            if(letter == mask_replaced[index]):
                index += 1
                continue
            if(letter.isnumeric()):
                letter_mask = mask_replaced[index]
                isvalid = True
                if(letter_mask == "Y"):
                    index += 1
                elif(letter_mask == "M"):
                    index += 1
                elif(letter_mask == "D"):
                    index += 1
                elif(letter_mask == "h"):
                    index += 1
                elif(letter_mask == "m"):
                    index += 1
                elif(letter_mask == "s"):
                    index += 1
                else:
                    isvalid = False
                
                if(isvalid):
                    continue
                else:
                    return False
            else:
                return False
        return True
    else:
        return False

def test_validate_date():
    mask = 'focos_terrama2q_%YYYY%MM%DD_%hh%mm%ss.csv'
    files = [
        'focos_terrama2q_19910214_120000.csv',
        'focos_terrama2q_19920214_120000.csv',
        'focos_terrama2q_19950117_080000.csv',
        'focos_terrama2q_19950117_100000.csv',
        'focos_terrama2q_19950117_120000.csv',
        'focos_terrama2q_19950117_130000.csv',
        'focos_terrama2q_19950117_133000.csv',
        'focos_terrama2q_19950117_140000.csv',
        'focos_terrama2q_19960214_120000.csv',
        'focos_terrama2q_19970214_120000.csv',
        'focos_terrama2q_19980214_120000.csv',
    ]

    validate_files = []

    date_compare = '1995-01-17T10:18:00.799000-03:00'

    for file_name in files:
        if(validate_date(file_name, mask, date_compare)):
            validate_files.append(file_name)
    
    print('*-------------------------------*')
    for name in validate_files:
        print(name)


#TODO comparar datas (ultima data salva no banco e data no nome do arquivo)
def validate_date(file_name, mask, last_date):
    year = ''
    month = ''
    day = ''
    hour = ''
    minute = ''
    second = ''

    #has year with 4 numbers
    if(mask.find("%YYYY") != -1):
        initial_position = mask.find("%YYYY")
        file_name = file_name[:initial_position]+'%'+file_name[initial_position:]
        year = file_name[initial_position+1:initial_position+5]
    elif(mask.find("%YY") != -1):
        initial_position = mask.find("%YY")
        file_name = file_name[:initial_position]+'%'+file_name[initial_position:]
        year = file_name[initial_position+1:initial_position+3]
    else:
        #doesn't have year
        year = str(datetime.now().year)

    if(mask.find("%MM") != -1):
        initial_position = mask.find("%MM")
        file_name = file_name[:initial_position]+'%'+file_name[initial_position:]
        month = file_name[initial_position+1:initial_position+3]
    else:
        #doesn't have month
        month = str(datetime.now().month)
    
    if(mask.find("%DD") != -1):
        initial_position = mask.find("%DD")
        file_name = file_name[:initial_position]+'%'+file_name[initial_position:]
        day = file_name[initial_position+1:initial_position+3]
    else:
        #doesn't have day
        day = str(datetime.now().day)
    
    if(mask.find("%hh") != -1):
        initial_position = mask.find("%hh")
        file_name = file_name[:initial_position]+'%'+file_name[initial_position:]
        hour = file_name[initial_position+1:initial_position+3]
    else:
        #doesn't have hour
        hour = '00'
    
    if(mask.find("%mm") != -1):
        initial_position = mask.find("%mm")
        file_name = file_name[:initial_position]+'%'+file_name[initial_position:]
        minute = file_name[initial_position+1:initial_position+3]
    else:
        #doesn't have day
        minute = '00'
        
    if(mask.find("%ss") != -1):
        initial_position = mask.find("%ss")
        file_name = file_name[:initial_position]+'%'+file_name[initial_position:]
        second = file_name[initial_position+1:initial_position+3]
    else:
        #doesn't have second
        second = '00'

    file_date = year+'/'+month+'/'+day+' '+hour+':'+minute+':'+second

    file_datetime = datetime.strptime(file_date, '%Y/%m/%d %H:%M:%S')

    last_datetime = datetime.utcfromtimestamp(datetime.fromisoformat(last_date).timestamp())

    if(file_datetime < last_datetime):
        return False
    else:
        return True

