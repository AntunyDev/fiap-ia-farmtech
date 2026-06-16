from modulos.talhoes import cadastrar_talhao, listar_talhoes, remover_talhao
from modulos.colheitas import registrar_colheita, listar_colheitas, colheitas_por_talhao
from modulos.relatorios import (
    relatorio_perdas_geral,
    relatorio_por_metodo,
    relatorio_prejuizo,
)
from modulos.persistencia import salvar_dados, carregar_dados, registrar_log
from modulos.banco import (
    inicializar_banco,
    salvar_talhao,
    salvar_colheita,
    listar_talhoes_bd,
    listar_colheitas_bd,
)
from rich.console import Console
from rich.panel import Panel
from rich import print as rprint

console = Console()


def limpar_terminal():
    import os

    os.system("cls" if os.name == "nt" else "clear")


estado = {"talhoes": {}, "colheitas": [], "historico": []}


def menu_talhoes():
    while True:
        limpar_terminal()
        rprint(
            Panel(
                "[bold yellow]GESTÃO DE TALHÕES[/bold yellow]",
                border_style="green",
                expand=False,
            )
        )
        rprint("[bold yellow][1][/bold yellow] [green]Cadastrar talhão[/green]")
        rprint("[bold yellow][2][/bold yellow] [green]Listar talhões[/green]")
        rprint("[bold yellow][3][/bold yellow] [green]Remover talhão[/green]")
        rprint("[bold yellow][0][/bold yellow] [yellow]Voltar[/yellow]")
        opcao = input("\nOpção: ").strip()

        if opcao == "1":
            talhao = cadastrar_talhao(estado["talhoes"])
            if talhao:
                salvar_talhao(talhao)
                salvar_dados(estado)
                registrar_log(
                    estado["historico"], f"Talhão '{talhao['nome']}' cadastrado."
                )

        elif opcao == "2":
            listar_talhoes(estado["talhoes"])
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            remover_talhao(estado["talhoes"])
            salvar_dados(estado)
            registrar_log(estado["historico"], "Talhão removido.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_colheitas():
    while True:
        limpar_terminal()
        rprint(
            Panel(
                "[bold yellow]REGISTRO DE COLHEITAS[/bold yellow]",
                border_style="green",
                expand=False,
            )
        )
        rprint("[bold yellow][1][/bold yellow] [green]Registrar colheita[/green]")
        rprint(
            "[bold yellow][2][/bold yellow] [green]Listar todas as colheitas[/green]"
        )
        rprint("[bold yellow][3][/bold yellow] [green]Colheitas por talhão[/green]")
        rprint("[bold yellow][0][/bold yellow] [yellow]Voltar[/yellow]")
        opcao = input("\nOpção: ").strip()

        if opcao == "1":
            registrar_colheita(estado["talhoes"], estado["colheitas"])
            if estado["colheitas"]:
                salvar_colheita(estado["colheitas"][-1])
            salvar_dados(estado)
            registrar_log(estado["historico"], "Colheita registrada.")

        elif opcao == "2":
            listar_colheitas(estado["colheitas"])
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            colheitas_por_talhao(estado["talhoes"], estado["colheitas"])
            input("\nPressione Enter para continuar...")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_relatorios():
    while True:
        limpar_terminal()
        rprint(
            Panel(
                "[bold yellow]RELATÓRIOS[/bold yellow]",
                border_style="green",
                expand=False,
            )
        )
        rprint(
            "[bold yellow][1][/bold yellow] [green]Relatório geral de perdas[/green]"
        )
        rprint(
            "[bold yellow][2][/bold yellow] [green]Comparativo manual vs mecânico[/green]"
        )
        rprint("[bold yellow][3][/bold yellow] [green]Top 5 maiores prejuízos[/green]")
        rprint("[bold yellow][0][/bold yellow] [yellow]Voltar[/yellow]")
        opcao = input("\nOpção: ").strip()

        if opcao == "1":
            relatorio_perdas_geral(estado["colheitas"])
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            relatorio_por_metodo(estado["colheitas"])
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            relatorio_prejuizo(estado["colheitas"])
            input("\nPressione Enter para continuar...")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_banco():
    while True:
        limpar_terminal()
        rprint(
            Panel(
                "[bold yellow]BANCO DE DADOS ORACLE[/bold yellow]",
                border_style="green",
                expand=False,
            )
        )
        rprint("[bold yellow][1][/bold yellow] [green]Consultar talhões[/green]")
        rprint("[bold yellow][2][/bold yellow] [green]Consultar colheitas[/green]")
        rprint("[bold yellow][0][/bold yellow] [yellow]Voltar[/yellow]")
        opcao = input("\nOpção: ").strip()

        if opcao == "1":
            listar_talhoes_bd()
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            listar_colheitas_bd()
            input("\nPressione Enter para continuar...")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_principal():
    while True:
        limpar_terminal()
        rprint(
            """[bold yellow]
███████╗░█████╗░██████╗░███╗░░░███╗████████╗███████╗░█████╗░██╗░░██╗  ░░░░░░
██╔════╝██╔══██╗██╔══██╗████╗░████║╚══██╔══╝██╔════╝██╔══██╗██║░░██║  ░░░░░░
█████╗░░███████║██████╔╝██╔████╔██║░░░██║░░░█████╗░░██║░░╚═╝███████║  █████╗
██╔══╝░░██╔══██║██╔══██╗██║╚██╔╝██║░░░██║░░░██╔══╝░░██║░░██╗██╔══██║  ╚════╝
██║░░░░░██║░░██║██║░░██║██║░╚═╝░██║░░░██║░░░███████╗╚█████╔╝██║░░██║  ░░░░░░
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝  ░░░░░░[/bold yellow]"""
        )
        rprint(
            "\n[bold yellow]Sistema de Gestão de Colheitas de Cana-de-Açúcar (SGCCA)[/bold yellow]\n"
        )
        rprint("[bold yellow][1][/bold yellow] [green]Gestão de Talhões[/green]")
        rprint("[bold yellow][2][/bold yellow] [green]Registro de Colheitas[/green]")
        rprint("[bold yellow][3][/bold yellow] [green]Relatórios[/green]")
        rprint("[bold yellow][4][/bold yellow] [green]Banco de Dados Oracle[/green]")
        rprint("[bold yellow][5][/bold yellow] [green]Histórico de operações[/green]")
        rprint("[bold yellow][0][/bold yellow] [yellow]Sair[/yellow]")
        opcao = input("\nOpção: ").strip()

        if opcao == "1":
            menu_talhoes()

        elif opcao == "2":
            menu_colheitas()

        elif opcao == "3":
            menu_relatorios()

        elif opcao == "4":
            menu_banco()

        elif opcao == "5":
            if not estado["historico"]:
                rprint("[yellow]Nenhuma operação registrada.[/yellow]")
            else:
                rprint(
                    Panel(
                        "[bold yellow]HISTÓRICO[/bold yellow]",
                        border_style="green",
                        expand=False,
                    )
                )
                for entrada in estado["historico"]:
                    rprint(
                        f"[green]{entrada['timestamp']}[/green]  [yellow]{entrada['mensagem']}[/yellow]"
                    )
                input("\nPressione Enter para continuar...")

        elif opcao == "0":
            salvar_dados(estado)
            rprint("[bold green]Dados salvos. Até logo![/bold green]")
            break

        else:
            rprint("[bold yellow]Opção inválida.[/bold yellow]")


if __name__ == "__main__":
    inicializar_banco()

    dados_salvos = carregar_dados()
    if dados_salvos:
        estado["talhoes"] = dados_salvos.get("talhoes", {})
        estado["colheitas"] = dados_salvos.get("colheitas", [])
        estado["historico"] = dados_salvos.get("historico", [])

    menu_principal()
