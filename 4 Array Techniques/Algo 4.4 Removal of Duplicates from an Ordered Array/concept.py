Dict=  {1: 1, 2: 2, 3: 1, 4: 3, 5: 4, 6: 1, 7: 1, 8: 2, 10: 1, 14: 1, 16: 1, 18: 2, 19: 1, 20: 2}
new_arr = []
k = 2
for key, value in Dict.items():
        if value <= k:
            ele = [key] * value 
            print("Element :- ",ele)
            new_arr += ele
            
        
