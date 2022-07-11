def verificar_curriculo(candidato_analista = None,candidato_cientista = None,escolha = None):
    contador_ocorrencia_analista = 0
    contador_ocorrencia_cientista = 0
    if escolha == 1:
        try:
            with open(f"{candidato_analista[1]}.txt","r",encoding="utf-8") as arquivo: #Abro o arquivo,leio ele e verifico se tem algum elemento das chaves do dicionário nele.
                for linha in arquivo:
                        for key in dict_Analista.keys():
                            if key in linha.lower():
                                contador_ocorrencia_analista +=1    #Se for encontrado algum elemento,é contabilizado a ocorrência.
        
            if contador_ocorrencia_analista > 0: #Se tiver uma ocorrência ou mais,o contador de ocorrência é adicionado na lista e a lista é retornada da função
                candidato_analista.append(contador_ocorrencia_analista)
                return candidato_analista
            return 0 #Caso tenha nenhuma ocorrência,retorna o valor 0 indicando que não teve.
        except FileNotFoundError:
            print("Arquivo não encontrado,tente novamente inserindo o nome do arquivo correto.")
            return None    #Retorna None se não conseguir ler o arquivo,então não será feito a verificação e portanto retorna vazio.
    elif escolha == 2:
        try:
            with open(f"{candidato_cientista[1]}.txt","r",encoding="utf-8") as arquivo:
                for linha in arquivo:
                        for key in dict_Cientista.keys():
                            if key in linha.lower():
                                contador_ocorrencia_cientista += 1
            if contador_ocorrencia_cientista > 0:
                candidato_cientista.append(contador_ocorrencia_cientista)
                return candidato_cientista
            return 0
        except FileNotFoundError:
            print("Arquivo não encontrado,tente novamente inserindo o nome do arquivo correto.")
            return None    

def inserir_candidato(escolha):
    candidato_analista = []
    candidato_cientista = []
    if escolha == 1:
        candidato_analista.append(input("Insira o seu nome:\n"))
        while True:
            try:
                decisao1 = int(input("Você deseja enviar o arquivo do seu currículo para nós ou inserir o resumo por aqui para criamos um arquivo com ele?\n[1]Enviar currículo.\n[2]Escrever o resumo.\n"))
                if decisao1 == 1:
                    candidato_analista.append(input("Insira o nome do arquivo do seu currículo e nos mande por e-mail:"))#A idéia é o usuário digitar o nome de algum arquivo txt que esteja na pasta do programa.
                    break
                elif decisao1 == 2:
                    resumo = input("Insira o resumo abaixo(Aperte Enter apenas para enviar o Resumo):\n") #Aqui o usuário digita uma frase ou um texto sem a tecla enter,pois é para confirmar.
                    candidato_analista.append(criando_arquivo(resumo)) #Estou adicionando na lista candidato_analista o retorno da função,que cria um arquivo com o nome dado dentro dela e depois retorna o nome.
                    break 
                else:
                    print("Opção inválida.Tente novamente...")
            except ValueError:
                print("Opção inválida.Tente novamente...")
                decisao1 = 1000
        return candidato_analista
    elif escolha == 2:
        candidato_cientista.append(input("Insira o seu nome:\n"))
        while True:
            try:
                decisao2 = int(input("Você deseja enviar o arquivo do seu currículo para nós ou inserir o resumo por aqui para criamos um arquivo com ele?\n[1]Enviar currículo.\n[2]Escrever o resumo.\n"))
                if decisao2 == 1:
                    candidato_cientista.append(input("Insira o nome do arquivo do seu currículo e nos mande por e-mail:"))
                    break
                elif decisao2 == 2:
                    resumo = input("Insira o resumo abaixo(Aperte Enter apenas para enviar o Resumo):\n")
                    candidato_cientista.append(criando_arquivo(resumo))
                    break
                else:
                    print("Opção inválida.Tente novamente...")
            except ValueError:
                print("Opção inválida.Tente novamente...")
                decisao2 = 1000
        return candidato_cientista

def criando_arquivo(resumo = None): # Cria um arquivo txt
    nome = input("Qual o nome que deseja dar para o arquivo do seu resumo ?(Sem caracteres especiais: ?!@#$% para evitar erro)") #Pega o nome dado pelo usuário,dá error se tiver caractere especial
    nomef = nome.replace(" ","") #Formata de forma bem básica,para tirar o espaço. Utilizei outra variável para receber a formatação pois achei melhor para entender.

    with open(f"{nomef}.txt","w",encoding= "utf-8") as arquivo: #Cria um arquivo txt para escrever a mensagem dada
        arquivo.write(resumo)
    return nomef    #Depois de criar o arquivo,retorna no nome dele para ele ser utilizado posteriormente na outra função de verificar arquivo.
   
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


while True:
    try:    
        candidatos_quant = int(input("Insira a quantidade de inscrições que deseja realizar: "))
        break
    except ValueError:
        print("Valor inválido,tente novamente...")
while count < candidatos_quant:
    while True:
        try:
            escolha_vaga = int(input("Em qual vaga deseja se candidatar?\n[1]Analista de dados\n[2]Cientista de dados\n"))
            if escolha_vaga == 1:
                participante_analista.append(inserir_candidato(escolha_vaga))
                count_analista += 1
                lista = verificar_curriculo(candidato_analista = participante_analista[count_analista - 1] , escolha = 1)
                if lista == None :
                    count_analista -= 1
                    participante_analista.pop()
                if (lista != None) and (lista != 0):
                    participante_analista_palavrachave.append(list(lista))
                break
            elif escolha_vaga == 2:
                participante_cientista.append(inserir_candidato(escolha_vaga))            
                count_cientista += 1
                lista = verificar_curriculo(candidato_cientista = participante_cientista[count_cientista - 1] , escolha = 2)
                if lista == None:
                    count_cientista -= 1
                    participante_cientista.pop()
                if (lista != None) and (lista != 0):
                    participante_cientista_palavrachave.append(list(lista))
                break
            else:
                print("Escolha inválida,tente novamente...")
        except ValueError:
            print("Escolha inválida,tente novamente...")
    count = count_analista + count_cientista
    metade = candidatos_quant/2
    if count > metade and count < candidatos_quant: #Se passar da metade e o usuário quiser sair,começará a aparecer uma pergunta perguntando se ele deseja sair.
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
                print("=====================================================")
                print("Escolha inválida,tente novamente...")
                escolha = 1000


print(f"O números de candidatos inscritos nas vagas são:\nAnalista de dados: {len(participante_analista)}.\nCientista de dados: {len(participante_cientista)}.")
print(f"O número de candidatos que tem oque procuramos é: {len(participante_analista_palavrachave)+len(participante_cientista_palavrachave)}.")
print(f"Contando com:\n\bCandidatos Analistas promissores => \b {len(participante_analista_palavrachave)}\n\bCandidatos Cientistas promissores => \b {len(participante_cientista_palavrachave)}")

#Mostrando os candidatos com os requisitos:
if len(participante_analista_palavrachave) > 0:
    print("Na lista de candidatos analistas de dados,os que possuem requisitos procurados são :")
    for i in participante_analista_palavrachave:
        print(f"O candidato {i[0]}.com {i[2]} palavras-chave.")
if len(participante_cientista_palavrachave) > 0:
    print("Na lista de candidatos cientistas de dados,os que possuem requisitos procurados são:")
    for j in participante_cientista_palavrachave:
        print(f"O candidato {j[0]}.Com {j[2]} palavras-chave.")