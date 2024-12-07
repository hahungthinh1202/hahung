#main
gender  = input("Enter your gender(M/F): ")
h_value = int(input("Enter your hemoglobin value (g/l): "))
female_list = ["Female", "female","girl","Girl", "woman", "Woman","F"]
male_list   = ["male", "Male","boy","Boy", "man", "Man","M"]
if gender in female_list:
    if h_value < 117:
        print("your hemoglobin value (g/l) is too low")
    elif h_value > 155:
        print("your hemoglobin value (g/l) is too high")
    else:
        print("your hemoglobin value (g/l) is normal")
elif gender in male_list:
    if h_value < 134:
        print("your hemoglobin value (g/l) is too low")
    elif h_value > 167:
        print("your hemoglobin value (g/l) is too high")
    else:
        print("your hemoglobin value (g/l) is normal")
else:
    print("invalid input")
