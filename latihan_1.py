arrayList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
def lamps(a):
    count_1 = 0
    count_2 = 0 
    
    flag = True

    for number in a:
        if flag:
            if number == 1:
                count_1 += 1
            if number == 0:
                count_2 += 1
            flag = False
        else: 
            if number == 1:
                count_2 += 1
            if number == 0:
                count_1 += 1  
            flag = True


    return min(count_1, count_2)

lamps(arrayList) 

