model = []

def implicitEnumeration(arr):
    global model
    model = arr
    printModel()

# Returns:
# - -1 if error
# - 0 if no feasible completion
# - 1 if there might be feasible completion after this iteration
# - 2 if candidate solution
def isFeasible():
    return -1

# Prints model
def printModel():
    # TODO: do this better
    global model
    for row in model:
        print(row)
