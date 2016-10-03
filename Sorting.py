arr = []
Qmoves = []
Bmoves = []
BBmoves = []

def analyze():
    length = len(Qmoves)
    print("Qsort\tBubble\tBetterBubble")
    for i in range(length):
        print()

def permute_and_sort():
    #do something with arr
    Qmoves.append(Qsort())
    Bmoves.append(Bubble())
    BBmoves.append(BetterBubble())
    analyze()

def Bubble():
    moves = 0
    for j in range(10):
        moves = moves + 1 #for it self
        for i in range(9 - j):
            moves = moves + 2 #for itself and the if
            if (arr[i] > arr[i + 1]):
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    return moves

def Qsort():
    moves = 0
    for j in range(10):
        moves =  moves + 3 #itself, swap, breaking if
        swap = 0
        for i range(9 - j):
            moves = moves + 2 #itself, if
            if (arr[i] > arr[i + 1]):
                moves = moves + 2 #itself and swap
                swap = swap + 1
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        if (swap < 2):
            break
    return moves

def BetterBubble():
    moves = 0
    for j in range(10):
        moves = moves + 3 #itself, flag, breaking if
        flag = False
        for i in range(9 - j):
            moves = moves + 2 #itself and if
            if (arr[i] > arr[i + 1]):
                moves = moves + 2 #ifself and flag
                flag = True
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        if (not flag):
            break
    return moves

permute_and_sort()
