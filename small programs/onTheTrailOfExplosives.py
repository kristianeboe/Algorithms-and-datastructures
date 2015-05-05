from sys import stdin

class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
        self.vekt = vekt
        self.neste = None

def spor(kubbe):
    element = forste
    max = element.vekt
    while element.neste != None:
        element = element.neste
        if element.vekt > max:
            max = element.vekt
    return max


# Oppretter lenket liste
input = [54,37,100,123,1,54,500]
forste = None
siste = None
for i in range(0,len(input)):
    forrige_siste = siste
    siste = Kubbe(int(input[i]))
    if forste == None:
        forste = siste
    else:
        forrige_siste.neste = siste


# for linje in stdin:
    forrige_siste = siste
#     siste = Kubbe(int(linje))
#     if forste == None:
#         forste = siste
#     else:
#         forrige_siste.neste = siste

# Kaller loesningsfunksjonen og skriver ut resultatet
print (spor(forste))
