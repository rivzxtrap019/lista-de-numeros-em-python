print("PROGRAMA PARA REALIZAR OPERAÇÕES COM LISTAS\n")

lista=[] # lista começa vazia
chave_para_realizar_operacoes_ate_cansar_ligada=True
while chave_para_realizar_operacoes_ate_cansar_ligada:
    print("1) Esvaziar a lista")
    print("2) Incluir número na lista")
    print("3) Mostrar a lista")
    print("4) Somar tudo da lista")
    print("5) Remover um número digitando-o")
    print("6) Remover um número utilizando sua posição")
    print("7) Calcular a média dos números")
    print("8) Mostrar o menor número da lista")
    print("9) Mostrar o maior número da lista")
    print("10) Sair do programa")    
    chave_para_escolher_opcao_ate_acertar_ligada=True
    while chave_para_escolher_opcao_ate_acertar_ligada:
        try:
            opcao=int(input("Opcao? "))
        except ValueError:
            print("Opção inválida; tente novamente!")
        else:
            if opcao<1 or opcao>10:
                print("Opção inválida; tente novamente!")
            else:
                chave_para_escolher_opcao_ate_acertar_ligada=False

    if opcao==1:
        lista.clear()
        print("Esvaziamento realizado com sucesso!")
    elif opcao==2:
        chave_para_digitar_um_numero_ate_acertar_ligada=True
        while chave_para_digitar_um_numero_ate_acertar_ligada:
            try:
                numero=float(input("Digite um número? "))
            except ValueError:
                print("Foi pedido um número; tente novamente!")
            else:   
                chave_para_digitar_um_numero_ate_acertar_ligada=False
        lista.append(numero)
        print("Número incluído com sucesso!")
    elif opcao==3:
        print(lista)
    elif opcao==4:
        print(sum(lista))
        
    elif opcao==5:
        chave_para_digitar_um_numero_ate_acertar_ligada=True
        while chave_para_digitar_um_numero_ate_acertar_ligada:
            try:
                numero=float(input("Digite um número? "))
            except ValueError:
                print("Foi pedido um número; tente novamente!")
            else:   
                chave_para_digitar_um_numero_ate_acertar_ligada=False
        lista.remove(numero)
        print("Número removido com sucesso!")
    elif opcao==6:
        chave_para_digitar_um_numero_ate_acertar_ligada=True
        while chave_para_digitar_um_numero_ate_acertar_ligada:
            try:
                numero=int(input("Digite um a posição de número! "))
            except ValueError:
                print("Foi pedido um número; tente novamente!")
            else:   
                chave_para_digitar_um_numero_ate_acertar_ligada=False
        del lista[numero]
        print("Número removido com sucesso!")
    elif opcao==7:
        media = sum(lista) / len(lista)
        print(media)
    elif opcao==8:
        
        menor = min(lista)
        print(f'O menor número é: {menor}')
    elif opcao==9:
        
        maior = max(lista)
        print(f'O maior número é: {maior}')
    else: # só sobrou a opcao ser 5
        chave_para_realizar_operacoes_ate_cansar_ligada=False

print("PROGRAMA ENCERRADO!")