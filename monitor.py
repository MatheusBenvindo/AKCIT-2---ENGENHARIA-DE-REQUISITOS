import time
import random
import requests
from requests.exceptions import RequestException
from typing import Optional, Dict, Any

# Configurações do monitoramento
API_URL = "https://api.exemplo.com/v1/dados"
MAX_RETRIES = 5
BASE_DELAY = 2.0  # Segundos

def fetch_data_with_retry(url: str) -> Optional[Dict[str, Any]]:
    """
    Executa requisição GET na API externa aplicando recuo exponencial.
    """
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, timeout=10.0)
            
            # Sucesso
            if response.status_code == 200:
                return response.json()
            
            # Trata erros temporários (rate limit ou falha no servidor)
            if response.status_code in [429, 500, 502, 503, 504]:
                # Cálculo do delay com recuo exponencial e jitter
                delay = (BASE_DELAY ** attempt) + random.uniform(0.1, 1.0)
                print(f"Status {response.status_code} recebido. Tentativa {attempt + 1}/{MAX_RETRIES} em {delay:.2f}s...")
                time.sleep(delay)
                continue
                
            # Erros permanentes que não aceitam nova tentativa
            print(f"Erro permanente de cliente: HTTP {response.status_code}")
            return None

        except RequestException as e:
            delay = (BASE_DELAY ** attempt) + random.uniform(0.1, 1.0)
            print(f"Erro de conexão ({e}). Tentativa {attempt + 1}/{MAX_RETRIES} em {delay:.2f}s...")
            time.sleep(delay)
            
    print("Número máximo de tentativas atingido. Falha no monitoramento.")
    return None

if __name__ == "__main__":
    print("Iniciando monitoramento da API...")
    dados = fetch_data_with_retry(API_URL)
    if dados:
        print("Dados obtidos com sucesso.")
    else:
        print("Não foi possível obter os dados da API.")
