from rich import print as rprint
from rich.table import Table
from rich.panel import Panel

def relatorio_perdas_geral(colheitas):
    if not colheitas:
        print("Nenhuma colheita registrada.")
        return

    total_esperado = sum(c["producao_esperada"] for c in colheitas)
    total_perda    = sum(c["perda_toneladas"]   for c in colheitas)
    total_real     = sum(c["producao_real"]      for c in colheitas)
    total_prejuizo = sum(c["prejuizo"]           for c in colheitas)
    media_perda    = (total_perda / total_esperado) * 100

    conteudo = (
        f"Produção esperada total : [bold yellow]{total_esperado:.2f}[/bold yellow] t\n"
        f"Produção real total     : [bold green]{total_real:.2f}[/bold green] t\n"
        f"Perda total             : [bold yellow]{total_perda:.2f}[/bold yellow] t\n"
        f"Média de perda          : [bold yellow]{media_perda:.2f}%[/bold yellow]\n"
        f"Prejuízo total          : [bold yellow]R$ {total_prejuizo:.2f}[/bold yellow]"
    )
    rprint(Panel(conteudo, title="[bold yellow]RELATÓRIO GERAL DE PERDAS[/bold yellow]", border_style="green", expand=False))


def relatorio_por_metodo(colheitas):
    if not colheitas:
        print("Nenhuma colheita registrada.")
        return

    grupos = {}
    for c in colheitas:
        metodo = c["metodo"]
        if metodo not in grupos:
            grupos[metodo] = {
                "quantidade": 0,
                "total_esperado": 0.0,
                "total_perda": 0.0,
                "total_prejuizo": 0.0
            }
        grupos[metodo]["quantidade"]      += 1
        grupos[metodo]["total_esperado"]  += c["producao_esperada"]
        grupos[metodo]["total_perda"]     += c["perda_toneladas"]
        grupos[metodo]["total_prejuizo"]  += c["prejuizo"]

    table = Table(title="Comparativo: Manual vs Mecânico", header_style="bold yellow", border_style="green")
    table.add_column("Método", style="green")
    table.add_column("Registros", style="yellow", justify="center")
    table.add_column("Prod. Esperada", style="yellow", justify="right")
    table.add_column("Perda Ton", style="yellow", justify="right")
    table.add_column("Perda %", style="yellow", justify="right")
    table.add_column("Prejuízo Total", style="bold yellow", justify="right")

    for metodo, dados in grupos.items():
        media = (dados["total_perda"] / dados["total_esperado"]) * 100
        table.add_row(
            metodo,
            str(dados["quantidade"]),
            f"{dados['total_esperado']:.2f} t",
            f"{dados['total_perda']:.2f} t",
            f"{media:.2f}%",
            f"R$ {dados['total_prejuizo']:.2f}"
        )
    
    rprint(table)


def relatorio_prejuizo(colheitas):
    if not colheitas:
        print("Nenhuma colheita registrada.")
        return

    top5 = sorted(colheitas, key=lambda c: c["prejuizo"], reverse=True)[:5]

    table = Table(title="Top 5 Maiores Prejuízos", header_style="bold yellow", border_style="green")
    table.add_column("Talhão", style="green")
    table.add_column("Safra", style="yellow", justify="center")
    table.add_column("Método", style="green")
    table.add_column("Perda %", style="yellow", justify="right")
    table.add_column("Prejuízo", style="bold yellow", justify="right")

    for c in top5:
        table.add_row(
            c['talhao_nome'],
            str(c['ano_safra']),
            c['metodo'],
            f"{c['perda_percentual']:.2f}%",
            f"R$ {c['prejuizo']:.2f}"
        )
    
    rprint(table)