from gmail_service import buscar_emails_remetente
from extractor_chain import extrair_dados

REMETENTE_LOGISTICO = "seu_fornecedor@email.com"

def main():
    emails = buscar_emails_remetente(REMETENTE_LOGISTICO)

    for email in emails:
        try:
            dados = extrair_dados(email)
            print(dados)
        except Exception as e:
            print("Não foi possível extrair:", e)

if __name__ == "__main__":
    main()
