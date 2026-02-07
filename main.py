import pandas as pd
from datetime import datetime

from gmail_service import buscar_emails_remetente, criar_evento
from extractor_chain import extrair_dados

REMETENTE_LOGISTICO = ["seufornecedor@gmail.com"]

def main():

    registros = []

    # 🔎 Buscar emails por remetente
    for remetente in REMETENTE_LOGISTICO:
        emails = buscar_emails_remetente(remetente)

        for email in emails:
            try:
                dados = extrair_dados(email)

                # 📅 Formatar data apenas para exibição/Excel
                if dados.data_horario_previsto:
                    data_formatada = dados.data_horario_previsto.strftime("%d/%m/%Y %H:%M")
                else:
                    data_formatada = ""

                # 📦 Guardar dados estruturados
                registros.append({
                    "material": dados.material,
                    "volume": dados.volume,
                    "data_prevista": data_formatada,                  # para Excel/CSV
                    "data_datetime": dados.data_horario_previsto      # para Calendar API
                })

            except Exception as e:
                print("Não foi possível extrair:", e)

    # 🧾 Criar DataFrame
    df = pd.DataFrame(registros)

    # 💾 Salvar CSV
    df.to_csv("programacoes_logisticas.csv", index=False, encoding="utf-8-sig")

    # 💾 Salvar Excel
    nome_arquivo = f"outputs/programacoes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    df.drop(columns=["data_datetime"]).to_excel(nome_arquivo, index=False)

    print("Arquivo salvo com sucesso!")

    # 📅 Criar eventos no Google Agenda
    for registro in registros:
        if registro["data_datetime"]:
            criar_evento(
                registro["data_datetime"],
                registro["material"],
                registro["volume"]
            )


if __name__ == "__main__":
    main()
