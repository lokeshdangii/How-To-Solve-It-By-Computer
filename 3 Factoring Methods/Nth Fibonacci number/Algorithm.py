n = int(input("Enter the number : "))
bin_arr = []

while n >1:
    ele = n%2
    bin_arr.append(ele)
    n = int(n/2)

# print("The array : ",bin_arr)

fn = 0
fn1 = 1
# i = len(bin_arr)
# print("lenth of array : ",i)
i = 0
while i<len(bin_arr):
    
    f2n = (fn*fn) + (fn1*fn1)
    f2n1 = 2*fn*fn1 + fn1*fn1

    if bin_arr[i] == 0:
        fn = f2n
        fn1 = f2n1
    else:
        fn = f2n1
        fn1 = f2n1 + f2n
    i =i+1
    print("The fibonacci no. : ",fn)
    
    

print("The nth fibonacci no. : ",fn)