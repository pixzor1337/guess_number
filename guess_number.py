from datetime import datetime, date, timedelta
from decimal import Decimal


DATE_FORMAT = '%Y-%m-%d'
goods = {}

def add(items, title, amount, expiration_date=None):
    if expiration_date is None:
        expiration_date = None
    else:
        expiration_date = datetime.strptime(expiration_date, DATE_FORMAT).date()
        
    if title in items:
        items[title].append({'amount':Decimal(amount), 'expiration_date':expiration_date})
    else:
        items[title] = [{'amount':Decimal(amount), 'expiration_date':expiration_date}]

add(goods, 'Пельмени Универсальные', 2, '2023-07-15')
add(goods, 'Пельмени Универсальные', 2, '2023-07-15')
add(goods, 'Пельмени Соевые', 2, '2023-07-15')
print(goods)

def add_by_note(items, note):
    parts = str.split(note, ' ')
    
    if len(str.split(parts[-1],'-')) == 3:
        expiration_date = parts[-1]
        amount = Decimal(parts[-2])
        title = str.join(' ', parts[0:-2])
    else:
        expiration_date = None
        amount = Decimal(parts[-1])
        title = str.join(' ', parts[0:-1])
    
    add(items, title, amount, expiration_date)

add_by_note(goods,  'Пельмени 4 2023-07-15')
add_by_note(goods, 'Яйца Фабрики №1 4 2023-07-15') 
add_by_note(goods, 'Молоко Отличное 1 2024-09-29')
print(goods)

def find(items, needle):
    search = []
    
    for title in items:
        if needle.lower() in title.lower():
            search.append(title)
    return search

found_items = find(goods, 'пельмени')
print(found_items)

def amount(items, needle):
    find_items = find(items, needle)
    total = Decimal(0)
    
    for item in find_items:
        for product in items[item]:
            total += product['amount']
    return total

total_1 = amount(goods, 'пельмени')
print(total_1)    


def expire(items, in_advance_days=0):
    today = date.today()
    nofresh = today + timedelta(days=in_advance_days)
    
    expired_items = []
    
    for title, batches in items.items():
        batche = Decimal(0)
        for batch in batches:
            expiration_date = batch['expiration_date']
            if expiration_date and expiration_date <= nofresh:
                batche += batch['amount']
        if batche > 0:
            expired_items.append((title, batche))

    return expired_items

expire(goods, 10)
print(expire)