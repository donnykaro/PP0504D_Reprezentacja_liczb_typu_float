# hex_to_power = {1: 1, 2: 16, 3: 256, 4: 4096, 5: 65536, 6: 1048576}
# non_numeric_hex_cases = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
#
#
# def to_hex(number):
#     # if number < 16:
#     #     return number
#
#     result = []
#     for x in hex_to_power:
#         if hex_to_power[x] > number:
#             for n in range(x-1, 0, -1):
#                 divide_rest = int(number / hex_to_power[n])
#                 if divide_rest in non_numeric_hex_cases:
#                     result.append(non_numeric_hex_cases[divide_rest])
#                 else:
#                     result.append(str(divide_rest))
#                 number = int(number % hex_to_power[n])
#
#             return result
#
#
import struct


def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])


def format_output(result):
    temp_hex_result = []
    for i in range(0, len(result), 2):
        try:
            if result[i] + result[i+1] == '00':
                temp_hex_result.append('0')
            else:
                temp_hex_result.append(result[i] + result[i+1])
        except IndexError:
            temp_hex_result.append('0')

    return temp_hex_result


hex_numbers = []
for i in range(0, int(input())):
    hex_numbers.append(format_output(float_to_hex(float(input()))[2:]))

for i in hex_numbers:
    if i[0] == '0':
        print('0 0 0 0')
    else:
        print(' '.join(i))
