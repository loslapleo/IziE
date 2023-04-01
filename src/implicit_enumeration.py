# The original model for problem.
model = []
# Array of all subs that have been calculated so far.
all_subs = []
# Array of subs in form; [<index>, <z>, [<values locked?>], [<binary values>]],
# that can be iterated on.
available_subs = []
# Current number of sub answers.
sub_counter = 0

# Main function to be called by other functions. Initialises global model.
def implicitEnumeration(arr):
    global model
    global available_subs
    model = arr
    print("MODEL:")
    printModel()
    print("\n----------------------------------------------------------------\n")
    master = getMaster()
    all_subs.append(master)
    available_subs.append(master)
    iteration = 0; # TODO temp
    while len(available_subs) > 0 and iteration < 5:
        iteration += 1
        max_z = available_subs[0][1]
        max_index = 0
        # Finds the the sub with the maximum z value.
        for i in range(len(available_subs)):
            if available_subs[i][1] > max_z:
                max_z = available_subs[i][1]
                max_index = i
        # Gets the left and right sub of sub.
        left_sub = getSub(available_subs[max_index], 0)
        right_sub = getSub(available_subs[max_index], 1)
        # Adds those subs to list of available subs.
        if len(left_sub) > 0:
            all_subs.append(left_sub)
            available_subs.append(left_sub)
        if len(right_sub) > 0:
            all_subs.append(right_sub)
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
# [<index>, <z>, <values locked>, [<binary values>]]. Call this function only
# once before any subs are calculated.
def getMaster():
    global model
    global sub_counter
    master = []
    binary = []
    z = 0
    for i in range(len(model[0])):
        if model[0][i] < 0:
            binary.append(0)
        else:
            binary.append(1)
            z += model[0][i]
    master.append(sub_counter)
    sub_counter += 1
    master.append(z)
    master.append(0)
    master.append(binary)
    return master

# Gets the left (side = 0) or right (side = 1) sub of given solution in the form
# [<index>, <z>, <values locked>, [<binary values>]]
def getSub(arr, side):
    # TODO do this functions
    sub = []
    add_sub = False
    feasible = isFeasible(arr[3])
    # Not a feasible solution and no solution after this solution.
    if feasible == -1:
        print("Error")
        # TODO stop program
    # Not a feasible solution and no solution after this solution.
    if feasible == 0:
        # TODO write to output but keep sub empty
        print("feasible: 0")
        add_sub = True
    # Not a candidate soltution but could contain a candidate solution after
    # this solution.
    elif feasible == 1:
        # TODO
        print("feasible: 1")
        add_sub = True
    # Candidate solution.
    elif feasible == 2:
        # TODO
        print("feasible: 2")
        add_sub = True
    # TODO add sub to all_subs if necessary
    return sub
