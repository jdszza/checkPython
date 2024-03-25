#DUPLA: JENNIFER DE SOUZA E FERNANDO BERTOLUCCI

print("Atenção! Informe as notas de 0 a 100.")
print("Primeiro Semestre")
check1 = int(input("Nota do Checkpoint 1: "))
check2 = int(input("Nota do Checkpoint 2: "))
check3 = int(input("Nota do Checkpoint 3: "))
sprint1 = int(input("Nota do Sprint 1: "))
sprint2 = int(input("Nota do Sprint 2: "))
gs1 = int(input("Nota da Global Solution: "))

print("Segundo Semestre")
check4 = int(input("Nota do Checkpoint 1: "))
check5 = int(input("Nota do Checkpoint 2: "))
check6 = int(input("Nota do Checkpoint 3: "))
sprint3 = int(input("Nota do Sprint 1: "))
sprint4 = int(input("Nota do Sprint 2: "))
gs2 = int(input("Nota da Global Solution: "))

menor_nota = min(check1, check2, check3)
menor_nota2 = min(check4, check5, check6)

geral1 = 0
geral2 = 0

if menor_nota == check1:
    geral1 = (check2 + check3 + sprint1 + sprint2) / 4
elif menor_nota == check2:
    geral1 = (check1 + check3 + sprint1 + sprint2) / 4
else:
    geral1 = (check1 + check2 + sprint1 + sprint2) / 4

media1 = (geral1 * 0.40) + (gs1 * 0.60)

if menor_nota == check4:
    geral2 = (check5 + check6 + sprint3 + sprint4) / 4
elif menor_nota == check5:
    geral2 = (check4 + check6 + sprint3 + sprint4) / 4
else:
    geral2 = (check4 + check5 + sprint3 + sprint4) / 4

media2 = (geral2 * 0.40) + (gs2 * 0.60)

media_final = (media1 * 0.40) + (media2 * 0.60)

print(media_final)

if media_final >= 60:
    print("Aluno Aprovado!")

if media_final < 40:
    print("Aluno Reprovado")

if media_final >= 40 and media_final < 60:
    print("Aluno De Exame")
