
sum_tot = 0
variable = 1
diff = 1
old_value = 10

while diff > 10**-16:
    new_value = 1 / (3*variable)
    sum_tot += new_value

    diff = old_value - new_value
    old_value = new_value
    variable += 1

print(sum_tot)
