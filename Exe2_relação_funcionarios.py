def ParaMB(TByte):
    TByte = float(TByte)
    return (float(TByte/(1024*1024)))

def Percentual(cadaUsuario,total):
    percentual = (cadaUsuario[3]/total)*100
    cadaUsuario.insert((len(cadaUsuario)),percentual)

def Ocupado(cadaUsuario,total):
    media = 0
    ele = len(cadaUsuario)
    media = (total) / (ele + 1)
    return media

usuarios = []
total,media = 0,0
posição = 1
cadaUsuario = []
with open("Exe2_usuarios.txt" , "r") as f:
    valor = 0
    for i in f:
        usuarios.append(i.split())
    for cadaUsuario in f:
        cadaUsuario.insert(0,posição)
        valor = ParaMB(float(cadaUsuario[2]))
        total += valor
        cadaUsuario.insert((len(cadaUsuario)),valor)
        posição += 1
    for cadaUsuario in f:
        Percentual(cadaUsuario,total)
media = Ocupado(cadaUsuario,total)

with open("Exe2_relatório_usuarios.txt" , "w") as file:
    file.write("ACME Inc.               Uso do espaço em disco pelos usuários.\n")
    file.write("-"*80)
    file.write("\nNº \tUsuario       \tEspaço utilizado    \t% de uso\n\n") 
    for cadaUsuario in file:
        porcentagem = round(cadaUsuario[3,2])
        file.write(str(cadaUsuario[0]) + "\t" + "{:<15}".format(cadaUsuario[1]) + "\t" + "{:<16}".format(porcentagem) + "MB" + "\t" + "{0:.2f}".format(cadaUsuario[4]) + "%" + "\n")
    file.write(f"\n Espaço total ocupado: {total}MB")
    file.write(f"\nEspaço médio ocuoado: {media}MB")
 