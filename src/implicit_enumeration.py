model = []
available_subs = []
sub_counter = 0

# Main function to be called by other functions. Initialises global model.
def implicitEnumeration(arr):
    global model
    global available_subs
    model = arr
    printModel()

    available_subs.append(initMaster())
    print(available_subs)
    while len(available_subs) > 0:
        max_z = available_subs[0][1]
        max_index = 0
        for i in range(len(available_subs)):
            if available_subs[i][1] > max_z:
                max_z = available_subs[i][1]
                max_index = i
        left_sub = getLeftSub(available_subs[max_index])
        right_sub = getRightSub(available_subs[max_index])
        if len(left_sub) > 0:
            available_subs.append(left_sub)
        if len(right_sub) > 0:
            available_subs.append(right_sub)

# Returns:
# - <-1> if error
# - <0> if no feasible completion.
# - <1> if there might be feasible completion after this iteration.
# - <2> if candidate solution.
def isFeasible(arr):
    global model
    answer = 2
    for i in range(len(model) - 1):
        t = 0
        z = 0
        for j in range(len(arr)):
            t += arr[j] * model[i + 1][j]
            z = model[i + 1][j + 1]
        if t > z:
            if answer == 2:
                answer = 0
        else:
            if answer == 0:
                answer = 1
    return answer

# Prints model
def printModel():
    # TODO: do this better
    global model
    for row in model:
        print(row)

# Gets master solution in form
# [<index>, <z>, [<values locked?>], [<binary values>]]. Call this function only
# once before any subs are calculated.
def initMaster():
    global model
    global sub_counter
    master = []
    binary = []
    locks = []
    z = 0
    for i in range(len(model[0])):
        if model[0][i] < 0:
            binary.append(0)
            locks.append(0)
        else:
            binary.append(1)
            locks.append(0)
            z += model[0][i]
    master.append(sub_counter)
    sub_counter += 1
    master.append(z)
    master.append(locks)
    master.append(binary)
    return master

# Gets the left sub of given solution in the form
# [<index>, <z>, [<values locked?>], [<binary values>]]
def getLeftSub(arr):
    return arr

# Gets the right sub of given solution in the form
# [<index>, <z>, [<values locked?>], [<binary values>]]
def getRightSub(arr):
    return arr
