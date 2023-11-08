import datetime

def getAniversariantes(arquivo):
    mesAtual = datetime.datetime.now().month
    aniversariantes = []
    with open(arquivo, 'r') as file:
        for linha in file:
            nome, email, dataNascimento = linha.strip().split('|')
            dataNascimento = datetime.datetime.strptime(dataNascimento, "%d/%m/%Y")
            if dataNascimento.month == mesAtual:
                aniversariantes.append((nome, email, dataNascimento))
    
    return aniversariantes

def gerarAniversariantes(arquivoSaida, aniversariantes):
    with open(arquivoSaida, 'w') as file:
        for aniversariante in aniversariantes:
            nome, email, dataNascimento = aniversariante
            line = f"{nome}|{email}|{dataNascimento.strftime('%Y-%m-%d')}\n\n"
            file.write(line)

arquivoTxt = 'consultores.txt'
arquivoTxtSaida = 'consultores que fazem aniversario neste mês.txt'
aniversariantesDoMes = getAniversariantes(arquivoTxt)
gerarAniversariantes(arquivoTxtSaida, aniversariantesDoMes)
