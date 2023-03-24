model = []

# Main function to be called by other functions. Initialises global model.
def implicitEnumeration(arr):
    global model
    model = arr
    printModel()
    print(getMaster())

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

    # No answer.
    return answer

# Prints model
def printModel():
    # TODO: do this better
    global model
    for row in model:
        print(row)

def getMaster():
    global model
    master = []

    for i in range(len(model[0])):
        if model[0][i] < 0:
            master.append(-1)
        else:
            master.append(1)

    return master
