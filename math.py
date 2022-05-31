import collections

def multiple(arg,many):
    mutiple_nums = []
    for m in range(1,many+1):
        mutiple_nums.append(arg*m)
    return mutiple_nums    


def USG(num,num1):
    num_mul = multiple(num,num1)
    num1_mul = multiple(num1,num)
    both = num_mul + num1_mul 

    similar = [item for item, count in collections.Counter(both).items() if count >  1]

    minimum = min(similar)


    return minimum


