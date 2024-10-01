import datetime as dt
from decimal import Decimal

goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': dt.datetime(2023, 7, 15).date()},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': dt.datetime(2023, 8, 1).date()},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}

DATE_FORMAT = '%Y-%m-%d'

def add(items, title, amount, expiration_date = None):

    if title not in items:
        items[title] = []
    if expiration_date is None:
        items[title].append({'amount': amount, 'expiration_date': expiration_date == None})
    else:
        expiration_date = dt.datetime.strptime(expiration_date, DATE_FORMAT).date()
        items[title].append({'amount': amount, 'expiration_date': expiration_date})
        
   
#add(goods, 'Пельмени Универсальные', Decimal('12.1'), '2023-10-28')
#print(goods)

def add_by_note(items, note):
    split_note = str.split(note, ' ')

    if len(str.split(split_note[-1], '-')) == 3:
        expiration_date = split_note[-1]
        amount = Decimal(split_note[-2])
        title = str.join(' ', split_note[0: -2])
    else:
        amount = Decimal(split_note[-1])
        title = str.join(' ', split_note[0: -1])
        expiration_date = None

    add(items, title, amount, expiration_date)

#add_by_note(goods, 'Яйца гусиные 4 2023-07-15')
#print(goods)

def find(items, needle):
    search = []

    for titl in items:
        if needle.lower() in titl.lower():
            search.append(titl)
    return search

a = find(goods, 'вод')
#print(a)

def amount(items, needle):
    find_items = find(items, needle)
    count = Decimal('0')
    for item in find_items:
