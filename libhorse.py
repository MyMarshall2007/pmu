from math import sqrt
from pprint import pprint
from datetime import timedelta
import pandas as pd
import sys
import csv

class Horse():
    def __init__(self, path, number, age, dist, gains, cote):
        self.path = path
        self.number = number
        self.age = age
        self.dist = dist
        self.gains = gains
        self.cote = cote

    def __str__(self):
        return f'{self.name}'
    

def excel_to_csv(path) -> None:
    read_file = pd.read_excel(path)
    read_file.to_csv("static/output.csv", index=None, header=True)
    

def parse_csv(path: str) -> list:
    with open(path, newline='') as csv_file:
        starter_pack = []
        content = csv.reader(csv_file)

        for i, row in enumerate(content, 0):
            if i == 0:
                continue

            sprinter = Horse(
                path=path,
                number=i,
                age=row[1],
                dist=row[2],
                gains=row[3],
                cote=row[4]
            )
            
            starter_pack.append(sprinter)

    return starter_pack


def ecart_type(data: list[float], type: int) -> float:
    moy = sum(data) / len(data)
    diff_moy = [(moy-x)**2 for x in data]
    if type == 1:
        result = sqrt(sum(diff_moy) / len(data))
    else:
        result = sqrt(sum(diff_moy) / (len(data))-1)
    return result


def sum_squared(data: list[float]) -> float:
    return sum([d**2 for d in data])


def main(path_to_xcl=sys.argv[1]):
    excel_to_csv(path_to_xcl)
    path = './static/output.csv'
    all_horse_result = []
    result = dict()
    head = parse_csv(path)

    for horse in head:
        current = [horse.age, horse.dist, horse.gains, horse.cote]
        float_current = [float(x) for x in current]

        result['moyenne'] = sum(float_current) / 4
        result['sum'] = sum(float_current)
        result['sum_squared'] = sum_squared(float_current)
        result['ecart_type'] = ecart_type(float_current, 0)
        result['ecart_type2'] = ecart_type(float_current, 1)
        result['dist'] = float(horse.dist)

        all_horse_result.append(result)

    all_output = []
    for horse_result in all_horse_result:
        output = horse_result['moyenne'] / horse_result['sum']
        output /= horse_result['sum_squared']
        output /= horse_result['ecart_type']
        output /= horse_result['ecart_type2']

        division_list = dict()

        a = output                  ; division_list['a'] = a
        b = a / result['dist']      ; division_list['b'] = b
        A = b / a                   ; division_list['A'] = A
        c = A / a 
        d = c / a                   ; division_list['d'] = d 
        e = d / A                   ; division_list['e'] = e
        f = e / a                   ; division_list['f'] = f
        g = f /b                    ; division_list['g'] = g
        h = g /e                    ; division_list['h'] = h
        i = h / e
        j = i / e                   ; division_list['j'] = j
        k = j / e                   ; division_list['k'] = k

        all_output.append(division_list)

    for out in all_output:
        pprint(out)
        print('\n')