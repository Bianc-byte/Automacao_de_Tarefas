import pandas as pd
from pathlib import Path

# Definir pastas
INPUT_DIR = Path("data/input")

def carregar_csvs(pasta: Path) -> pd.DataFrame:
    # Procurar todos os arquivos .csv dentro da pasta
    arquivos = list(pasta.glob("*.csv"))

    if not arquivos:
        print(f"Nenhum CSV encontrado em: {pasta.resolve()}")
        return pd.DataFrame()  # retorna vazio

    # Guardar as tabelas lidas
    tabelas = []
    for arq in arquivos:
        print(f"Lendo arquivo: {arq.name}")
        df = pd.read_csv(arq)
        df["__arquivo"] = arq.name  # opcional: marcar de qual arquivo veio
        tabelas.append(df)

    # Juntar todos os CSVs em um só DataFrame
    df_final = pd.concat(tabelas, ignore_index=True)
    return df_final

def main():
    df = carregar_csvs(INPUT_DIR)
    if df.empty:
        print("Nada para processar. Coloque CSVs em data/input.")
        return
    
    print("\nPré-visualização dos dados:")
    print(df.head())  # mostra as 5 primeiras linhas

if __name__ == "__main__":
    main()
    