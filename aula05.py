import os 
os.system ("cls")
#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")

#ATIVIDADE 7
# nota = float(input("DIGITE SUA NOTA  "))
# nota1 = float(input("DIGITE SUA SEGUNDA NOTA  "))
# media = (nota + nota1) /2
# print ("MEDIA É ", media)
# if media < 5:
#     print("BURRO")
# elif media <=5 or media <=6 or media ==7:
#     print ("RECUPERAÇÃO")

# elif media > 7:
#     print(" PARABENS APROVADO")

#ATIVIDADE 8

# peso= float(input("QUAL É O SEU PESO: ").replace("," , "."))
# altura= float(input("QUAL É A SUA ALTURA:  ") .replace("," , "."))
# imc = peso/(altura*altura)
# print (f"SEU IMC é {imc: .2f}")

# if imc < 17:
#     print("MUITO ABAIXO DO PESO(GRAVETO)")
# elif imc > 17 and imc < 18.49:
#     print ("ABAIXA DO PESO(PESO LENÇOL)")
# elif imc > 18.5 and imc <24.99:
#     print ("PESO NORMAL(ABRE ASPA PESSOA NORMAL)")
# elif imc > 25 and imc < 29.99:
#     print ("ACIMA DO PESO (GORDIN)")
# elif imc > 30 and imc <34.99:
#     print ("OBESIDADE 1 (BOLA)")
# elif imc >35 and imc < 39.99:
#     print ("OBESIDADE 2(GORDAO)")
# elif imc > 40:
#     print ("OBESIDADE 3(GORDAO DA XJ)")


#ATIVIDADE 9 (a melhor)
print ("-"*14, "AUTOCAR", "-"*14)
print (r"""
 
░░░░░░░░░░░░▄▄▄█████████▄▄▄░░░░░░░░░░░░
░░░░░░░░▄▄██████▀▀▀▀▀▀▀██████▄▄░░░░░░░░
░░░░░░▄████▀▀░░░░░░░░░░░░░▀▀████▄░░░░░░
░░░░▄███▀░░░░░░░░░░░░░░░░░░░░▀▀███▄░░░░
░░▄███▀░░░░░░░░░░░░░░░░░░░░░░░░░████░░░
░▄███▀░░░░░▄▄▄▄░░░░░░░░░░░░░░░░░░▀███░░
░███░░░░░░█████▄░░░░░░░░░░░░░░░░░░▀███░
███▀░░░░░░██████░░░░░░░░░░░░░░░░░░░███▄
███░░░░░░░█████▀░░░░░░░░░░░░░░░░░░░░███
███░░░░░░░░████▄░░░░░░░░░░░░░░░░░░░░███
███░░░░░░░░░▀███▄░░░░░░░░░░░░░░░░░░░███
███░░░░░░░░░░░█████▄░░░▄███▄▄░░░░░░▄███
▀███░░░░░░░░░░░░▀████████████░░░░░░███░
░███▄░░░░░░░░░░░░░▀▀████████▀░░░░░███▀░
░░████░░░░░░░░░░░░░░░░░▀▀▀░░░░░░▄███▀░░
░░███▀░░░░░░░░░░░░░░░░░░░░░░░░░▄███▀░░░
░▄███░░░░▄▄░░░░░░░░░░░░░░░░░▄████▀░░░░░
▄███▄▄███████▄▄▄░░░░░░░▄▄▄█████▀░░░░░░░
███████▀▀▀▀▀███████████████▀▀░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒█░░▒█ █░░█ █▀▀█ ▀▀█▀▀ █▀▀ ░█▀▀█ █▀▀█ █▀▀█░
▒█▒█▒█ █▀▀█ █▄▄█ ░░█░░ ▀▀█ ▒█▄▄█ █░░█ █░░█░
▒█▄▀▄█ ▀░░▀ ▀░░▀ ░░▀░░ ▀▀▀ ▒█░▒█ █▀▀▀ █▀▀▀░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ """)

print ("ESTAMOS REFORMULANDO OS SALARIOS")
print ("."*50,)
salario = float(input("Digite o seu salario "))
if salario <= 2799.99:
    print("a.Seu salario antes do reajuste é", salario)
    print ("b.Seu aumento é de 20%")
    aumento = salario*0.20
    print ("c.seu aumento é ", aumento)
    atual = salario + aumento
    print("d.Logo seu salario atual é R$: ", atual )
    print ("."*50,)
elif salario >= 2800 and salario <6999.99:
    print("a.Seu salario antes do reajuste é", salario)
    print ("b.Seu aumento é de 15%")
    aumento = salario*0.15
    print ("c.seu aumento é R$", aumento)
    atual = salario + aumento
    print("d.Logo seu salario atual é R$: ", atual )
    print ("."*50,)
elif salario >= 7000 and salario < 14999.99:
    print("a.Seu salario antes do reajuste é", salario)
    print ("b.Seu aumento é de 10%")
    aumento = salario*0.10
    print ("c.seu aumento é R$", aumento)
    atual = salario + aumento
    print("d.Logo seu salario atual é R$: ", atual )
    print ("."*50,)
elif salario >= 15000:
    print("a.Seu salario antes do reajuste é", salario)
    print ("b.Seu aumento é de 5%")
    aumento = salario*0.05
    print ("c.seu aumento é R$", aumento)
    atual = salario + aumento
    print("d.Logo seu salario atual é R$: ", atual )
    print ("."*50)