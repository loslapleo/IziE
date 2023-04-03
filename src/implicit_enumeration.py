# Array containing the original model for the current problem.
model = []
# Current number of subs.
sub_counter = 0
# Root of the binary tree of subs (master sub).
root_sub = []

# Binary tree containing all subs that have been calculated.
class Sub:
    # Initialises sub object.
    def __init__(self, sub, iterateable):
        self.left = None
        self.right = None
        self.sub = sub
        self.iterateable = iterateable

    # Sets iterateable to false.
    def setNotIterateable(self):
        self.iterateable = False

    # Returns the sub.
    def getSub(self):
        return self.sub

    # Returns left sub.
    def getLeftSub(self):
        if self.left:
            return self.left
        else:
            return None
    
    # Returns right sub.
    def getRightSub(self):
        if self.right:
            return self.right
        else:
            return None

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

    # Gets the best sub that is currently in the list of all current subs.
    def getBestSub(self):
        best = None
        if (self.iterateable):
            best = self
        if self.left:
            temp = self.left.getBestSub()
            if best == None:
                best = temp
            elif temp != None and \
                    temp.getSub()[1] > best.getSub()[1] and \
                    temp.getIterateable():
                best = temp
        if self.right:
            temp = self.right.getBestSub()
            if best == None:
                best = temp
            elif temp != None and \
                    temp.getSub()[1] > best.getSub()[1] and \
                    temp.getIterateable():
                best = temp
        return best

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
    global root_sub
    model = arr
    iteration = 0
    print(model)

    print("\nIteration {}:".format(iteration))
    iteration += 1
    master = getMaster()
    root_sub = Sub(master, True)
    root_sub.printSubs()

    while (root_sub.getIterateableAmount() > 0):
        print("\nIteration {}:".format(iteration))
        iteration += 1
        best_sub = root_sub.getBestSub()
        generateSubs(best_sub)
        root_sub.printSubs()

    generateOutput()

# Returns:
# <0> if feasibility might exist in oncoming solutions.
# <1> if candidate solution.
def isFeasible(arr):
    global model
    output = 0
    passed = 0

    for i in range(len(model) - 1):
        t = 0
        z = model[i + 1][len(arr)]

        for j in range(len(arr)):
            t += arr[j] * model[i + 1][j]

        if t <= z:
            passed += 1

    if passed == len(model) - 1:
        output = 1
    else:
        output = 0

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

# Generates the left and right sub of the given sub in the format <[<index>,
# <z>, <# fixed variables>, [<binary values>]]>.
def generateSubs(sub):
    global model
    global sub_counter
    sub.setNotIterateable()
    current_sub = sub.getSub()
    left_sub = []
    right_sub = []

    left_sub.append(sub_counter)
    sub_counter += 1
    right_sub.append(sub_counter)
    sub_counter += 1

    left_z = 0
    left_fixed = current_sub[2] + 1
    left_binary = current_sub[3].copy()
    left_binary[current_sub[2]] = 0
    right_z = 0
    right_fixed = current_sub[2] + 1
    right_binary = current_sub[3].copy()
    right_binary[current_sub[2]] = 1

    for i in range(len(model[0])):
        left_z += left_binary[i] * model[0][i]
        right_z += right_binary[i] * model[0][i]

    left_sub.append(left_z)
    left_sub.append(left_fixed)
    left_sub.append(left_binary)
    right_sub.append(right_z)
    right_sub.append(right_fixed)
    right_sub.append(right_binary)

    if (left_fixed == len(left_binary)):
        left_iterateable = False
    else:
        left_iterateable = isFeasible(left_sub[3]) != 1
    if (right_fixed == len(right_binary)):
        right_iterateable = False
    else:
        right_iterateable = isFeasible(right_sub[3]) != 1
    sub.insertLeftSub(left_sub, left_iterateable)
    sub.insertRightSub(right_sub, right_iterateable)

# Generates binary tree as output that can be used in Mermaid.
def generateOutput():
    global root_sub
    file = open("out/output1.txt", "w")
    file.write("Copy the following text to the Mermaid website:\n\n")
    file.write("flowchart TD\n")

    output = "\t{}(Master\\nz = {}\\n{})\n".format( \
            root_sub.getSub()[0], \
            root_sub.getSub()[1], \
            arrayToString(root_sub.getSub()[3]))
    file.write(output)
    writeSubs(file, root_sub)

    file.close()

# Writes all subs after master to output file.
def writeSubs(file, current_sub):
    if (current_sub.getLeftSub()):
        output = "\t{} --> {}(Sub {}\\nz = {}\\n{})\n".format( \
                current_sub.getSub()[0], \
                current_sub.getLeftSub().getSub()[0], \
                current_sub.getLeftSub().getSub()[0], \
                current_sub.getLeftSub().getSub()[1], \
                arrayToString(current_sub.getLeftSub().getSub()[3]))
        file.write(output)
        writeSubs(file, current_sub.getLeftSub())
    if (current_sub.getLeftSub()):
        output = "\t{} --> {}(Sub {}\\nz = {}\\n{})\n".format( \
                current_sub.getSub()[0], \
                current_sub.getRightSub().getSub()[0], \
                current_sub.getRightSub().getSub()[0], \
                current_sub.getRightSub().getSub()[1], \
                arrayToString(current_sub.getRightSub().getSub()[3]))
        file.write(output)
        writeSubs(file, current_sub.getRightSub())

# Turns binary array into string for output.
def arrayToString(arr):
    output = ""
    for i in range(len(arr)):
        output += str(arr[i]) + " "
    return output
