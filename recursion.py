# ვქმნით ფუნქციას, რომელსაც გადავცემთ ნ პარამეტრს, შემდეგ ვამოწმებთ თუ ეს გადაცემული n == 0 ? return 1 : n * ref_func(n-1)
def rec_func(n):
    if n == 0:
        return 1
    else:
         return n * rec_func(n - 1)
     
     
print(rec_func(5))
print(rec_func(4))
print(rec_func(3))
print(rec_func(2))