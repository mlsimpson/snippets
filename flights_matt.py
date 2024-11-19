flights = [
    ('JFK', 'ATL'),
    ('YYZ', 'JFK'),
    ('ATL', 'HOU'),
    ('HOU', 'SFO'),
]

def find_path(f):
    flight_dict = {k: v for k, v in flights}
    o = (flight_dict.keys() - flight_dict.values()).pop()
    # d = (flight_dict.values() - flight_dict.keys()).pop()
    # print(o, d)

    path = []
    next_hop = o

    while next_hop:
        path.append(next_hop)
        next_hop = flight_dict.get(next_hop)

    return path


if __name__ == '__main__':
    print(find_path(flights))


