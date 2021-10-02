'''
@Author 28Pollux28
Calculates the next number in the look_and_say sequence for any number.
'''


def main(n):
    print(int(next(str(n))))

def next(string):
    next = ''
    i=0
    while i <=len(string) - 1:
        char = string[i]
        localcount = 1
        j = 0
        while i + j + 1 < len(string) and string[i + j + 1] == char:
            localcount += 1
            j += 1
        next += str(localcount) + char
        i+=localcount
    return next


if __name__ == '__main__':
    n= int(input("Number ?"))
    main(n)