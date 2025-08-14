import json
import csv

#necessário definir o path e o tipo dos arquivos

#encoding='utf-8' passo para corrigir o erro de leitura
def leitura_json(path_json):                #assinatura da função
    dados_json = []
    with open(path_json, 'r', encoding='utf-8') as file:
        dados_json = json.load(file)
    return dados_json

def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r', encoding='utf-8') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv

def leitura_dados(path, tipo_arquivo):
    dados = []
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)
    return dados

def get_columns(dados):
    
    return list(dados[0].keys())

def rename_columns(dados, key_mapping):
    new_dados_csv = []
    
    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
        
    return new_dados_csv

def size_data(dados):
  return len(dados)

def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

def transformando_dados_tabela(dados, nomes_colunas):
    dados_combinados_tabela = [nomes_colunas]
    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)
    return dados_combinados_tabela

def salvando_dados(dados, path):
    with open(path, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

path_json = 'Documentos/pipeline_dados/data_raw/dados_empresaA.json'
path_csv = 'Documentos/pipeline_dados/data_raw/dados_empresaB.csv'

#Iniciando a leitura
dados_json = leitura_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_json)
tamanho_dados_json = size_data(dados_json)
print(f'Colunas json: {nome_colunas_json}')
print(f'Quantidade de dados json: {tamanho_dados_json}')

dados_csv = leitura_dados(path_csv, 'csv')
nome_colunas_csv = get_columns(dados_csv)
tamanho_dados_csv = size_data(dados_csv)
print(f'Colunas csv: {nome_colunas_csv}')
print(f'Quantidade de dados csv: {tamanho_dados_csv}')

#Transformação dos dados
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_csv = rename_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(nome_colunas_csv)

#Unificação dos dados
dados_unificados = join(dados_json, dados_csv)
nome_colunas_unificados = get_columns(dados_unificados)
tamanho_dados_unificados = size_data(dados_unificados)
print(f'Colunas unificadas: {nome_colunas_unificados}')
print(f'Quantidade de dados unificados: {tamanho_dados_unificados}')

#Salvando dados
dados_unificados_tabela = transformando_dados_tabela(dados_unificados, nome_colunas_unificados)

path_dados_combinados = 'Documentos/pipeline_dados/data_processed/dados_combinados.csv'

salvando_dados(dados_unificados_tabela, path_dados_combinados)

print(f'Dados salvos com sucesso! {path_dados_combinados}')