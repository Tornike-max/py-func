def func(dict):
    min_key = None
    min_value = float('inf')
    
    for key,value in dict.items():
        if value < min_value:
            min_value = value
            min_key = key
        print(min_value)
    if min_key is not None:
        print(f"Lowest value is {min_value}")
dict = {
    'A': 43,
    'B': 32,
    'C': 44,
    'D': 31,
    'E': 98,
}

func(dict)




