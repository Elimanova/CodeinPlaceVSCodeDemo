def convert_c_to_f(temp_in_celsius):
    temp_in_farinheight = temp_in_celsius * 1.8 + 32
    return temp_in_farinheight

temperature_in_f = convert_c_to_f(40)
print(temperature_in_f)
