#comment


import string

shibu = "botson shibu"
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase


shift = 34
shift %= 26
new_val = lower_case[shift:]+lower_case[:shift]
shifted_values = str.maketrans(new_val,lower_case)
print(shibu.translate(shifted_values))

