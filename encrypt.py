import random
#Gonna try to maje a basic encryptor on the fly. 
#I shouldn't need to know more than ord and chr, which I just looked up. 
print('(E)ncrypt or (D)ecrypt?')
while True:
    type = input()
    if type == 'E' or type == 'D':
        break
    else:
        print('Please input either E or D.')

#Using normal python random stuff, despite this being encryption. Such
#a card. Wait, do I need random? Start with ruining a perfectly good string. 

if type == 'E':
    print('Please input the string you wish to encrypt.')
    org = input()
    print('Do you have a (P)reexisting key, or would you like to (G)enerate one?')
    while True:
        keyt = input()
        if keyt == 'G' or keyt == 'P':
            break
        else:
            print('Please input either G or P.')
    if keyt == 'G':
        #Current idea is to generate a long number 32 digits or another
        #even number, split into 16 pairs, add 32 to get out of control
        #characters, before converting into unicode.
        rawkey = str(random.randint(0,(10**32-1))).zfill(32)
        #Occasionally gives us a 31 digit number, could, at worst, give
        #a single zero. String.zfill seems to work.
        li = range(0,32,2)
        chunk = []
        for x in li:
            chunk.append(rawkey[x:x+2])
            if len(chunk) == 16:
                break
        num = list(map(int,chunk))
        nums = [x+32 for x in num]
        keyparts = list(map(chr,nums))
        sep = ''
        key = sep.join(keyparts)
        print('Your key is:\n' + key + '\nYou\'d better jot that down!')
    else:
        print('Please input your key:')
        key = input()
    #We have the key now, so we have to do above in reverse, but we
    #can't guarantee key length so...
    keystring = [x for x in key]
    keynums = list(map(ord,keystring))
    keylist = [x-32 for x in keynums]
    fkey = int(''.join(map(str,keylist)))
    #We're going to be doing operations like above a lot, aren't we?
    #Regardless, with our big ugly key number, we can do math unto the
    #the poor input and create something unrecognizable.
    orgnums = list(map(ord,[x for x in org]))
    #I have no idea if this even makes decryption harder but it's fun.
    if fkey%2 == 1:
        nkl = keylist[::2]
    else:
        nkl = keylist[1::2]
    
    enc = []
    for x in range(len(orgnums)):
        nval = orgnums[x] + 32 + nkl[x%len(nkl)]
        enc.append(chr(nval))
    encr = ''.join(enc)
    print('Your encrypted phrase is:\n' + encr)
#Decryption
else:
    print('Input your string.')
    msg = input()
    print('Input your key.')
    key = input()
    
    #Repeating the processing of key verbatim should help?
    keystring = [x for x in key]
    keynums = list(map(ord,keystring))
    keylist = [x-32 for x in keynums]
    fkey = int(''.join(map(str,keylist)))
    if fkey%2 == 1:
        nkl = keylist[::2]
    else:
        nkl = keylist[1::2]
    #Now we turn the msg into a processable string of numbers.
    msgnums = list(map(ord,[x for x in msg]))

    dec = []
    for x in range(len(msgnums)):
        nval = msgnums[x] - 32 - nkl[x%len(nkl)]
        dec.append(chr(nval))
    decr = ''.join(dec)
    print('Your encrypted phrase is:\n' + decr)

#Times I used char instead of chr counter: 2