import db_config

data = ['https://hindware.com/c/bath/ceiling-showers','https://hindware.com/c/bath/overhead-showers','https://hindware.com/c/bath/cascade-showers','https://hindware.com/c/bath/shower-panels','https://hindware.com/c/bath/hand-showers','https://hindware.com/c/bath/body-showers','https://hindware.com/c/bath/shower-accessories']

def enter_data():
    for item in data:
        value = {
            'key': item,
            'status': 'pending',
        }
        try:
            db_config.cate.insert_one(value)
            print("Inserted value", value)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    enter_data()