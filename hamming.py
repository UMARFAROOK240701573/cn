data = input("Enter 4-bit data: ")

h = ['0'] * 8

h[3] = data[0]
h[5] = data[1]
h[6] = data[2]
h[7] = data[3]

h[1] = str(int(h[3]) ^ int(h[5]) ^ int(h[7]))
h[2] = str(int(h[3]) ^ int(h[6]) ^ int(h[7]))
h[4] = str(int(h[5]) ^ int(h[6]) ^ int(h[7]))

print("Hamming code:", ''.join(h[1:]))

pos = int(input("Enter error position (0 for no error): "))

if pos != 0:
    h[pos] = '1' if h[pos] == '0' else '0'

s1 = int(h[1]) ^ int(h[3]) ^ int(h[5]) ^ int(h[7])
s2 = int(h[2]) ^ int(h[3]) ^ int(h[6]) ^ int(h[7])
s4 = int(h[4]) ^ int(h[5]) ^ int(h[6]) ^ int(h[7])

error = s1 + 2 * s2 + 4 * s4

print("Error position:", error)

if error != 0:
    h[error] = '1' if h[error] == '0' else '0'

print("Corrected code:", ''.join(h[1:]))