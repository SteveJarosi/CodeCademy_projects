message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
offset = 10
alph_str = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
alph_L = []
alph_U = []
alph_tmp = alph_str.split(',')
for i in alph_tmp:
    alph_U.append(i.strip())
print(alph_U)
for i in alph_U:
    alph_L.append(i.lower())
print(alph_L)


def decode(str, offset):
    str_dec = ''
    for i in str:
        if i in alph_L:
            str_dec += alph_L[(alph_L.index(i)+offset) % 26]
        elif i in alph_U:
            str_dec += alph_U[(alph_U.index(i)+offset) % 26]
        else:
            str_dec += i
    return str_dec


print(decode(message, 10))

def encode(str, offset):
    str_enc = ''
    for i in str:
        if i in alph_L:
            str_enc += alph_L[(alph_L.index(i)-offset) % 26]
        elif i in alph_U:
            str_enc += alph_U[(alph_U.index(i)-offset) % 26]
        else:
            str_enc += i
    return str_enc

print(encode("Hello! How are you doing on this beautyful day?", 10))

print(decode("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10))

print(decode("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14))

for i in range(26):
    print(decode("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.", i), i)
# offset: 7

def vigenere_decode(str, keyword):
    str_dec = ''
    count=0
    for i in str:
        if i in alph_L:
            str_dec += alph_L[(alph_L.index(i)-(alph_L.index(keyword[count % len(keyword)]))) % 26]
            count+=1
        elif i in alph_U:
            str_dec += alph_U[(alph_U.index(i)-(alph_U.index(keyword[count % len(keyword)]))) % 26]
            count+=1
        else:
            str_dec += i
        
    return str_dec

print(vigenere_decode("dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!", "friends"))

def vigenere_encode(str, keyword):
    str_enc = ''
    count=0
    for i in str:
        if i in alph_L:
            str_enc += alph_L[(alph_L.index(i)+(alph_L.index(keyword[count % len(keyword)]))) % 26]
            count+=1
        elif i in alph_U:
            str_enc += alph_U[(alph_U.index(i)+(alph_U.index(keyword[count % len(keyword)]))) % 26]
            count+=1
        else:
            str_enc += i
        
    return str_enc

print(vigenere_encode("you were able to decode this? nice work! you are becoming quite the expert at crytography!", "friends"))
