def validaIP(ipz):
    ips = ipz.split(".")
    for i in ips:
        i = int(i)
        if i < 0 or i > 255:
            return False
    return True

def EscreveArquivo(ip_valido,ip_invalido):
    files = open(("Relação_de_ip's.txt" , "w"))
    files.write("[ip_valido]\n")
    for i in range(len(ip_valido)):
        files.write(ip_valido[i])
    files.write("[ip_invalido]\n")
    for i in range(len(ip_invalido)):
        files.write(ip_invalido[i])
    file.close()
        

file = open("IP.txt", "r")
ip = file.readlines()
file.close()
ip_valido = []
ip_invalido = []
for ipz in ip:
    if validaIP(ipz) == True:
        ip_valido.append(ipz)
    else:
        ip_invalido.append(ipz)
EscreveArquivo(ip_valido,ip_invalido)


