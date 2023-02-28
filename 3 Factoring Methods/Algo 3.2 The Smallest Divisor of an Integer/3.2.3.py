def smallest_int(n):
    num = 0
    number = []

    for i in range(0,10001):
        num = num + 1
        list1 = []
        for i in range(2,num+1):
            if num%i == 0:
                list1.append(i)
        no_of_divsrs = len(list1)
        if no_of_divsrs >= n:
            print("Smallest integer that has n or more divisor : ",num)
            break

n = int(input("Enter a no. of divisors : "))
smallest_int(n)