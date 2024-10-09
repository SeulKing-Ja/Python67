arrival = [900, 1000]
departure = [1000, 1100]

station_used = 0

            

if len(arrival) > 0:
    station_used += 1
if len(arrival) > 1:
    for i in range(len(arrival)):
        if i < len(arrival) - 1 and departure[i] >= arrival[i+1] and arrival[i] > arrival[i+1]:
            station_used += 1
            if station_used == 3:
                break

print(station_used)

    