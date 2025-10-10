from math import sqrt
from pprint import pprint
from datetime import timedelta
from math import sqrt
import sys
import csv

class Horse():
    path: str = ''
    name: str = None
    sex: str = None
    dist: int = 0
    pilot: str = None
    gains: int = None
    cote: float = 0
    record: timedelta = timedelta()
    last_perf: list = []

    def __str__(self):
        return f'{self.name}'

    def parse_csv(self) -> list:
        with open(self.path, newline='') as csv_file:
            starter_pack = []
            content = csv.reader(csv_file)

            for row in content:
                sprinter = Horse(
                    self.path,
                    row["name"],
                    row["sex"],
                    row["dist"],
                    row["pilot"],
                    row["gains"],
                    row['cote']
                )
                record = row["record"].strip("'")
                sprinter.record = timedelta(
                    minutes=record[0], 
                    seconds=record[1], 
                    milliseconds=record[2]
                )

                last_perf = row["last_perf"].strip(' ')
                sprinter.last_perf = last_perf

                starter_pack += sprinter

        return starter_pack


def ecart_type(data: list[float], type: int) -> float:
    moy = sum(data) / len(data)
    diff_moy = [(moy-x)**2 for x in data]
    if type == 1:
        result = sqrt(sum(diff_moy) / len(data))
    else:
        result = sqrt(sum(diff_moy) / (len(data))-1)
    return round(result, 10)

def sum_squared(data: list[float]) -> float:
    return sum([d**2 for d in data])

def variance(e_type: float) -> float:
    return e_type**2

def main(path=sys.argv[1]):
    all_horse_result = []
    result = dict()
    parent_horse = Horse(path=path)
    head = parent_horse.parse_csv()

    for horse in head:
        current = [horse.age, horse.dist, horse.gains, horse.cote]
        float_current = [float(x) for x in current]

        result['moyenne'] = sum(float_current) / 4
        result['sum'] = sum(float_current)
        result['ecart_type'] = ecart_type(float_current, 0)
        result['ecart_type2'] = ecart_type(float_current, 1)

        all_horse_result += result

    all_output = []
    for horse_result in all_horse_result:
        output = horse_result['moyenne'] / horse_result['sum']
        output /= horse_result['ecart_type']
        output /= horse_result['ecart_type2']
        output += all_output
    
    pprint(all_output)