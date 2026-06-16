# =====================================================
# PROJECTO FINAL - ANÁLISE DE DADOS LABORATORIAIS
# =====================================================

# 1. IMPORTAÇÃO DAS BIBLIOTECAS
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# 2. IMPORTAÇÃO DOS DADOS
# =====================================================

df = pd.read_csv("lab_limpo.csv")

print("Primeiras linhas:")
print(df.head())

print("\nInformações gerais:")
print(df.info())

# =====================================================
# 3. LIMPEZA DOS DADOS
# =====================================================

# Verificar valores nulos
print("\nValores nulos:")
print(df.isnull().sum())

# Remover duplicados
df = df.drop_duplicates()

# Converter data para formato datetime
df["data_teste"] = pd.to_datetime(df["data_teste"])

print("\nDados limpos com sucesso!")

# =====================================================
# 4. TRANSFORMAÇÕES
# =====================================================

# Extrair mês
df["mes"] = df["data_teste"].dt.month

# Extrair ano
df["ano"] = df["data_teste"].dt.year

# Criar categoria para valor CT
df["nivel_ct"] = pd.cut(
    df["valor_ct"],
    bins=[0, 20, 30, 50],
    labels=["Baixo", "Médio", "Alto"]
)

print("\nTransformações concluídas!")

# =====================================================
# 5. AGREGAÇÕES
# =====================================================

# Quantidade de testes por patógeno
patogenos = df.groupby("patogeno").size()

print("\nTestes por patógeno:")
print(patogenos)

# Resultado dos testes
resultados = df.groupby("resultado").size()

print("\nResultados:")
print(resultados)

# Média de valor CT por patógeno
media_ct = df.groupby("patogeno")["valor_ct"].mean()

print("\nMédia do Valor CT:")
print(media_ct)

# Testes por laboratório
laboratorios = df.groupby("laboratorio").size()

print("\nTestes por laboratório:")
print(laboratorios)

# =====================================================
# 6. TABELAS RESUMO
# =====================================================

tabela_resumo = df.groupby(
    ["patogeno", "resultado"]
).size().reset_index(name="quantidade")

print("\nTabela Resumo:")
print(tabela_resumo)

# Exportar tabela resumo
tabela_resumo.to_csv(
    "tabela_resumo.csv",
    index=False
)

# =====================================================
# 7. VISUALIZAÇÕES
# =====================================================

# Gráfico 1 - Patógenos
plt.figure(figsize=(8,5))
patogenos.plot(kind="bar")
plt.title("Quantidade de Testes por Patógeno")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig("artefatos/grafico_patogenos.png")
plt.show()

# Gráfico 2 - Resultados
plt.figure(figsize=(6,6))
resultados.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Distribuição dos Resultados")
plt.ylabel("")
plt.savefig("artefatos/grafico_resultados.png")
plt.show()

# Gráfico 3 - Laboratórios
plt.figure(figsize=(8,5))
laboratorios.plot(kind="bar")
plt.title("Testes por Laboratório")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig("artefatos/grafico_laboratorios.png")
plt.show()

# =====================================================
# 8. EXPORTAÇÃO FINAL
# =====================================================

df.to_csv(
    "dataset_tratado.csv",
    index=False
)

print("\nArquivos exportados:")
print("- dataset_tratado.csv")
print("- tabela_resumo.csv")
print("- grafico_patogenos.png")
print("- grafico_resultados.png")
print("- grafico_laboratorios.png")

# =====================================================
# FIM DO PROJECTO
# =====================================================