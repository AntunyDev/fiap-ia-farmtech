import csv
import os

from data import (
    lista_culturas,
    lista_formas,
    lista_largura,
    lista_comprimento,
    lista_area,
    lista_insumos,
    lista_ruas,
    lista_dose,
)
from math import pi

culturas_disponiveis = {1: "Café", 2: "Milho"}
formas_culturas = {"Café": "retângulo", "Milho": "quadrado"}


def limpar_terminal():
    import subprocess
    import platform

    input("Pressione qualquer tecla para continuar...")

    sistema = platform.system()
    if sistema == "Windows":
        subprocess.run("cls", shell=True)  # Windows
    else:
        subprocess.run("clear", shell=True)  # Linux e Mac


def mostrar_menu():
    print("\n===== FARMTECH SOLUTIONS =====\n")
    print("[1] - Inserir plantação")
    print("[2] - Mostrar dados")
    print("[3] - Atualizar plantação")
    print("[4] - Deletar plantação")
    print("[5] - Calcular manejo de insumos")
    print("[6] - Exportar dados para CSV")
    print("[7] - Consultar dados meteorológicos")
    print("[8] - Sair \n")


def ler_opcao():
    while True:
        entrada = input("Digite uma opção: ")
        try:
            numero = float(entrada)
            if numero.is_integer():
                op = int(numero)

                if 1 <= op <= 8:
                    return op

                else:
                    print("Opção inválida.")
            else:
                print("Opção inválida.")

        except ValueError:
            print("Entrada Inválida")


def calcular_area(forma, dimensao1, dimensao2):
    if forma == "retângulo":
        return dimensao1 * dimensao2
    elif forma == "quadrado":
        return dimensao1**2
    else:
        print(f"Erro: forma '{forma}' não suportada.")
        return 0


def inserir_plantacao():
    print("\n===== INSERIR PLANTAÇÃO =====\n")

    # Escolha da cultura
    while True:
        print("Escolha a cultura:")
        for chave, valor in culturas_disponiveis.items():
            print(f"[{chave}] - {valor}")
        try:
            escolha = int(input("Digite o número da cultura: "))
            if escolha in culturas_disponiveis:
                cultura = culturas_disponiveis[escolha]
                break
            else:
                print("Opção inválida. Por favor, escolha uma cultura válida.")

        except ValueError:
            print(
                "Entrada inválida. Por favor, digite o número correspondente à cultura de interesse."
            )

    # Escolha da forma
    if cultura == "Milho":
        while True:
            try:
                lado = float(input("Digite o lado da área quadrada (em metros): "))
                if lado > 0:
                    break
                else:
                    print("O valor deve ser positivo.")
            except ValueError:
                print("Digite um número válido.")
        largura = lado
        comprimento = lado
    else:
        while True:
            try:
                largura = float(input("Digite a largura da área (em metros): "))
                if largura > 0:
                    break
                else:
                    print("O valor deve ser positivo.")
            except ValueError:
                print("Digite um número válido.")
        while True:
            try:
                comprimento = float(input("Digite o comprimento da área (em metros): "))
                if comprimento > 0:
                    break
                else:
                    print("O valor deve ser positivo.")
            except ValueError:
                print("Digite um número válido.")

    # Calcular a área com base na forma da cultura
    forma = formas_culturas[cultura]
    area = calcular_area(forma, largura, comprimento)
    print(f"A área calculada para a cultura {cultura} é: {area:.2f} m².")

    # guardar dados nas listas
    lista_culturas.append(cultura)
    lista_formas.append(forma)
    lista_largura.append(largura)
    lista_comprimento.append(comprimento)
    lista_area.append(area)
    lista_ruas.append(None)
    lista_dose.append(None)
    lista_insumos.append(None)


def mostrar_dados():
    print("\n===== DADOS DAS PLANTAÇÕES =====\n")
    if len(lista_culturas) == 0:
        print("Nenhum dado disponível.")
        return

    for i in range(len(lista_culturas)):
        print(f"Plantação {i + 1}:")
        print(f"Cultura: {lista_culturas[i]}")
        print(f"Forma geométrica usada para a cultura: {lista_formas[i]}")
        print(f"Largura: {lista_largura[i]} m")
        print(f"Comprimento: {lista_comprimento[i]} m")
        print(f"Área: {lista_area[i]:.2f} m²")
        print(
            f"Quantidade de ruas: {lista_ruas[i] if lista_ruas[i] is not None else 'Não informado até o momento'}"
        )
        print(
            f"Dose de insumo: {lista_dose[i] if lista_dose[i] is not None else 'Não calculado até o momento'} mL/m"
        )
        print(
            f"Total de insumo necessário: {lista_insumos[i]:.2f} litros"
            if lista_insumos[i] is not None
            else "Total de insumo necessário: Não calculado até o momento"
        )
        print("-" * 30)


