uppercases = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercases = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
specialchars = '.?!&#,;:-_*'

def firstTask(password):
    requirements = 0
    if len([x for x in password if x in uppercases]) > 0:
        requirements += 1
    if len([x for x in password if x in lowercases]) > 0:
        requirements += 1
    if len([x for x in password if x in numbers]) > 0:
        requirements += 1
    if requirements == 3:
        return "True"
    else:
        return "False"


print firstTask("Ab1")
print firstTask("A1B")
print firstTask("abBBA")
print firstTask("123Password")
print firstTask("")

def secondTask(password):
    strength = 0
    if len([x for x in password if x in specialchars]) > 0:
        strength += 1
    numberStrength = len([x for x in password if x in numbers])
    if numberStrength > 0:
        if numberStrength >= 4:
            strength += 3
        elif numberStrength >= 2:
            strength += 2
        elif numberStrength >= 1:
            strength += 1
    upperStrength = len([x for x in password if x in uppercases])
    if upperStrength > 0:
        if upperStrength >= 3:
            strength += 3
        elif upperStrength >= 2:
            strength += 2
        elif upperStrength >= 1:
            strength += 1
    lowerStrength = len([x for x in password if x in lowercases])
    if lowerStrength > 0:
        if lowerStrength >= 3:
            strength += 3
        elif lowerStrength >= 2:
            strength += 2
        elif lowerStrength >= 1:
            strength += 1
    return strength

print secondTask("1")
print secondTask("1234")
print secondTask("password")
print secondTask("password1234123")
print secondTask("password!!!23")
print secondTask("PassWord123!")
print secondTask("IAmSoTired1234!")
