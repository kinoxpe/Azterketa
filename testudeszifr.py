gakoa = {
    'A': 'd',
    'B': 'B',
    'C': 'i',
    'D': 'p',
    'E': 'a',
    'F': 's',
    'G': 'j',
    'H': 't',
    'I': 'o',
    'J': 'n',
    'K': 'r',
    'L': 'z',
    'M': 'h',
    'N': 's',
    'O': 'f',
    'P': 'm',
    'Q': 'b',
    'R': 'c',
    'S': 'q',
    'T': 'l',
    'U': 'g',
    'V': 'y',
    'W': 'W',
    'X': 'e',
    'Y': 'Y',
    'Z': 'u'
}

file_path = "/home/asier/Escritorio/3/segurtasuna/labo1/1 Laborategia -  Zifraketa I-20230925/txt.txt"
with open(file_path, 'r') as file:
    testua = file.read()
print(testua)
print()
print()
print()
frekuentziak = {}
for letra in testua:
    if letra.isalpha() and letra.isupper():
        letra = letra.upper()
        if letra in frekuentziak:
            frekuentziak[letra] += 1
        else:
            frekuentziak[letra] = 1
frekuentziak_ordenatutak = dict(sorted(frekuentziak.items(), key=lambda item: item[1], reverse=True))
keys_frekuentziak_ordenatutak = list(frekuentziak_ordenatutak.keys())
print(keys_frekuentziak_ordenatutak)
print()
print()
print()
testu_berria = ""
for letra in testua:
    if letra.isalpha() and letra.isupper():
        letra = letra.upper()
        testu_berria += gakoa[letra]
    else:
        testu_berria += letra
print(testu_berria)
print()
print()
print()
