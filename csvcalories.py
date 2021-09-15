# Calorie Counting Project using CSV files


import datetime
import os
import csv


def table_of_file(filename):
    with open(filename) as c:
        r = csv.reader(c)  # read csv data
        next(r)            # skip the row of column names
        table = {}
        for row in r:
            table[row[0]] = row[1:]   # load a row's key and values
        return table


def list_foods():
    for k, vs in table_of_file('calories.txt').items():
        print(k, end=' ')
        for v in vs:
            print(v, end=' ')
        print('')


def list_eaten(name, date):
    for k, vs in table_of_file(os.path.join(name, date) + '.csv').items():
        print(f'{k} {vs[0]}')


def list_weights(name):
    for k, vs in table_of_file(os.path.join(name, 'weight.txt')).items():
        print(f'{k} {vs[0]}')


# list_weights('Helal')

def list_dates(name):
    l = os.listdir(name)
    l.sort()
    if 'weight.csv' in l:
        l.remove('weight.csv')
    for x in l:
        y = x[-len(x):-4]  # removes .txt from the end
        print(y)


# list_dates('Helal')

def lookup_calories(food):
    table = table_of_file('calories.csv')
    vs = table[food]
    if vs is None:
        print(f'Food {food} is not found')
    else:
        if len(vs) > 1:
            weight = vs[0]
            calories = vs[1]
            print(f'There are {calories} calories in {weight}g of {food}')
        else:
            print(f'Malformed calorie entry for {food} in calories file')


def lookup_weight(name, date):
    table = table_of_file(os.path.join(name, 'weight.csv'))
    if date not in table:
        print(f'Date {date} is not found')
    else:
        vs = table[date]
        if len(vs) > 0:
            weight = vs[0]
            print(f"{name}'s weight was {weight} on {date}")
        else:
            print(f'No weight found for date {date}')


# lookup_weight('Helal', '03-01-2020')

def total_date(name, date):
    calories = table_of_file('calories.csv')
    table = table_of_file(os.path.join(name, date) + '.csv')
    total = 0
    for k, vs in table.items():
        weight_and_calories = calories[k]
        reference_weight = int(weight_and_calories[0])
        reference_calories = int(weight_and_calories[1])
        calories_per_gram = reference_calories / reference_weight
        total += int(vs[0]) * calories_per_gram
    print(f'Total calories for {date}: {int(total)}')


def new_user(name):
    try:
        os.mkdir(name)
        with open(os.path.join(name, 'weight.csv'), 'w') as f:
            print('Date,Weight', file = f)
    except FileExistsError:
        print(f'The folder {name} already exists. Choose a different name')


# new_user('Mark')


def date_today():
    d = datetime.datetime.now()
    return f'{d.day:02}-{d.month:02}-{d.year}'


def eaten(name, food, grams):
    filename = os.path.join(name, date_today()) + '.csv'
    is_new = not os.path.exists(filename)
    with open(filename, 'a') as f:
        if is_new:
            print('Food,Weight', file=f)
        print(f'"{food}",{grams}', file=f)


def weighed(name, weight):
    filename = os.path.join(name, 'weight.csv')
    is_new = not os.path.exists(filename)
    with open(filename, 'a') as f:
        if is_new:
            print('Date,Weight', file-f)
        print(f'{date_today()} {weight}', file=f)

