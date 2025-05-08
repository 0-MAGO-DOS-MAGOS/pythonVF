import os
os.system("cls")
#ESTRUTURAS CONDICIONAIS IF ELSE (ELSIF)
#SWITCH CASE -> (match case) escolha caso (a partir da versão 3.10)
#match valor:
# case valor:


# brawler= input ("escolha um brawler")

# match brawler:
#     case "juju":
#         print (" gayzão")
#     case "amber":
#         print ("viadão")
#     case "gus":
#         print ("maior viadão")
#     case "bibi":
#         print ("the best")



# dia = input("DIGITE UM DIA DA SEMANA   ")

#  match dia:
#     case "1":
#      print ("SEGUNDA-FEIRA")
#     case "2":
#      print ("TERÇA-FEIRA")
#     case "3":
#      print ("QUARTA-FEIRA")
#     case "4":
#      print ("QUINTA-FEIRA")
#     case "5":
#      print ("SEXTA-FEIRA")
#     case "6":
#      print ("SABADO")
#     case "7":
#      print ("DOMINGO")
# #     case _:
# #      print ("NAO É UM DIA DA SEMANA")

# print ("MUNDO DO CELULAR")

# print ("""
#    OPÇOES DE ESCOLHA:    
#    1- IPHONE 15 - R$ 5000,00
#    2- XIAOMI REDMI 13 PRO PLUS 512GB - 2500,00
#    3- SANGUNG S25 265GB - 6999,99
    
       
#           """)
# celular= input("digite o numero do produto ")

# print ("*"*40)
# print (""" 
#      ESCOLHA A REGIAO DE ENTREGUE  
#        SP -> 10,00
#        MG -> 15,00
#        RS -> 20,00

#        """)
# frete= input("digite a sigla do estado ")
# print ("seu frete é", frete) 
# match celular:
#     case "1":   
#      celular = 5000
#     case "2":
#      celular = 2500
#     case "3":
#      celular = 6999.99
#     case _ :
#      print ("NUMERO NAO RECONHECIDO")
     
# print ("seu produto custa R$", celular)

# match frete:
#     case "SP":
#      frete = 10
#     case "MG":
#      frete = 15
#     case "RS":
#      frete = 20
#     case _ :
#      print("NUMERO NÃO RECONHECIDO")

# print ("seu frete é R$", frete)

# print ("*"*40)

# print ("PREÇO R$:",celular)
# print ("FRETE R$:",frete)
# print ("TOTAL R$:",celular+frete)


print ("JOGO DE PEDRAA, PAEPELL E TESORA")
import random
maquina = random.randint(1,3)
match maquina:
    case _ if maquina == 1: 
     maquina = ( """
    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    case _ if maquina == 2:
     maquina = ("""
     _________
---'    ______)
           (____)
          (_____)
         (_____)
---._____(___)
""")
    case _ if maquina ==3:
     maquina = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

""")
    
eu= input ("ESCOLHA ENTRE PEDRA, PAPEL E TESOURA: ").upper()
match eu:
  case "PEDRA":
    eu =  ("""
     _________
---'    ______)
           (____)
          (_____)
         (_____)
---._____(___)
""")
  case "PAPEL":
    eu = ( """
    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
  case "TESOURA":
    eu = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

""")


print ("A MAQUINA ESCOLHEU")
print (maquina)

print ("VOCÊ ESCOLHEU")
print (eu)


match eu:
   case _ if eu == ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

""") and maquina == ( """
    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""):
        print("VOCÊ GANHOU")
   case _ if eu == ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

""") and maquina == ("""
     _________
---'    ______)
           (____)
          (_____)
         (_____)
---._____(___)
"""):
        print ("VOCÊ PERDEU")
   case _ if eu == ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

""") and maquina == ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""):
        print ("VOCÊ EMPATOU ")

match eu:
   case _ if eu == ( """
    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""") and maquina == ( """
    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""):
        print("VOCÊ EMPATOU")
   case _ if eu == ( """
    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""") and maquina == ("""
     _________
---'    ______)
           (____)
          (_____)
         (_____)
---._____(___)
"""):
        print ("VOCÊ GANHOU")
   case _ if eu == ( """
    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""") and maquina == ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""):
        print ("VOCÊ PERDEU ")
match eu:
   case _ if eu == ( """
    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""") and maquina == ( """
    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""):
        print("VOCÊ GANHOU ")
   case _ if eu == ( """
    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""") and maquina == ("""
     _________
---'    ______)
           (____)
          (_____)
         (_____)
---._____(___)
"""):
        print ("VOCÊ EMPATOU")
   case _ if eu == ( """
    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""") and maquina == ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""):
        print ("VOCÊ GANHOU ")



