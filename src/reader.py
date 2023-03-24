def readFromFile(file_name):
    arr = []
    with open(file_name, "r") as file:
        for line in file:
            line_words = []
            for word in line.split():
                line_words.append(word)
            arr.append(line_words)
    return arrayStrToInt(arr)

def arrayStrToInt(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = int(arr[i][j])
    return arr
