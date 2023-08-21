def realizar_login():
    tentativas = 0
    while tentativas < 3:
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        if usuario == "usuario123" and senha == "senha123":
            return True

        print("Usuário ou senha incorretos. Tente novamente.")
        tentativas += 1

    print("Você excedeu o número máximo de tentativas. Contate o suporte da central para desbloqueio de conta.")
    return False

def obter_localizacao():
    print("Selecione a zona de São Paulo:")
    print("1. Oeste")
    print("2. Leste")
    print("3. Norte")
    print("4. Sul")
    opcao = input("Digite o número correspondente à zona desejada: ")
    # Lógica para verificar a opção de localização
    # ...
    return opcao

def obter_informacoes_lixeira(lixeira):
    peso = 300  # Exemplo de peso da lixeira coletado do circuito arduíno
    volume = 1200  # Exemplo de volume da lixeira coletado do circuito arduíno
    timer = 20  # Exemplo de timer da lixeira coletado do circuito arduíno
    return peso, volume, timer

def exibir_resumo(dados_lixeiras):
    print("Resumo:")
    for lixeira, dados in dados_lixeiras.items():
        print(f"Lixeira {lixeira}: Peso = {dados[0]}kg, Volume = {dados[1]}L, Timer = {dados[2]}min")

def main():
    funcionario_logado = realizar_login()
    if not funcionario_logado:
        print("Falha no login. Encerrando o programa.")
        return

    dados_lixeiras = {}
    continuar = True
    while continuar:
        localizacao = obter_localizacao()
        lixeira = input("Digite o número serial correspondente à lixeira desejada: ")
        peso, volume, timer = obter_informacoes_lixeira(lixeira)
        dados_lixeiras[lixeira] = (peso, volume, timer)

        opcao = input("Deseja selecionar outra lixeira? (S/N): ")
        if opcao.upper() != "S":
            continuar = False

    exibir_resumo(dados_lixeiras)

main()



