def calculate_energy(m, c):
    energy = m * c ** 2
    return energy

m = int(input("m: "))
c = 300000000

result = calculate_energy(m, c)
print("E", format(result, ".0f"))
