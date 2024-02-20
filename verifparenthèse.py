import socket
import time

HOST = '37.59.31.202'  # L'adresse IP du serveur
PORT = 2000  # Le port du serveur

open_list = ["[","{","("]
close_list = ["]","}",")"]
 
# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "False"
    if len(stack) == 0:
        return "True"
    else:
        return "False"



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print('Received', repr(data))
    s.sendall(b'\n3')
    for _ in range(200):  # Pour chaque chaîne de parenthèses
        data = s.recv(1024).decode()
        print('Received', repr(data))
        if "parentheses" in data:  # Si c'est une instruction
            continue  # Passer à la prochaine itération
        if data.strip():  # Ignorer les chaînes vides
            result = check(data)  # Vérifier si la chaîne est équilibrée
            print(result)
            s.sendall(str(result).encode())  # Renvoyer le résultat
