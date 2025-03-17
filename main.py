import os
import time
import json
import re
from dotenv import load_dotenv
import pandas as pd
import google.generativeai as genai

class ExtratorInformacoes:
    def __init__(self, api_key, modelo='gemini-2.0-flash'): #configuração e instanciação do modelo
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(modelo)
            print("Extrator de informações inicializado com sucesso.")
        except Exception as e:
            print(f"Erro ao inicializar o extrator: {e}")
            self.model = None

    def extrair(self, conversa):
        if self.model is None:
            return None
        try:
            prompt = f"""
            Extraia as seguintes informações da conversa e retorne em formato JSON:

            {{
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
            }}

            Conversa:
            {conversa}

            Informações extraídas:
            """
            response = self.model.generate_content(prompt)
            # Formata a saída da extração para o formato JSON padrão
            json_str = re.sub(r'```json\n', '', response.text)
            json_str = re.sub(r'\n```', '', json_str)
            # Decodifica o JSON
            dados = json.loads(json_str)
            print("Informações extraídas com sucesso.")
            return dados
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {response.text}")
            print(f"Erro específico: {e}")
            return None
        except Exception as e:
            print(f"Erro ao extrair informações: {e}")
            return None

class ProcessadorLeads:
    def __init__(self, extrator):
        self.extrator = extrator
        print("Processador de leads inicializado com sucesso.")

    def processar_csv(self, df):
        resultados = []
        total_conversas = len(df)
        print(f"Processando {total_conversas} conversas...")
        for index, row in df.iterrows():
            print(f"Processando conversa {index + 1}/{total_conversas}...")
            conversa = row['conversa']
            informacoes = self.extrator.extrair(conversa)
            if informacoes:
                resultados.append(informacoes)
            time.sleep(1) # Delay de 1 segundo entre requisições para não sobrecarregar o uso da API
        print("Processamento de conversas concluído.")
        return resultados

    def salvar_resultados_json(self, resultados, caminho_json):
        try:
            with open(caminho_json, 'w', encoding='utf-8') as f:
                json.dump(resultados, f, ensure_ascii=False, indent=4)
            print(f"Resultados salvos em {caminho_json}")
        except Exception as e:
            print(f"Erro ao salvar resultados em JSON: {e}")

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Erro: Chave de API GEMINI_API_KEY não encontrada no arquivo .env")
    else:
        extrator = ExtratorInformacoes(api_key)
        processador = ProcessadorLeads(extrator)

        input_path = 'data/conversas_leads.csv'
        output_path = 'results/resultados.json'

        try:
            input_df = pd.read_csv(input_path)
            resultados = processador.processar_csv(input_df)
            processador.salvar_resultados_json(resultados, output_path)
        except FileNotFoundError:
            print(f"Erro: Arquivo não encontrado em {input_path}")
        except Exception as e:
            print(f"Erro inesperado: {e}")