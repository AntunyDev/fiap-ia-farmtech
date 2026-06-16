import functions as fcs
import subprocess

subprocess.run(["chcp", "65001"], capture_output=True, shell=True)

while True:

    fcs.mostrar_menu()
    op = fcs.ler_opcao()

    if op == 1:
        fcs.inserir_plantacao()
        fcs.limpar_terminal()

    elif op == 2:
        fcs.mostrar_dados()
        fcs.limpar_terminal()

    elif op == 3:
        fcs.atualizar_plantacao()
        fcs.limpar_terminal()

    elif op == 4:
        fcs.deletar_plantacao()
        fcs.limpar_terminal()

    elif op == 5:
        fcs.calcular_manejo_insumo()
        fcs.limpar_terminal()

    elif op == 6:
        fcs.exportar_csv()
        fcs.limpar_terminal()

    elif op == 7:
        fcs.consultar_dados_meteorologicos()
        fcs.limpar_terminal()

    elif op == 8:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")
