import math
from datetime import datetime

def notas(valor):
    notasMaiorValue = []
    notasMenorValue = []
    
    valor = int(valor)

    notasMaiorValue.extend(['100 reais'] * (valor // 100))
    valor %= 100
    notasMaiorValue.extend(['50 reais'] * (valor // 50))
    valor %= 50
    notasMenorValue.extend(['20 reais'] * (valor // 20))
    valor %= 20
    notasMenorValue.extend(['10 reais'] * (valor // 10))
    valor %= 10
    notasMenorValue.extend(['5 reais'] * (valor // 5))
    valor %= 5
    
    return notasMaiorValue, notasMenorValue

def opcoesRetirada(valor):
    notasMaiorValue, notasMenorValue = notas(valor)
    halfValue = valor // 2
    notasMaiorHalf, notasMenorHalf = notas(halfValue)
    print(f"Valor empréstimo: {valor} reais")
    
    print("Notas de maior valor:")
    for nota in notasMaiorValue:
        print(f"➢ 1 x {nota};")
    
    print("\nNotas de menor valor:")
    for nota in notasMenorValue:
        print(f"➢ 1 x {nota};")
    
    print("\nNotas meio a meio:")
    print(f"{halfValue} reais em notas de maior valor:")
    for nota in notasMaiorHalf:
        print(f"➢ 1 x {nota};")
    
    print(f"{halfValue} reais em notas de menor valor:")
    for nota in notasMenorHalf:
        print(f"➢ 1 x {nota};")

#inputs
nome_colaborador = input("Nome: ")
dataAdmissao = input("Data de admissão (Dia/Mês/Ano): ")
salarioaAual = float(input("Salário atual: "))
valorEmprestimo = float(input("Valor de empréstimo: "))

dataAdmissao = datetime.strptime(dataAdmissao, "%d/%m/%Y")
tempoCasa = datetime.now().year - dataAdmissao.year

if tempoCasa > 5 and valorEmprestimo % 2 == 0:
    opcoesRetirada(valorEmprestimo)
else:
    print("você não atende os requisitos mínimos para o empréstimo ModalGR.")

