# String Slicing
try:    
    name = "Code By Kaja"
    print(name[0])  # Output: C
    print(name[1])  # Output: o
    print(name[2])  # Output: d
    print(name[3])  # Output: e
    print(name[4])  # Output:
    print(name[5])  # Output: B
    print(name[6])  # Output: y
    print(name[7])  # Output: K
    print(name[8])  # Output: a
    print(name[9])  # Output: j
    print(name[10])  # Output: a
    print(name[11])  # Output:
 
    print(name[0:4])  # Output: Code only prints up to the 3th index witch means 0,1,2,3 but forth will not be printed
    print(name[0:6])  # Output: Code B
    # print(name[12])  # Output: Error: string index out of range
    print(name[0:12])  # Output: Code By Kaja
    print(name[5:])   # Output: By Kaja
    print(name[:5])   # Output: Code
    print(name[::-1])  # Output: aja K yB edoC
    print(name[::-2])   # Output: aja K yB edoC
    
#     print(f"An error occurred: {e}")
except IndexError as e:
    print(f"{e}")

