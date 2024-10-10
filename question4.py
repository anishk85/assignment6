def prefRevCapStr(mystr, original=None):
    if original is None:
        original = mystr
    if len(mystr) == 0:
        return ""
    if len(mystr) == 1:
        return mystr.upper() + " -> " + original
    else:
        return mystr[-1].upper() + prefRevCapStr(mystr[:-1], original)

d = prefRevCapStr("diwali to come")
print(d)
