nums = [i for i in map(int, input().split())]

negative_nums = [x for x in nums if x < 0]
positive_nums = [x for x in nums if x not in negative_nums]

def add_code(array):

    res=[]
    for x in array:
        fill_length = len(bin(int(str(x)[1:]))[2:])
        print(fill_length)
        print(bin(x)[2:])
        x = int(bin(x)[2:].zfill(8-fill_length%8))
        print(x)
        inverse_s = x ^ (2**(len(bin(x)[2:-3])+1)-1)
        inverse_s = int(inverse_s,2) + 1
        res.append(inverse_s)
    return res

print(int("11111101",2))

print(add_code(negative_nums))