# Extrator de Informações de Leads com Gemini

Este projeto utiliza a API Gemini do Google para extrair informações relevantes de conversas entre um assistente virutal e leads armazenadas em um arquivo CSV.

## Estrutura do Diretório

├── data/
│   └── conversas_leads.csv  # Arquivo de entrada com as conversas
├── results/
│   └── resultados.json      # Arquivo de saída com as informações extraídas
├── .gitignore
├── .env
├── requirements.txt
└── main.py

## Pré-requisitos

* Python 3.6+
* Uma chave de API Gemini (Google Generative AI)

## Configuração da API Key do Google Gemini

1.  **Obtenha sua chave de API:**
    * Acesse o [Google AI Studio](https://makersuite.google.com/).
    * Crie uma conta ou faça login com sua conta Google.
    * Clique no botão Get API Key
    * Clique no botão Criar chave de API
    * Selecione um projeto
    * Clique em Criar uma chave de API em um projeto atual

2.  **Configure o arquivo .env:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Adicione a seguinte linha ao arquivo, substituindo `sua_chave_api_aqui` pela sua chave de API:

    ```
    GEMINI_API_KEY=sua_chave_api_aqui
    ```

## Configuração do Ambiente

1.  Clone o repositório:

    ```bash
    git clone https://github.com/Caio-Lott/desafio-tecnico-morada.ai.git
    cd desafio-tecnico-morada.ai
    ```

2.  Crie um ambiente virtual (recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate  # No Windows
    ```

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Execução

1.  Certifique-se de que o arquivo `conversas_leads.csv` esteja na pasta `data/`.
2.  Execute o script `main.py`:

    ```bash
    python main.py
    ```

3.  As informações extraídas serão salvas no arquivo `resultados.json` na pasta `results/`.

## Formato de Entrada

O arquivo `conversas_leads.csv` deve conter duas colunas:

* `id`: Um número inteiro que identifica a conversa.
* `conversa`: Uma string contendo o texto da conversa do lead.

Exemplo:

```csv
id,conversa
1,"Assistente: Olá! Bem-vindo à Morada.ai. Como posso ajudar você hoje?
Lead: Olá, estou procurando um apartamento em São Paulo.
Assistente: Ótimo! Temos várias opções em São Paulo. Você poderia me dizer em qual região da cidade você tem interesse?
Lead: Estou interessado na região de Pinheiros ou Vila Madalena."
2,"Assistente: Olá! Seja bem-vindo à Morada.ai. Como posso te ajudar hoje?
Lead: Oi, estou procurando uma casa para minha família.
Assistente: Que ótimo! Estamos aqui para ajudar. Você já tem alguma região específica em mente?"
```

## Formato de Saída

O arquivo `resultados.json` conterá uma lista de dicionários, onde cada dicionário representa as informações extraídas de uma conversa. O formato de cada dicionário é o seguinte:

```json
{
    "nome": "Nome do Lead",
    "email": "Email do Lead",
    "telefone": "Telefone do Lead",
    "cidade": "Cidade de interesse",
    "regiao": "Região de interesse",
    "tipo_imovel": "Tipo de imóvel (apartamento, casa, terreno, etc.)",
    "quartos": "Número de quartos",
    "orcamento": "Orçamento",
    "caracteristicas": "Características adicionais (piscina, vaga de garagem, etc.)",
    "disponibilidade": "Disponibilidade para visita",
    "intencao": "Intenção (compra, aluguel, investimento, etc.)"
}
```

## Principais desafio enfrentados

Dentre os desafio enfrentados durante a implementação da solução, destacam-se os 4 principais e mais relevantes:

* Trabalhar com LLMs (Large Language Models) foi um grande aprendizado, pois eu ainda não tinha experiência prática com essa tecnologia. Para superar essa dificuldade, pesquisei bastante, assisti a vídeos e li tutoriais até compreender melhor seu funcionamento e sua integração com a API de IA Generativa.

* Como minha experiência com APIs de IA generativa era limitada, precisei investir um tempo em estudos por meio de tutoriais, vídeos e análise de códigos de terceiros para entender seu uso, principalmente relativo à bibliote específica para Python. 

* Na descrição do desafio, havia a possibilidade do uso da ferramenta LangChain. No entanto, considerando o curto prazo de implementação e meu desconhecimento prévio da ferramenta, optei por manter a abordagem mais básica para garantir um entendimento completo dos conceitos-chave necessários para solucionar o problema. 

* Por fim, o último desagio foi determinar quais informações deveriam ser extraídas para construir uma base de dados realmente útil para o cliente. Essa etapa exigiu análise crítica e um julgamento de quais seriam as principais necessiades dado o mercado imobiliário.

