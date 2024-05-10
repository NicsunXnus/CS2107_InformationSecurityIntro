kkk = "$ecretK3ySup3rS3cr3t"

def check_one(input_str):

    if len(input_str) != 48:
        return False, "wrong len"

    if not input_str.startswith("CS2107{") or not input_str.endswith("}"):
        return False, "no fL@g header"

    content = input_str[len("CS2107{"):-1]

    return True, content

def check_two(input_two):

    wwww = "771010022c177a5c0c772a154b34625f54005200"
    bbb = list(bytes.fromhex(wwww))
    for i in range(len(input_two)):
        if ord(input_two[i]) ^ bbb[i] != ord(kkk[i]):
            return False
    
    return True

def check_three(user_input):

    # Beware the stairs of check
    # Are you good at math?
    # Maybe a math equation solver can help you ?

    if (ord(user_input[18]) == 84):
        if (ord(user_input[12]) - 105 == 0):
            if (ord(user_input[9]) + 100 == 199):    
                if (ord(user_input[0]) + ord(user_input[9]) == 204):
                    if (ord(user_input[7]) * 6 * ord(user_input[1]) == 56610):
                        if (ord(user_input[1]) * 8 - 90 == 798):
                            if (ord(user_input[10]) - ord(user_input[16]) == -40):
                                if (ord(user_input[2]) * 10 + ord(user_input[5]) - 900 == 298):
                                    if (ord(user_input[0]) ^ 99 == 100 - 90):
                                        if (ord(user_input[7]) - 900 == -815):
                                            if (ord(user_input[14]) * ord(user_input[11]) == 12760):
                                                if (ord(user_input[10]) + ord(user_input[2]) == ord(user_input[3]) + 79): 
                                                    if (ord(user_input[9]) + 3 * ord(user_input[5]) - ord(user_input[6]) == 291):
                                                        if (ord(user_input[13]) - 111 == -63):
                                                            if (ord(user_input[1]) == 111):
                                                                if (2 * ord(user_input[5]) - 3 * ord(user_input[1]) == ord(user_input[9]) - 236):
                                                                    if (ord(user_input[3]) * ord(user_input[4]) == 4560):
                                                                        if (ord(user_input[8]) * 4567 == 525205):
                                                                            if (ord(user_input[16]) * 9090 == 945360):
                                                                                if (-ord(user_input[7]) - ord(user_input[4]) - 18 * ord(user_input[0]) == -2023):
                                                                                    if (ord(user_input[19]) * 33 * ord(user_input[5]) - 45 * ord(user_input[9]) == 357753):
                                                                                        if (ord(user_input[14]) + ord(user_input[10]) - ord(user_input[3]) - ord(user_input[7]) == -6):
                                                                                            if (ord(user_input[11]) * ord(user_input[16]) == 143 * ord(user_input[17]) + 52):
                                                                                                if (147 + ord(user_input[12]) * ord(user_input[4]) == 5187):
                                                                                                    if (ord(user_input[13]) * ord(user_input[15]) == ord(user_input[18]) * 100 - 3840):
                                                                                                        if (ord(user_input[15]) * 1111 - 9999 == 95546):
                                                                                                            return True
                                                                                                        else:
                                                                                                            return False
                                                                                                    else:
                                                                                                        return False
                                                                                                else:
                                                                                                    return False
                                                                                            else:
                                                                                                return False
                                                                                        else:
                                                                                            return False
                                                                                    else:
                                                                                        return False
                                                                                else:
                                                                                    return False
                                                                            else:
                                                                                return False
                                                                        else:
                                                                            return False
                                                                    else:
                                                                        return False
                                                                else:
                                                                    return False
                                                            else:
                                                                return False
                                                        else:
                                                            return False
                                                    else:
                                                        return False
                                                else:
                                                    return False
                                            else:
                                                return False
                                        else:
                                            return False
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

ascii_table = [chr(i) for i in range(128)]
wwww = "771010022c177a5c0c772a154b34625f54005200"
bbb = list(bytes.fromhex(wwww))
pw = "CS2107{"
#starting index = 7
for i in range(0,20):
    for j in range(len(ascii_table)):
        if ord(ascii_table[j]) ^ bbb[i] == ord(kkk[i]):
            pw += ascii_table[j]
            break
print(pw) #first half, so now we have CS2107{SuspIc1ou$_exF1l7rat, 27 CHARACTERS
#Left 28 to 48
'''
Fill up remaining characters, can be done using pen,paper,calculator
0 i/105
1 111
2 110
3 95
4 48
5 98
6 102
7 85
8 115
9 99
10 64
11 116
12 105
13 48
14 110
15 95
16 104
17 84
18 84
19 112
'''
sec_half = [105,111,110,95,48,98,102,85,115,99,64,116,105,48,110,95,104,84,84,112]
for i in range(len(sec_half)):
    pw += chr(sec_half[i])
print(pw)
pw += '}'
is_valid, content = check_one(pw)
if not is_valid:
    print("incorrect check 1")
    exit()

print("Correct 1")

correct = check_two(content[:20])


if not correct:
    print("incorrect check 2")
    exit()

print("Correct 2")

correct = check_three(content[20:])


if not correct:
    print("incorrect check 3")
    exit()

print("Correct 3") 
