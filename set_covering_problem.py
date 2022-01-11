states_needed = set(["MT","WA","OR","ID","NV","UT","CA","AZ"])

stations = {}
stations["kONE"]= set(["ID","NV","UT"])
stations["kTWO"] = set(["ID","WA","MT"])
stations["kTHREE"] = set(["NV","OR","CA"])
stations["kFOUR"] = set(["NV","UT"])
stations["kFIVE"] = set(["CA","AZ"])
final_stations = set()

while states_needed:  #if the states needed still existts
    best_station = None 
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states #this must contain the states_needed and states from the stations
        if len(covered)>len(states_covered): #
            best_station = station
            states_covered = states
        print(states_covered)
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
#print(states_needed) #this would present :NJ in the asbsence of the loop