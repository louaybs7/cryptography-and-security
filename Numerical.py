def format_number(x):
    # Convert the decimal number to binary
    binary = bin(int(x * 2**5))[2:]

    # Add leading zeros to the binary number if necessary
    binary = '0'*(7-len(binary)) + binary

    # Extract the integer and fractional parts of the binary number
    integer_part = binary[:5]
    fractional_part = binary[5:]

    # Convert the integer and fractional parts to decimal
    integer = int(integer_part, 2)
    fractional = sum([int(fractional_part[i])*2**(-(i+1)) for i in range(len(fractional_part))])

    # Round the fractional part to 2 decimal places
    fractional = round(fractional, 2)

    # Combine the integer and fractional parts to form the formatted number
    formatted = f"[{integer_part} | {fractional}]"

    return formatted

print (format_number(0.12))
