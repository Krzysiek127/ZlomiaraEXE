# ZłomiaraEXE.py V2.69
# Made by Krzysiek127

print("ZłomiaraEXE V2.69 \nMade by Krzysiek127\n")

rfile = open(input("Input > "), "r", encoding='utf-8')
wfile = open(input("Output > "), "w", encoding='utf-8')
message = input("Message > ")

readbyte = []
writebyte = []

while True:
    byt = rfile.read(1)  # Read one char at the time
    if byt == "":  # Check if char is null, if yes break
        break
    read = format(ord(byt), 'b')  # convert char into binary representation of it

    # if len(br) is lower than 16 bits, complete to this value.
    for i in range(0x10-len(read)):
        read = "0" + read
    readbyte.append(read)

while True:
    try:
        offset = int(input("Offset > "))
    except ValueError:
        raise Exception("ERROR: NOT A NUMBER.")
    if -1 < offset < len(readbyte):
        break
    print("ERROR: INVALID NUMBER.")

carry = "0000000000000000"

for byte_i in range(len(readbyte)):
    byte = readbyte[byte_i]

    todo = carry[0:12] + byte[12:16]
    carry = byte[0:12]

    try:
        writebyte.append(int(todo, base=2) ^ ord(message[byte_i-offset]))
    except IndexError:
        writebyte.append(int(todo, base=2))

for wr in writebyte:
    wfile.write(chr(wr))
