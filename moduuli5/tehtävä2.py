luvut = []
jatkuu = True
while jatkuu:

    luku = input( 'Anna luku: ')
    print(luku)

    if luku =='':
        jatkuu = False

    else:
        luvut.append(int(luku))
        luvut.sort(reverse=True)
for i in range(5):
    print("Lviisi suurinta luka:", luvut[i])











