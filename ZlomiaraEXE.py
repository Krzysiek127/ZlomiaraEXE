import random,sys

if len(sys.argv) == 1:
    filename = input("Input filename? ")
    outfn = input("Output filename? ")
    msg = input("Message? ")
    repeats = int(input("Message Repeats? "))
else:
    if sys.argv[1] == "-help":
        nameoffile = str(sys.argv[0]).split('\\')
        print("Usage: ")
        print(nameoffile[len(nameoffile)-1], " [IFN] [OFN] [MSG] [RPT]")
        print("")
        print("[IFN] Input Path and Filename")
        print("[OFN] Output Path and Filename")
        print("[MSG] Message")
        print("[RPT] Number of times to repeat message in random parts of file.")
        print("")
        print("If no arguments is passed, program will prompt it.")
        print("Made by Krzysiek127")
        exit(0)
    else:
        filename = sys.argv[1]
    outfn = sys.argv[2]
    msg = sys.argv[3]
    repeats = int(sys.argv[4])
truth_table = [True,False]
file_bytes = []
message_bytes = []
fb, sb = "", ""
x = 0

for i in msg:
    message_bytes.append(format(ord(i),'b'))
meslen = len(message_bytes)

INT_BITS = 8


def rotate_left(n, d):
    return (n << d) | (n >> (INT_BITS - d))


def rotate_right(n, d):
    return (n >> d) | (n << (INT_BITS - d)) & 0xFFFFFFFF


with open(filename, 'rb') as f:
    while True:
        byte_s = f.read(1)
        if not byte_s:
            break
        byte = byte_s[0]
        file_bytes.append(format(byte,'b'))
bytelen = len(file_bytes)
bytes2write = file_bytes

print("Encoding a message in file, please wait...")


#for i in file_bytes:
#    findex = file_bytes.index(i)
#    try:
#        x = format(i,'b') # Add zeros so there would be 8 bits
#    except ValueError:
#        x = i
#    print(type(i))
#    for addbits in range(8-len(x)):
#        x = str("0" + i)
#
#    for b in range(0,3): # Split to four bits
#        fb += x[b]
#    for c in range(4,7):
#        sb += x[c]

#    rot_r = random.randint(0,7)
#    rot_l = random.randint(0,7)

#   fbb = rotate_left(int(fb,base=2),rot_r)
#  sbb = rotate_right(int(sb,base=2),rot_l)

#    for m in message_bytes:
#       index = message_bytes.index(m)
#      xorfb = fbb ^ int(m,base=2)
#     xorsb = sbb ^ int(message_bytes[index],base=2)
#
#       bytes2write[findex] = xorfb
#      bytes2write[findex+1] = xorsb
#
#       print(type(i))
#      byt = format(int(i,base=2),'x').upper()
#     pos = format(findex,'x').upper()
#        byt2 = format(bytes2write[findex],'x').upper()
#        print("Byte {0} at position {1} replaced with {2}".format(byt,pos,byt))
#

for rep in range(repeats):
    radom = random.randint(0,round(bytelen*0.75))
    for i in message_bytes:
        index = message_bytes.index(i)
        fbyte = file_bytes[index+radom]

        fb = int(fbyte,base=2)
        sb = int(i,base=2)

        #if random.choice(truth_table):
        #    save = rotate_right(fb ^ sb,random.randint(0,7))
        #else:
        #    save = rotate_left(fb ^ sb, random.randint(0, 7))

        save = (fb ^ sb) ^ random.randint(0, 255)
        bytes2write[index+radom] = format(save,'b')
        print("Byte: ", format(fb,'x').upper(), " at position: ",format(index+radom,'x'), " replaced with: ", format(save,'x').upper())
print("Done!")
print("Saving...")

savefile = open(outfn,"w")
for saving in bytes2write: # Zapisywanie
    try:
        savefile.write(chr(int(saving,base=2)))
    except UnicodeDecodeError:
        savefile.write("A")
    except UnicodeEncodeError:
        savefile.write("A")
    print("Remaining bytes: ", len(bytes2write) - x)
    x += 1
savefile.close()
print("Done!")