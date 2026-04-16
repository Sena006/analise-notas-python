import pandas as pd


def carregar_dados(arquivo):
    """
    Carrega os dados do arquivo Excel.
    """
    return pd.read_excel(arquivo)


def calcular_media(df):
    """
    Calcula a média das notas.
    """
    df["Media"] = (df["Nota1"] + df["Nota2"]) / 2
    return df


def classificar_alunos(df):
    """
    Classifica alunos como Aprovado ou Reprovado.
    """
    df["Classificacao"] = df["Media"].apply(
        lambda media: "Aprovado" if media >= 6 else "Reprovado"
    )
    return df


def mostrar_resultado(df):
    """
    Mostra o resultado final.
    """
    print("\nResultado Final:")
    print(df)


def main():
    arquivo = "analise_python.xlsx"

    dados = carregar_dados(arquivo)
    dados = calcular_media(dados)
    dados = classificar_alunos(dados)

    mostrar_resultado(dados)


if __name__ == "__main__":
    main()