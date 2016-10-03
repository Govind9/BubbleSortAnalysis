arr = []
Qmoves = []
Bmoves = []
BBmoves = []

def analyze():	
    length = len(Bmoves)
    Q = B = BB = 0
    print("Qsort\tBubble\tBetterBubble")
    for i in range(length):
        print(str(Qmoves[i]) + "\t" + str(Bmoves[i]) + "\t" + str(BBmoves[i]))
	Q = Q + Qmoves[i]
	B = B + Bmoves[i]
	BB = BB + BBmoves[i]
    print(str(Q) + "\t" + str(B) + "\t" + str(BB))

def permute(x):
	arr = []
	if (len(x) == len(s)):
		p = ""
		for i in x:
			p = p + s[int(i)]
		for i in p:
			arr.append(int(i))
		#a new combination ready, sort now
		sort(arr)
	for i in range(len(s)):
		if (str(i) not in x):
			permute(x + str(i))

def sort(arr):
    a = arr
    Bmoves.append(Bubble(a))
    a = arr
    Qmoves.append(Qsort(a))
    a = arr
    BBmoves.append(BetterBubble(a))
    a = arr
    analyze()

def Bubble(arr):
    moves = 0
    for j in range(len(arr)):
        moves = moves + 1 #for it self
        for i in range(len(arr) -1 - j):
            moves = moves + 2 #for itself and the if
            if (arr[i] > arr[i + 1]):
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    return moves

def Qsort(arr):
    moves = 0
    for j in range(len(arr)):
        moves =  moves + 3 #itself, swap, breaking if
        swap = 0
        for i in range(len(arr) -1 - j):
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

def BetterBubble(arr):
    moves = 0
    for j in range(len(arr)):
        moves = moves + 3 #itself, flag, breaking if
        flag = False
        for i in range(len(arr) -1 - j):
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

s = '123456'
permute("")
