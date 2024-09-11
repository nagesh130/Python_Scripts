import copy

def rotate(matrix):
    data = copy.depcopy(matrix)
    for i in range(len(data)):
        for j  in range(i+1, len(data[i])):
            temp = data[i][j]
            data[i][j] = data[j][i]
            data[j][i] = temp

    return data

D =[[1, 2, 3, 4],
   [4, 5, 6, 89],
   [7, 8, 9, 33]]

print(rotate)

simulation  = [[1, 2, 3], [2, 3, 4], [3, 2, 1]]

def Z_M(SIM, x, y, strength):
    for i in range(len(SIM)):
        for j in range(len(SIM[i])):
            if j != len(SIM[i])- 1:
                if SIM[i][j] <= strength:
                    SIM[i][j] = -1
    return SIM



for i in range(0,len(Z_M(simulation,0,0,2))):
        print (simulation[i])


def Does_it_count(word):
    D_words = {}
    i = 0
    while word != None:
        i+=1
        if word[i] in D_words:
            return True
        else:
            if word[i] not in D_words:
                D_words = {word[i]: +1}



print(Does_it_count('google'))








