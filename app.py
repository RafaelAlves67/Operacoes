import pandas as pd

df = pd.read_excel('Operacoes.xlsx') 

newBet = [
    {
        "Jogo": "Cruzeiro x Liberta",
        "Aposta": "over 2.5 gols",
        "Odd": "1.80",
        "Unidade": "1 UN",
        "Valor": "20$",
        "Data": "2024-09-19"
    },
    {
        "Jogo": "Atletico x Liberta",
        "Aposta": "over 2.5 gols",
        "Odd": "1.80",
        "Unidade": "1 UN",
        "Valor": "20$",
        "Data": "2024-09-19"
    },
    {
        "Jogo": "Atletico x Flamengo",
        "Aposta": "over 2.5 gols",
        "Odd": "1.80",
        "Unidade": "1 UN",
        "Valor": "20$",
        "Data": "2024-09-19"
    },
    {
        "Jogo": "Cruzeiro x Liberta",
        "Aposta": "over 2.5 gols",
        "Odd": "1.80",
        "Unidade": "1 UN",
        "Valor": "20$",
        "Data": "2024-09-19"
    },
    {
        "Jogo": "Atletico x Liberta",
        "Aposta": "over 2.5 gols",
        "Odd": "1.80",
        "Unidade": "1 UN",
        "Valor": "20$",
        "Data": "2024-09-19"
    },
    {
        "Jogo": "Atletico x Flamengo",
        "Aposta": "over 2.5 gols",
        "Odd": "1.80",
        "Unidade": "1 UN",
        "Valor": "20$",
        "Data": "2024-09-19"
    },
    {
        "Jogo": "Cruzeiro x Liberta",
        "Aposta": "over 2.5 gols",
        "Odd": "1.80",
        "Unidade": "1 UN",
        "Valor": "20$",
        "Data": "2024-09-19"
    },
    {
        "Jogo": "Atletico x Liberta",
        "Aposta": "over 2.5 gols",
        "Odd": "1.80",
        "Unidade": "1 UN",
        "Valor": "20$",
        "Data": "2024-09-19"
    },
    {
        "Jogo": "Atletico x Flamengo",
        "Aposta": "over 2.5 gols",
        "Odd": "1.80",
        "Unidade": "1 UN",
        "Valor": "20$",
        "Data": "2024-09-19"
    },
    {
        "Jogo": "Cruzeiro x Liberta",
        "Aposta": "over 2.5 gols",
        "Odd": "1.80",
        "Unidade": "1 UN",
        "Valor": "20$",
        "Data": "2024-09-19"
    },
    {
        "Jogo": "Atletico x Liberta",
        "Aposta": "over 2.5 gols",
        "Odd": "1.80",
        "Unidade": "1 UN",
        "Valor": "20$",
        "Data": "2024-09-19"
    },
    {
        "Jogo": "Atletico x Flamengo",
        "Aposta": "over 2.5 gols",
        "Odd": "1.80",
        "Unidade": "1 UN",
        "Valor": "20$",
        "Data": "2024-09-19"
    },
]

# Gerando uma tabela com novos dados
newBet_DF = pd.DataFrame(newBet)

# Adicionando dados 
planilhaAlimentada = pd.concat([df, newBet_DF], ignore_index=True)


# Salvando planilha atualizada
planilhaAlimentada.to_excel("Operacoes.xlsx", index=False)


#Começando a análise de dados....
planilhaAlimentada 


# Houve um erro de inserção, odds cruzeiro 2.50 

planilhaAlimentada.loc[planilhaAlimentada["Jogo"].str.contains('Cruzeiro'), "Odd"] = "2.50" 


#Média das odds 
media_odds = float(planilhaAlimentada["Odd"].mean()) 
media_odds

#filtrando dados nulos 
dados_nulos = planilhaAlimentada.isnull()

#filtrando dados não nulos
dados_nao_nulos = planilhaAlimentada.notnull()
dados_nao_nulos 
planilhaAlimentada[dados_nao_nulos]

# Alterando dados nulos para determinada string
planilhaAlimentada = planilhaAlimentada.fillna(value="Não tem valores")
planilhaAlimentada.to_excel("Operacoes.xlsx") 

# procurando indices com esses valores
indices_remove = planilhaAlimentada[planilhaAlimentada["Aposta"] == "Não tem valores"].index 
indices_remove

#excluindo 
planilhaAlimentada = planilhaAlimentada.drop(indices_remove)
planilhaAlimentada 

planilhaAlimentada["Jogo"].str.contains("Atletico").value_counts() 
planilhaAlimentada["Jogo"].value_counts()




