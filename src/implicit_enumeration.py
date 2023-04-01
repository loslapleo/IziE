# Array containing the original model for the current problem.
model = []
# Current number of subs.
sub_counter = 0

# Binary tree containing all subs that have been calculated.
class Sub:
    # Initialises sub object.
    def __init__(self, sub, iterateable):
        self.left = None
        self.right = None
        self.sub = sub
        self.iterateable = iterateable

    # Returns the sub.
    def getSub(self):
        return self.sub

    # Returns if sub iterateable.
    def getIterateable(self):
        return self.iterateable

    # Gets the amount of iterateable subs after and including this sub.
    def getIterateableAmount(self):
        amount = 0
        if self.iterateable:
            amount += 1
        if self.left:
            amount += self.left.getIterateableAmount()
        if self.right:
            amount += self.right.getIterateableAmount()
        return amount

    # Inserts left sub object.
    def insertLeftSub(self, sub, iterateable):
        self.left = Sub(sub, iterateable)
    
    # Inserts left sub object.
    def insertRightSub(self, sub, iterateable):
        self.right = Sub(sub, iterateable)

    # Prints current sub and all its children.
    def printSubs(self):
        print("{} {}".format(self.iterateable, self.sub))
        if self.left:
            self.left.printSubs()
        if self.right:
            self.right.printSubs()

# Main function to be called by other files.
def implicitEnumeration(arr):
    global model
    model = arr
    iteration = 0
    print(model)

    print("\nIteration {}:".format(iteration))
    iteration += 1
    master = getMaster()
    rootSub = Sub(master, True)
    rootSub.printSubs()

    print("\nIteration {}:".format(iteration))
    iteration += 1
    arr = getSubs(rootSub.getSub())
    rootSub.insertLeftSub(arr, True)
    arr = getSubs(rootSub.getSub())
    rootSub.insertRightSub(arr, False)
    rootSub.printSubs()

# Returns:
# <-1> if error.
# <0> if no feasible completion.
# <1> if feasibility might exist in oncoming solutions.
# <2> if candidate solution.
def isFeasible(arr):
    global model
    output = 2

    for i in range(len(model) - 1):
        t = 0
        z = 0

        for j in range(len(arr)):
            t += arr[j] * model[i + 1][j]
            z = model[i + 1][j + 1]

        if t > z:
            if output == 2:
                output = 0
        else:
            if output == 0:
                output = 1

    return output

# Gets master solution in form <[<index>, <z>, <# fixed variables>,
# [<binary values>]]>. Should only be called once before all other subs are
# calculated.
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

# Generates the left and right sub of the given solution in the format
# <[<index>, <z>, <# fixed variables>, [<binary values>]]>.
def getSubs(arr):
    global sub_counter
    sub = [sub_counter]
    sub_counter += 1
    return sub
