cipher = '*s<;:{7M>?T=RY:FYS"B?TI{"{I:NY=NJ:&Y"rYS>L6D~~9'
def shift(c,key):
    return c+key
def dec(text):
    aabb = ""
    for c in text:
        ac = ord(c)
        print(ac)
        if ac >= 85 and ac <= 90:
            ac = shift(ac,6)
            aabb += chr(ac)
            continue
        if ac >= 105 and ac <= 122:
            ac = shift(ac,-32)
            aabb += chr(ac)
            continue
        if ac >= 40 and ac <= 47:
            ac = shift(ac,25)
            aabb += chr(ac)
            continue
        
        if ac >= 91 and ac <= 104:
            ac = shift(ac,-57)
            aabb += chr(ac)
            continue
        
        if ac >= 123 and ac <= 125:
            ac = shift(ac,-68)
            aabb += chr(ac)
            continue
        if ac >= 58 and ac <= 64:
            ac = shift(ac,-10)
            aabb += chr(ac)
            continue
        if ac>=48 and ac<=54:
            ac = shift(ac,10)
            aabb += chr(ac)
            continue

        if ac >= 55 and ac < 58:
            ac = shift(ac,68)
            aabb += chr(ac)
            continue
        
        if ac >= 34 and ac <= 39:
            ac = shift(ac,83)
            aabb += chr(ac)
            continue
        
        if ac >= 34 and ac <= 84:
            ac = shift(ac,32)
            aabb += chr(ac)
            continue
        
        if ac == 126 or ac == 33:
            aabb += chr(33)
    return aabb
                                         
print(dec(cipher))                                       
