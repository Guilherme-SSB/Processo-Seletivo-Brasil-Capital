def atualiza_sql(gestora: str, rentabilidade_dia: float):
    """Dado a gestora e o valor de rentabilidade diária adquirida, 
    realiza uma query de UPDATE ao banco de dados em SQL Server"""

    # Importações
    import pyodbc
    from config import dados_conexao

    # Tentando fazer a conexão com o banco
    try: 
        print('Estabelecendo conexão com o banco de dados')
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
        print(f"Rentabilidade diária da {gestora} foi atualizada (SQL Server)!\n\n")
    except:
        raise print("Ocorreu um erro ao executar o comando")


if __name__ == '__main__':
    atualiza_sql()