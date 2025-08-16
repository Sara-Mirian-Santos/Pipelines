# Coleta de Dados com API do GitHub usando Requests

O objetivo deste projeto é aplicar os conceitos de consumo de APIs, utilizando a biblioteca `requests` para construir uma **pipeline ETL** que extrai, transforma e armazena dados da **API do GitHub**, com foco nas linguagens de programação utilizadas por grandes empresas.

---

## Bibliotecas Utilizadas

```bash
pip install requests==2.28.2
pip install pandas==2.0.0
```

---

## O que foi aprendido neste projeto

### Bibliotecas e conceitos abordados:

* Uso da biblioteca `requests` para realizar:

  * `GET`
  * `POST`
  * `PUT`
  * `DELETE`
* Autenticação via token na API do GitHub
* Paginação de resultados
* Manipulação de múltiplos **endpoints**
* Tratamento de respostas com diferentes **status codes**
* Estruturação de dados retornados em **JSON**
* Conversão e manipulação com **pandas.DataFrame**
* Codificação de arquivos em **base64** para upload via API

---

## Dicionário

### 🔹 DataFrame

* Estrutura tabular oferecida pela biblioteca `pandas`
* Permite armazenar, filtrar, agrupar e exportar dados com facilidade

### 🔹 Base64

* Utilizado para converter arquivos em sequência de caracteres para envio via requisições HTTP.
* Essencial para uploads de arquivos via API.
