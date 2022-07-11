def verificar_curriculo(candidato_analista = None,candidato_cientista = None,escolha = None):
    if escolha == 1:
        try:
            with open(f"{candidato_analista[1]}.txt","r",encoding="utf-8") as arquivo:
                for linha in arquivo:
                        for i in candidato_analista:
                            for key in dict_Analista.keys():
                                if key in linha.lower():
                                    return participante_analista_palavrachave.append(i)
        except FileNotFoundError:
            print("Arquivo não encontrado,tente novamente inserindo o nome correto.")    
    elif escolha == 2:
        try:
            with open(f"{candidato_cientista[1]}.txt","r",encoding="utf-8") as arquivo:
                for linha in arquivo:
                    for i in participante_cientista:
                        for key in dict_Cientista.keys():
                            if key in linha.lower():
                                return participante_cientista_palavrachave.append(i)
        except FileNotFoundError:
            print("Arquivo não encontrado,tente novamente inserindo o nome correto.")    

def inserir_candidato(escolha):
    candidato_analista = []
    candidato_cientista = []
    if escolha == 1:
        candidato_analista.append(input("Insira o seu nome:\n"))
        candidato_analista.append(input("Insira o nome do arquivo do seu currículo e nos mande por e-mail:"))
        return candidato_analista
    elif escolha == 2:
        candidato_cientista.append(input("Insira o seu nome:\n"))
        candidato_cientista.append(input("Insira o nome do arquivo do seu currículo e nos mande por e-mail:"))
        return candidato_cientista
dict_Analista = {
    "python": True,
    "powerbi" : True,
    "sql": True,
    "boa comunicação": True
}

dict_Cientista = {
    "python": True,
    "banco de dados": True,
    "machine learning" : True,
    "resolução de problemas": True,
    "estatística": True
}
count = 0
count_analista = 0
count_cientista = 0


participante_analista = []  # lista com todos os candidatos analistas
participante_cientista = [] # lista com todos os candidatos cientistas
participante_analista_palavrachave = [] # lista com todos os candidatos analistas com os requisitos no curriculo
participante_cientista_palavrachave = []    # lista com todos os candidatos cientistas com os requisitos no curriculo



try:    
    candidatos_quant = int(input("Insira a quantidade de inscrições que deseja realizar: "))
except ValueError:
    candidatos_quant = int(input("Insira a quantidade de inscrições que deseja realizar: (responda apenas com números inteiros positivos por favor):"))
while count < candidatos_quant:
    try:
        escolha_vaga = int(input("Em qual vaga deseja se candidatar?\n[1]Analista de dados\n[2]Cientista de dados\n"))
        if escolha_vaga == 1:
            participante_analista.append(inserir_candidato(escolha_vaga))
            count_analista += 1
            verificar_curriculo(candidato_analista = participante_analista[count_analista - 1] , escolha = 1)
        elif escolha_vaga == 2:
            
            count_analista += 1
            verificar_curriculo(candidato_cientista =  participante_cientista[count_cientista - 1] , escolha = 2)
        else:
            print("Escolha inválida,tente novamente...")
    except ValueError:
        print("Escolha inválida,tente novamente...")
    count = count_analista + count_cientista
    if count < candidatos_quant:
        while True:
            try:
                print("=====================================================")
                escolha = int(input("Deseja continuar inscrevendo os candidatos na vaga?\n[1]Sim\n[2]Não\n"))
                print("=====================================================")
                if  escolha == 1:
                    break
                elif escolha ==  2:
                    count = candidatos_quant
                    break
                else:
                    print("Escolha inválida,tente novamente...")
            except ValueError:
                print("Escolha inválida,tente novamente...")
                escolha = 1000


print(f"O números de candidatos inscritos nas vagas são:\nAnalista de dados: {len(participante_analista)}.\nCientista de dados: {len(participante_cientista)}.")
print(f"O número de candidatos que em seu currículo tem oque procuramos é: {len(participante_analista_palavrachave)+len(participante_cientista_palavrachave)}.")
print(f"Contando com:\n\bCandidatos Analistas promissores => \b {len(participante_analista_palavrachave)}\n\bCandidatos Cientistas promissores => \b {len(participante_cientista_palavrachave)}")