def atualizar_plantacao():
    print("\n===== ATUALIZAR PLANTAÇÃO =====\n")

    if len(lista_culturas) == 0:
        print("Nenhuma plantação cadastrada.")
        return

    # Se houver apenas uma plantação
    if len(lista_culturas) == 1:
        index = 0
        print(
            f"Plantação única encontrada: {lista_culturas[0]} (Área: {lista_area[0]:.2f} m²)"
        )

    else:
        # Mostrar plantações disponíveis
        for i, cultura in enumerate(lista_culturas):
            print(f"[{i+1}] - {cultura} (Área: {lista_area[i]:.2f} m²)")

        # Escolher plantação
        while True:
            try:
                escolha = int(
                    input("Digite o número da plantação que deseja atualizar: ")
                )
                if 1 <= escolha <= len(lista_culturas):
                    index = escolha - 1
                    break
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Digite apenas números.")

    # Menu de atualização
    print("\nO que deseja atualizar?")
    print("[1] Cultura")
    print("[2] Largura")
    print("[3] Comprimento")

    while True:
        try:
            campo = int(input("Escolha uma opção: "))
            if campo in [1, 2, 3]:
                confirmacao = input(f"Confirma atualização do campo {campo}? (s/n): ")
                if confirmacao.lower() == "s":
                    break
                else:
                    print("Operação cancelada.")
                    return
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite apenas números.")

    # Atualizar cultura
    if campo == 1:

        while True:

            print("\nEscolha a nova cultura:")
            for chave, valor in culturas_disponiveis.items():
                print(f"[{chave}] - {valor}")

            try:
                nova = int(input("Digite: "))

                if nova in culturas_disponiveis:

                    cultura_nome = culturas_disponiveis[nova]

                    lista_culturas[index] = cultura_nome

                    nova_forma = formas_culturas[cultura_nome]
                    lista_formas[index] = nova_forma

                    if cultura_nome == "Milho":
                        lista_comprimento[index] = lista_largura[index]

                    print(f"Cultura atualizada para {cultura_nome}")

                    break

                else:
                    print("Cultura inválida.")

            except ValueError:
                print("Digite apenas números.")

    # Atualizar largura
    elif campo == 2:
        while True:
            try:
                nova_largura = float(input("Digite a nova largura (m): "))
                if nova_largura > 0:
                    lista_largura[index] = nova_largura
                    if lista_culturas[index] == "Milho":
                        lista_comprimento[index] = nova_largura
                    break
                else:
                    print("O valor deve ser positivo.")
            except ValueError:
                print("Digite um número válido.")

    # Atualizar comprimento
    elif campo == 3:
        while True:
            try:
                novo_comprimento = float(input("Digite o novo comprimento (m): "))
                if novo_comprimento > 0:
                    lista_comprimento[index] = novo_comprimento
                    if lista_culturas[index] == "Milho":
                        lista_largura[index] = novo_comprimento
                    break
                else:
                    print("O valor deve ser positivo.")
            except ValueError:
                print("Digite um número válido.")

    # Recalcular área
    forma = lista_formas[index]
    largura = lista_largura[index]
    comprimento = lista_comprimento[index]

    try:
        lista_area[index] = calcular_area(forma, largura, comprimento)
    except Exception as e:
        print(f"Erro ao recalcular área: {e}")
        return

    # Recalcular insumos se já calculados
    if lista_insumos[index] is not None:
        try:
            total_ml = lista_ruas[index] * lista_comprimento[index] * lista_dose[index]
            lista_insumos[index] = total_ml / 1000
            print(f"Insumos recalculados: {lista_insumos[index]:.2f} litros")
        except Exception as e:
            print(f"Erro ao recalcular insumos: {e}")

    print(f"\nÁrea atualizada: {lista_area[index]:.2f} m²")


