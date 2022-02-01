>>> flights = [
...     ('JFK', 'ATL'),
...     ('YYZ', 'JFK'),
...     ('ATL', 'HOU'),
...     ('HOU', 'SFO'),
... ]
>>> flight_dict = {}
>>> for departure, arrival in flights:
...     flight_dict[departure] = arrival
...
>>> departures = set(flight_dict.keys())
>>> arrivals = set(flight_dict.values())
>>> origin = next(iter(departures - arrivals))
>>> origin
'YYZ'
>>> dest = next(iter(arrivals - departures))
>>> dest
'SFO'
>>> path = []
>>> next_hop = origin
>>> while next_hop:
...     path.append(next_hop)
...     next_hop = flight_dict.get(next_hop)
...
>>> path
['YYZ', 'JFK', 'ATL', 'HOU', 'SFO']