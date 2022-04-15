metin=input('Metni qeyd edin:')
z=[]
for m in metin:
    z.append(ord(m))
print(z)
sifre=input('Acarinizi qeyd edin:')
a=[]
for s in sifre:
    a.append(ord(s))
la=[]
for r in a:
    r=int(r)
    la.append(r)
la=(la*(len(z)//len(la)))+la[:(len(z)%len(la))]
print(la)
print('Acarin ve metnin elementlerinin cemi')
x=0
F=[]
while x<len(z):
    F.append((z[x])+(la[x]))
    x=x+1
print(F)
print('Cem ikilik saya cevirilir ')
d=[]
for hee in F:
    d.append(bin(hee))
print(d)
print('Metnin sifrelenmis formasi:')
H=[]
for  yaz in F:
    H.append(chr(yaz))
print(H)
