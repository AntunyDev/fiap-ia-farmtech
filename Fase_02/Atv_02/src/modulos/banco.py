import oracledb
import os
from dotenv import load_dotenv
from rich import print as rprint
from rich.table import Table

from pathlib import Path
env_path = Path(__file__).resolve().parent.parent.parent / "config" / ".env"
load_dotenv(dotenv_path=env_path)

DB_USER     = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DSN      = os.getenv("DB_DSN")


def conectar():
    try:
        conexao = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
        return conexao
    except oracledb.DatabaseError as e:
        rprint(f"[bold yellow]Erro ao conectar no banco:[/bold yellow] [green]{e}[/green]")
        return None


def inicializar_banco():
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE talhoes (
                        id           VARCHAR2(8)   PRIMARY KEY,
                        nome         VARCHAR2(100) NOT NULL,
                        area_ha      NUMBER(10,2)  NOT NULL,
                        variedade    VARCHAR2(50),
                        municipio    VARCHAR2(100),
                        ano_plantio  NUMBER(4)
                    )';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN RAISE; END IF;
            END;
        """
        )

        cursor.execute(
            """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE colheitas (
                        id                  VARCHAR2(20)  PRIMARY KEY,
                        talhao_id           VARCHAR2(8)   REFERENCES talhoes(id),
                        talhao_nome         VARCHAR2(100),
                        ano_safra           NUMBER(4),
                        metodo              VARCHAR2(20),
                        producao_esperada   NUMBER(12,2),
                        perda_percentual    NUMBER(5,2),
                        perda_toneladas     NUMBER(12,2),
                        producao_real       NUMBER(12,2),
                        preco_tonelada      NUMBER(10,2),
                        prejuizo            NUMBER(14,2),
                        data_registro       VARCHAR2(20)
                    )';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN RAISE; END IF;
            END;
        """
        )

        conexao.commit()
        rprint("[bold green]Banco inicializado com sucesso.[/bold green]")

    except oracledb.DatabaseError as e:
        rprint(f"[bold yellow]Erro ao inicializar banco:[/bold yellow] [green]{e}[/green]")
    finally:
        conexao.close()


def salvar_talhao(talhao):
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute(
            """
            MERGE INTO talhoes t
            USING (SELECT :id AS id FROM dual) src
            ON (t.id = src.id)
            WHEN MATCHED THEN
                UPDATE SET nome = :nome, area_ha = :area_ha,
                           variedade = :variedade, municipio = :municipio,
                           ano_plantio = :ano_plantio
            WHEN NOT MATCHED THEN
                INSERT (id, nome, area_ha, variedade, municipio, ano_plantio)
                VALUES (:id, :nome, :area_ha, :variedade, :municipio, :ano_plantio)
        """,
            {
                "id": talhao["id"],
                "nome": talhao["nome"],
                "area_ha": talhao["area_ha"],
                "variedade": talhao["variedade"],
                "municipio": talhao["municipio"],
                "ano_plantio": talhao["ano_plantio"],
            },
        )
        conexao.commit()
        rprint("[bold green]Talhão salvo no banco.[/bold green]")

    except oracledb.DatabaseError as e:
        rprint(f"[bold yellow]Erro ao salvar talhão:[/bold yellow] [green]{e}[/green]")
    finally:
        conexao.close()


def salvar_colheita(colheita):
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute(
            """
            MERGE INTO colheitas c
            USING (SELECT :id AS id FROM dual) src
            ON (c.id = src.id)
            WHEN MATCHED THEN
                UPDATE SET perda_percentual = :perda_percentual,
                           perda_toneladas  = :perda_toneladas,
                           prejuizo         = :prejuizo
            WHEN NOT MATCHED THEN
                INSERT (id, talhao_id, talhao_nome, ano_safra, metodo,
                        producao_esperada, perda_percentual, perda_toneladas,
                        producao_real, preco_tonelada, prejuizo, data_registro)
                VALUES (:id, :talhao_id, :talhao_nome, :ano_safra, :metodo,
                        :producao_esperada, :perda_percentual, :perda_toneladas,
                        :producao_real, :preco_tonelada, :prejuizo, :data_registro)
        """,
            {
                "id": colheita["id"],
                "talhao_id": colheita["talhao_id"],
                "talhao_nome": colheita["talhao_nome"],
                "ano_safra": colheita["ano_safra"],
                "metodo": colheita["metodo"],
                "producao_esperada": colheita["producao_esperada"],
                "perda_percentual": colheita["perda_percentual"],
                "perda_toneladas": colheita["perda_toneladas"],
                "producao_real": colheita["producao_real"],
                "preco_tonelada": colheita["preco_tonelada"],
                "prejuizo": colheita["prejuizo"],
                "data_registro": colheita["data_registro"],
            },
        )
        conexao.commit()
        rprint("[bold green]Colheita salva no banco.[/bold green]")

    except oracledb.DatabaseError as e:
        rprint(f"[bold yellow]Erro ao salvar colheita:[/bold yellow] [green]{e}[/green]")
    finally:
        conexao.close()


def listar_talhoes_bd():
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id, nome, area_ha, variedade, municipio, ano_plantio FROM talhoes ORDER BY nome"
        )
        linhas = cursor.fetchall()

        if not linhas:
            rprint("[yellow]Nenhum talhão no banco de dados.[/yellow]")
            return

        table = Table(title="Talhões no Banco de Dados Oracle", header_style="bold yellow", border_style="green")
        table.add_column("ID", style="yellow")
        table.add_column("Nome", style="green")
        table.add_column("Área", style="yellow", justify="right")
        table.add_column("Variedade", style="green")
        table.add_column("Município", style="green")
        table.add_column("Plantio", style="yellow", justify="center")

        for linha in linhas:
            table.add_row(
                linha[0], 
                linha[1], 
                f"{linha[2]:.2f} ha", 
                linha[3], 
                linha[4], 
                str(linha[5])
            )
        
        rprint(table)

    except oracledb.DatabaseError as e:
        print(f"Erro ao consultar talhões: {e}")
    finally:
        conexao.close()


def listar_colheitas_bd():
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute(
            """
            SELECT id, talhao_nome, ano_safra, metodo,
                   producao_esperada, perda_percentual, prejuizo
            FROM colheitas
            ORDER BY ano_safra DESC
        """
        )
        linhas = cursor.fetchall()

        if not linhas:
            rprint("[yellow]Nenhuma colheita no banco de dados.[/yellow]")
            return

        table = Table(title="Colheitas no Banco de Dados Oracle", header_style="bold yellow", border_style="green")
        table.add_column("ID", style="yellow")
        table.add_column("Talhão", style="green")
        table.add_column("Safra", style="yellow", justify="center")
        table.add_column("Método", style="green")
        table.add_column("Prod.Esp.", style="yellow", justify="right")
        table.add_column("Perda%", style="yellow", justify="right")
        table.add_column("Prejuízo", style="bold yellow", justify="right")

        for linha in linhas:
            table.add_row(
                linha[0],
                linha[1],
                str(linha[2]),
                linha[3],
                f"{linha[4]:.2f} t",
                f"{linha[5]:.2f}%",
                f"R$ {linha[6]:.2f}"
            )
        
        rprint(table)

    except oracledb.DatabaseError as e:
        print(f"Erro ao consultar colheitas: {e}")
    finally:
        conexao.close()
