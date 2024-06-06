from colorama import Fore, Style
from pessoa_fisica import PessoaFisica
from conta_corrente import ContaCorrente
from deposito import Deposito
from saque import Saque


def depositar(usuarios, contas):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print(
            Fore.RED
            + "\nUsuário não encontrado, fluxo de depósito encerrado!"
            + Style.RESET_ALL
        )
        return

    numero_conta = input("Informe o número da conta: ")
    conta = filtrar_conta(numero_conta, contas)

    if not conta:
        print(
            Fore.RED
            + "\nConta não encontrada, fluxo de depósito encerrado!"
            + Style.RESET_ALL
        )
        return

    if conta.cliente != usuario:
        print(
            Fore.RED
            + "\nUsuário não encontrado, fluxo de depósito encerrado!"
            + Style.RESET_ALL
        )
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    usuario.realizar_transacao(conta, transacao)


def sacar(usuarios, contas):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print(
            Fore.RED + "\nUsuário não encontrado, fluxo de saque encerrado!"
            + Style.RESET_ALL
        )
        return

    numero_conta = input("Informe o número da conta: ")
    conta = filtrar_conta(numero_conta, contas)

    if not conta:
        print(
            Fore.RED + "\nConta não encontrada, fluxo de saque encerrado!"
            + Style.RESET_ALL
        )
        return

    if conta.cliente != usuario:
        print(
            Fore.RED + "\nUsuário não encontrado, fluxo de saque encerrado!"
            + Style.RESET_ALL
        )
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    usuario.realizar_transacao(conta, transacao)


def exibir_extrato(usuarios, contas):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print(
            Fore.RED + "\nUsuário não encontrado, fluxo de extrato encerrado!"
            + Style.RESET_ALL
        )
        return

    numero_conta = input("Informe o número da conta: ")
    conta = filtrar_conta(numero_conta, contas)

    if not conta:
        print(
            Fore.RED + "\nConta não encontrada, fluxo de extrato encerrado!"
            + Style.RESET_ALL
        )
        return

    if conta.cliente != usuario:
        print(
            Fore.RED + "\nUsuário não encontrado, fluxo de extrato encerrado!"
            + Style.RESET_ALL
        )
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato_vazio = True
    for transacao in transacoes:
        print(transacao["registro"])
        extrato_vazio = False

    if extrato_vazio:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("===========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    usuarios.append(usuario)

    print("\n=== Usuário criado com sucesso! ===")


def criar_conta(usuarios, contas):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\nCliente não encontrado, fluxo de criação de conta encerrado!")
        return

    numero_conta = len(contas) + 1
    conta = ContaCorrente.nova_conta(usuario, numero_conta)
    contas.append(conta)
    usuario.adicionar_conta(conta)

    print("\n=== Conta criada com sucesso! ===")
    print(conta)


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def filtrar_conta(numero_conta, contas):
    contas_filtradas = [
        conta for conta in contas if conta.numero == numero_conta]
    return contas_filtradas[0] if contas_filtradas else None
