import json

import torch
import torch.nn as nn
import torch.nn.functional as F

class DistributionModel(nn.Module):
    def __init__(self):
        super(DistributionModel, self).__init__()

        self.conv1T = nn.Conv1d(7, 1, 3, padding=3)
        self.conv1S = nn.Conv1d(7, 5, 3, padding=2)

        self.conv2 = nn.Conv1d(1, 5, 5, padding=2)
        self.conv3 = nn.Conv1d(5, 7, 5, padding=1)


    def forward(self, inputT, inputS):
        xT = F.relu(self.conv1T(inputT))
        xS = F.relu(self.conv1S(inputS))
        x = (xT @ xS)
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))

        return x
    
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device('cpu')

model = DistributionModel().to(device)
checkpoint = torch.load('model_cp_1.pth', map_location=device)
model.load_state_dict(checkpoint)

def get_loading_wag_by_state(situations):
    all_trains_info = []
    all_stations_info = []
    situations_data = []
    for situation in situations:
        trains_info = []
        for train in situation['full_timetable'].values():
            train_info = [[0] for _ in range(7)]
            route = list(map(int, train['route']))
            free_carriage = list(map(int, train['free_carriage'])) + [0]
            for i in range(len(route)):
                train_info[route[i] - 1] = [free_carriage[i]]
            trains_info.append(train_info)

        stations_info = []
        for station in situation['stations'].values():
            stations_info.append(list(map(int, station)))

        situations_data.append((torch.tensor(trains_info, dtype=torch.float32), torch.tensor([stations_info], dtype=torch.float32)))

    return torch.round(model(situations_data[0][0].to(device), situations_data[0][1].to(device)))