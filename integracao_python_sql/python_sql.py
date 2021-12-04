def atualiza_sql(gestora: str, rentabilidade_dia: float):
    # Importações
    import pyodbc

    # Dados para conexão
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=PC-do-Gui;"
        "Database=BrasilCapitalDB;"
        )

    # Tentando fazer a conexão com o banco
    try: 
        conexao = pyodbc.connect(dados_conexao)
        print("Conexão bem sucedida!")
        cursor = conexao.cursor()
    except:
        raise print("Ocorreu um erro ao se conectar com o banco")

    # Comando SQL a ser executado
    comando = f"""
            UPDATE CotasDiarias 
            SET rentabilidade_dia={rentabilidade_dia} 
            WHERE gestora='{gestora}'"""

    # Tentando executar o comando
    try: 
        cursor.execute(comando)
        cursor.commit()
        print(f"Rentabilidade diária da {gestora} foi atualizado!\n")
    except:
        raise print("Ocorreu um erro ao executar o comando")


if __name__ == '__main__':
    atualiza_sql()