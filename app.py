from flask import Flask, render_template, request
import json
import model

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/distrib/', methods=['POST'])
def distrib():
    page = int(request.args.to_dict().get('page'))

    f = request.files['file']
    file_content = f.read()
    bytes_value = file_content
    my_json = bytes_value.decode('utf8').replace("'", '"')
    situations = json.loads(my_json)
    count_pages = len(situations)
    situation = situations[page]

    stations = list(map(lambda x: x.split()[0], situation['stations'].keys()))
    trains = situation['full_timetable']
    for train in trains:
        trains[train]['route'] = list(map(int, trains[train]['route']))
    count_stations = {}
    for num_train, info_train in trains.items():
        count_stations[num_train] = len(info_train['route'])

    array = model.get_loading_wag_by_state(situation)

    out = array
    pick_wag = {}
    no_used_trains = []
    for i, train in enumerate(trains):
        count_add_wag = []
        for route in trains[train]['route']:
            station_add = []
            for j, count in enumerate(out[i][route - 1]):
                if int(count.item()):
                    station_add.append(stations[j] + ' +' + str(int(count.item())))
            count_add_wag.append(', '.join(station_add))
        if count_add_wag ==  [''] * len(trains[train]['route']):
            no_used_trains.append(train)
        pick_wag[train] = count_add_wag
            


    context = {
        'page': page,
        'count_pages': count_pages,
        'stations': stations,
        'trains': trains,
        'count_stations': count_stations,
        'pick_wag': pick_wag,
        'no_used_trains': no_used_trains,
    }
    return render_template('./distrib-wag.html', **context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
