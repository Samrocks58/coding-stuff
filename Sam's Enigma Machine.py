abc = [i for i in "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"]
msg="Sam is Awesome."
translate_word = "Rzl hr Zvdrnld."
def convert(arg, conversion):
    upperlist=[]
    for j in arg:
        if j.isupper():
            upperlist.append(arg.index(j))
    conversion = conversion.lower()
    a_to_b = conversion.split('a')[1]
    ConvertRate = abc.index(a_to_b)
    clist=[]
    for c in arg:
        c = c.lower()
        if c == " ":
            clist.append(" ")
        elif c in abc:
            letter_index=abc.index(c)
            c = abc[(letter_index+ConvertRate)]
            clist.append(c)
        else:
            clist.append(c)
    for d in upperlist:
        clist[d] = clist[d].upper()
    Convertmsg=""
    for g in clist:
        Convertmsg += g
    return Convertmsg

def translate_with(arg, conversion):
    upperlist=[]
    for j in arg:
        if j.isupper():
            upperlist.append(arg.index(j))
    conversion = conversion.lower()
    a_to_b = conversion.split('a')[1]
    ConvertRate = abc.index(a_to_b)
    clist=[]

    for c in arg:
        c = c.lower()
        if c == " ":
            clist.append(" ")
        elif c in abc:
            letter_index=abc.index(c)
            c = abc[(letter_index-ConvertRate)]
            clist.append(c)
        else:
            clist.append(c)
    for d in upperlist:
        clist[d] = clist[d].upper()
    Convertmsg=""
    for g in clist:
        Convertmsg += g
    return Convertmsg

Printmsg = convert(msg, "az")
Printmsg2 = translate_with(Printmsg, "az")
print(msg)
print(Printmsg)
print(Printmsg2)