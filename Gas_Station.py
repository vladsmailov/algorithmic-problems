gas = [1,2,3,4,5] # How much gas you'll get on each gas station
cost = [3,4,5,1,2] # How much gas you'll spend to trevel to the next station (by index)
gas2 = [2, 4, 2]
cost2 = [3, 4 ,4]
def trevel(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    gas_tank = 0
    start = 0
    for index in range(len(gas)):
        gas_tank += gas[index] - cost[index]
        if gas_tank < 0:
            gas_tank = 0
            start = index + 1
    return start

print(trevel(gas, cost))