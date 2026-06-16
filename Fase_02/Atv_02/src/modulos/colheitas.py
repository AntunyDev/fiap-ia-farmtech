from modulos.talhoes import buscar_talhao_por_id
from datetime import datetime
from rich import print as rprint
from rich.table import Table
from rich.panel import Panel

METODOS_COLHEITA = ("Manual", "Mecânico")

PERDA_REFERENCIA = {
    "Manual": 5.0,
    "Mecânico": 15.0
}


def _validar_float(mensagem, minimo=0.0, maximo=None):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor < minimo:
                print(f"Valor mínimo permitido: {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Valor máximo permitido: {maximo}")
                continue
            return valor
        except ValueError:
            print("Digite um número válido. Exemplo: 150.5")


def _validar_inteiro(mensagem, opcoes=None):
    while True:
        try:
            valor = int(input(mensagem).strip())
            if opcoes and valor not in opcoes:
                print("Opção inválida. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Digite um número inteiro válido.")


def calcular_perda(producao_esperada, perda_percentual):
    perda_toneladas = producao_esperada * (perda_percentual / 100)
    producao_real = producao_esperada - perda_toneladas
    return round(perda_toneladas, 2), round(producao_real, 2)


def registrar_colheita(talhoes, colheitas):
    print("(Digite 0 para cancelar)\n")

    talhao_id = input("ID do talhão: ").strip().upper()
    if talhao_id == "0":
        return

    talhao = buscar_talhao_por_id(talhoes, talhao_id)
    if not talhao:
        print("Talhão não encontrado.")
        return

    print(f"Talhão encontrado: {talhao['nome']} ({talhao['area_ha']} ha)\n")

    rprint("[bold yellow]Métodos de colheita:[/bold yellow]")
    for i, m in enumerate(METODOS_COLHEITA, 1):
        rprint(f"  [bold yellow][{i}][/bold yellow] [green]{m}[/green]")
    idx = _validar_inteiro("Escolha o método: ", opcoes=range(1, len(METODOS_COLHEITA) + 1))
    metodo = METODOS_COLHEITA[idx - 1]

    ano_safra = _validar_inteiro("Ano da safra: ", opcoes=range(2000, 2101))
    producao_esperada = _validar_float("Produção esperada (toneladas): ", minimo=0.1)
    
    referencia = PERDA_REFERENCIA[metodo]
    print(f"Referência de perda para colheita {metodo.lower()}: {referencia}%")
    perda_percentual = _validar_float("Percentual de perda observado (%): ", minimo=0.0, maximo=100.0)

    preco_tonelada = _validar_float("Preço por tonelada (R$): ", minimo=0.1)

    perda_toneladas, producao_real = calcular_perda(producao_esperada, perda_percentual)
    prejuizo = round(perda_toneladas * preco_tonelada, 2)

    if perda_percentual > referencia:
        rprint(f"\n[bold yellow]AVISO: Perda acima da referência para colheita {metodo.lower()} ({referencia}%)![/bold yellow]")

    resumo = (
        f"Produção esperada : [bold yellow]{producao_esperada}[/bold yellow] t\n"
        f"Perda             : [bold yellow]{perda_toneladas}[/bold yellow] t ([bold yellow]{perda_percentual}%[/bold yellow])\n"
        f"Produção real     : [bold green]{producao_real}[/bold green] t\n"
        f"Prejuízo estimado : [bold yellow]R$ {prejuizo}[/bold yellow]"
    )
    rprint(Panel(resumo, title="Resumo da Colheita", border_style="green", expand=False))

    confirmacao = input("\nConfirmar registro? (s/n): ").strip().lower()
    if confirmacao != "s":
        print("Registro cancelado.")
        return

    colheita = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S"),
        "talhao_id": talhao_id,
        "talhao_nome": talhao["nome"],
        "ano_safra": ano_safra,
        "metodo": metodo,
        "producao_esperada": producao_esperada,
        "perda_percentual": perda_percentual,
        "perda_toneladas": perda_toneladas,
        "producao_real": producao_real,
        "preco_tonelada": preco_tonelada,
        "prejuizo": prejuizo,
        "data_registro": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    colheitas.append(colheita)
    print("Colheita registrada com sucesso!")


def listar_colheitas(colheitas):
    if not colheitas:
        rprint("[yellow]Nenhuma colheita registrada.[/yellow]")
        return

    table = Table(title="Registro de Colheitas", header_style="bold yellow", border_style="green")
    table.add_column("ID", style="yellow", width=16)
    table.add_column("Talhão", style="green")
    table.add_column("Safra", style="yellow", justify="center")
    table.add_column("Método", style="green")
    table.add_column("Prod.Esp.", style="yellow", justify="right")
    table.add_column("Perda%", style="yellow", justify="right")
    table.add_column("Prejuízo", style="bold yellow", justify="right")

    for c in colheitas:
        # Destacar perda alta com estilo diferente de amarelo se necessário, mas mantendo o tema
        table.add_row(
            c['id'],
            c['talhao_nome'],
            str(c['ano_safra']),
            c['metodo'],
            f"{c['producao_esperada']:.2f} t",
            f"{c['perda_percentual']:.2f}%",
            f"R$ {c['prejuizo']:.2f}"
        )

    rprint(table)


def colheitas_por_talhao(talhoes, colheitas):
    if not talhoes:
        print("Nenhum talhão cadastrado.")
        return

    listar_colheitas(colheitas)
    talhao_id = input("\nDigite o ID do talhão: ").strip().upper()

    filtradas = [c for c in colheitas if c["talhao_id"] == talhao_id]

    if not filtradas:
        print("Nenhuma colheita encontrada para este talhão.")
        return

    listar_colheitas(filtradas)