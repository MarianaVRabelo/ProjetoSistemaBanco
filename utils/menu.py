from colorama import Fore, Style
from operacoes import (
    depositar,
    sacar,
    exibir_extrato,
    criar_conta,
    listar_contas,
    criar_usuario,
)


def exibir_menu():
    menu = f"""
    {Fore.CYAN}
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => {Style.RESET_ALL}"""
    return input(menu)


def main():
    contas = []
    usuarios = []

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            depositar(usuarios, contas)

        elif opcao == "s":
            sacar(usuarios, contas)

        elif opcao == "e":
            exibir_extrato(usuarios, contas)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            criar_conta(usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\nVolte sempre!")
            break

        else:
            print(
                Fore.RED
                + "Operação inválida, por favor selecione novamente a operação desejada."
                + Style.RESET_ALL
            )