def deletar_plantacao():
    print("\n===== DELETAR PLANTAÇÃO =====\n")

    if len(lista_culturas) == 0:
        print("Nenhuma plantação cadastrada.")
        return

    # Se houver apenas uma plantação
    if len(lista_culturas) == 1:
        index = 0
        print(
            f"Plantação única encontrada: {lista_culturas[0]} (Área: {lista_area[0]:.2f} m²)"
        )
    else:
        # Mostrar plantações disponíveis
        for i, cultura in enumerate(lista_culturas):
            print(f"[{i+1}] - {cultura} (Área: {lista_area[i]:.2f} m²)")

        # Escolher plantação
        while True:
            try:
                escolha = int(
                    input("Digite o número da plantação que deseja deletar: ")
                )
                if 1 <= escolha <= len(lista_culturas):
                    index = escolha - 1
                    break
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Digite apenas números.")

    # Confirmar exclusão
    confirmacao = input(
        f"Tem certeza que deseja deletar a plantação '{lista_culturas[index]}'? (s/n): "
    )
    if confirmacao.lower() == "s":
        del lista_culturas[index]
        del lista_formas[index]
        del lista_largura[index]
        del lista_comprimento[index]
        del lista_area[index]
        del lista_ruas[index]
        del lista_dose[index]
        del lista_insumos[index]
        print("Plantação deletada com sucesso.")
    else:
        print("Operação cancelada.")


def calcular_manejo_insumo():
    print("\n===== CALCULAR MANEJO DE INSUMOS =====\n")

    if len(lista_culturas) == 0:
        print("Nenhuma plantação cadastrada.")
        return

    # Mostrar plantações
    for i, cultura in enumerate(lista_culturas):
        print(f"[{i+1}] - {cultura} (Área: {lista_area[i]:.2f} m²)")

    while True:
        try:
            escolha = int(input("Digite o número da plantação: "))
            if 1 <= escolha <= len(lista_culturas):
                index = escolha - 1
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite apenas números.")

    # Menu de insumos
    print("\nEscolha o tipo de insumo:")
    print("[1] Fertilizante")
    print("[2] Pesticida")
    print("[3] Fosfato")
    print("[4] Nitrogênio")
    print("[5] Potássio")
    print("[6] Enxofre")
    print("[7] Cálcio")

    while True:
        try:
            insumo_escolha = int(input("Digite o número do insumo: "))

            if 1 <= insumo_escolha <= 7:
                insumos = [
                    "Fertilizante",
                    "Pesticida",
                    "Fosfato",
                    "Nitrogênio",
                    "Potássio",
                    "Enxofre",
                    "Cálcio",
                ]

                insumo = insumos[insumo_escolha - 1]
                break

            else:
                print("Opção inválida.")

        except ValueError:
            print("Digite apenas números.")

    # Entrada de dados
    while True:
        try:
            ruas = int(input("Quantas ruas possui a lavoura? "))
            if ruas > 0:
                break
            else:
                print("O número de ruas deve ser positivo.")
        except ValueError:
            print("Digite um número inteiro válido.")
    while True:
        try:
            dose = float(input(f"Digite a dose de {insumo} (mL por metro): "))
            if dose > 0:
                break
            else:
                print("A dose deve ser positiva.")
        except ValueError:
            print("Digite um número válido.")

    # Cálculo
    try:
        total_ml = ruas * lista_comprimento[index] * dose
        total_litros = total_ml / 1000
    except Exception as e:
        print(f"Erro no cálculo: {e}")
        return

    # Guardar nos vetores
    lista_ruas[index] = ruas
    lista_dose[index] = dose
    lista_insumos[index] = total_litros

    print(f"\nTotal de {insumo} necessário: {total_litros:.2f} litros")


def consultar_dados_meteorologicos():
    import subprocess
    import os

    print("\n===== DADOS METEOROLÓGICOS =====\n")

    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    script_r = os.path.join(pasta_atual, "..", "r", "open_api.r")

    resultado = subprocess.run(
        ["Rscript", script_r],
        capture_output=True,
        text=True,
        encoding="utf-8",
        cwd=os.path.dirname(script_r),
    )

    if resultado.stdout:
        print(resultado.stdout)

    if resultado.stderr:
        print("Erro ao executar script R:")
        print(resultado.stderr)


def exportar_csv():

    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(pasta_atual, "..", "data", "dados_farmtech.csv")

    with open(caminho_csv, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Cultura",
                "Área (m²)",
                "Ruas",
                "Dose (mL/m)",
                "Total Insumo (litros)",
            ]
        )

        for i in range(len(lista_culturas)):
            writer.writerow(
                [
                    lista_culturas[i],
                    f"{lista_area[i]:.2f}",
                    lista_ruas[i] if lista_ruas[i] is not None else "N/A",
                    lista_dose[i] if lista_dose[i] is not None else "N/A",
                    (
                        f"{lista_insumos[i]:.2f}"
                        if lista_insumos[i] is not None
                        else "N/A"
                    ),
                ]
            )

    print("Dados exportados para 'data/dados_farmtech.csv' com sucesso.")
