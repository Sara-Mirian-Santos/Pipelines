from processando_dados import Dados

path_json = 'Documentos/pipeline_dados/data_raw/dados_empresaA.json'
path_csv = 'Documentos/pipeline_dados/data_raw/dados_empresaB.csv'

dados_empresaA = Dados(path_json, 'json')
print(f'Caminho da pasta da empresa A: {dados_empresaA.dados}')

dados_empresaB = Dados(path_csv, 'csv')
print(f'Caminho da pasta da empresa B: {dados_empresaB.dados}')

dados_empresaA = Dados(path_json, 'json')
print(f'Nome das colunas da empresa A: {dados_empresaA.nome_colunas}')
print(f'Quantidade de linhas {dados_empresaA.qtd_linhas}')

dados_empresaB = Dados(path_csv, 'csv')
print(f'Nome das colunas  da empresa B: {dados_empresaB.nome_colunas}')
print(f'Quantidade de linhas {dados_empresaB.qtd_linhas}')

#Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)

dados_combinados = Dados.join(dados_empresaA, dados_empresaB)
print (dados_combinados)

#Load

path_dados_combinados = 'Documentos/pipeline_dados/data_processed/dados_combinados.csv'
dados_combinados.salvando_dados(path_dados_combinados)
print(f'Arquivo salvo com sucesso no caminho: {path_dados_combinados}')