print("O heroi que buscamos, responda apenas s/n")
resposta1 = input("Esse personagem tem capa vermelha? ")

if resposta1 == "s":
    print("Então é o Super-Homem")
else:
    resposta2 = input("Esse personagem tem capa preta? ")
    if resposta2 == "s":
        print("Então é o Batman")
    else:
        resposta3=input("esse personagem parece um robo?")
        if resposta3=="s":
            print("entao e o ciborgue")
        else:
            resposta4=input("esse personagem tem um raio com simbolo?")
            if resposta4=="s":
                print("entao e o flash")
            else:
                resposta5=input("esse personagem tem roupa verde")
                if resposta5=="s":
                    print("entao e o lanterna verde")
                else:
                    resposta6=input("esse personagem tem podere aquaticos ?")
                    if resposta6=="s":
                        print("entao e o aquaman")
                    else:
                        resposta7=input("esse personagem usa uma corda com arma ")
                        if resposta7=="s":
                            print("entao e a mulher maravihar")
                        else:
                            print("voce n sabe oq quer")