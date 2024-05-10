attempts = 3
ascii_table = [chr(i) for i in range(128)] #brute force all possible passwords using all ascii characters
def breakPW():#retrieve encryption java sript function using inspect tools
    password_input = ascii_table
    expected_string = "e|278Fx7|!VeX7_!V!|@8SR"
    # Retrieve big integer values by going to
    # to a javascript playground and printing them out
    # https://playcode.io/new
    magic = [
        180758036634373586855986153129327037440435200000,
        30371497954664560547934282676524731982579264000,
        2326350245662806051448259351464928577062395200,
        107556589139054689493151371480217131922561440,
        3349112013620304019382625721734120647278572,
        74177829139406224107438224432649553406776,
        1202504716675938369856747352650589005671,
        14449993601000731218524154750449469141,
        128747857113173407665651901872655467,
        840323243106107751155149189961449,
        3906617606706492868477955626629,
        12254463773866918309096572719,
        23256080315034544256321661,
        20173193776555036220475,
    ]
    magic2 = 55087374223494444286125519719270400000
    calculated_string = ''
    one_char = 0
    result = 0
    nresult = 0
    for i in range(len(expected_string)):
        for j in range(len(ascii_table)):
            result = 0
            nresult = 0
            one_char = -ord(ascii_table[j])
            for k in range(len(magic)):
                result *= one_char
                result += magic[len(magic) - 1 - k]
            nresult = result % magic2
            result = int(-result / magic2)
            result += (888 - result) * (result > 127)
            result += (888 - result) * (nresult != 0)
            result += (888 - result) * (result < 33)
            if (expected_string[i] == chr(result)):
                calculated_string += ascii_table[j]
                break
    print(calculated_string)


# Call the function to simulate the behavior
breakPW()
