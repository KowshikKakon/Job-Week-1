def pel(mystr):
    if(mystr==mystr[::-1]):
        return True
    else:
        return False
print(pel("madam"))