from flask import Flask, render_template
import json
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/distrib/', methods=['POST'])
def distrib():
    with open('rzd_ds_t1.json', encoding='utf-8') as file:
        data = json.load(file)
    stations = list(map(lambda x: x.split()[0], data['stations'].keys()))
    trains = data['full_timetable']
    for train in trains:
        trains[train]['route'] = list(map(int, trains[train]['route']))
    count_stations = {}
    for num_train, info_train in trains.items():
        count_stations[num_train] = len(info_train['route'])


    rows = len(trains)
    columns = 7
    depth = 7

    # Создайте многомерный массив с указанными размерами
    array = [[[random.randint(1, 9) for _ in range(columns)] for _ in range(depth)] for _ in range(rows)]

    out = array
    pick_wag = {}
    for i, train in enumerate(trains):
        count_add_wag = []
        for route in trains[train]['route']:
            station_add = []
            for j, count in enumerate(out[i][route - 1]):
                if count:
                    station_add.append(stations[j] + ' +' + str(count))
            count_add_wag.append(', '.join(station_add))
        pick_wag[train] = count_add_wag
            


    context = {
        'stations': stations,
        'trains': trains,
        'count_stations': count_stations,
        'pick_wag': pick_wag,
    }
    return render_template('./distrib-wag.html', **context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
