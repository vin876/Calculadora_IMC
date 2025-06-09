from datetime import datetime

def salvar_historico_txt(historico, nome_arquivo="historico_imc.txt"):
    with open(nome_arquivo, "a", encoding="utf-8") as f:
        f.write(f"\n📅 Sessão: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        for i, (peso, altura, imc, classificacao) in enumerate(historico, 1):
            f.write(f"{i}. Peso: {peso} kg | Altura: {altura} m → IMC: {imc:.2f} ({classificacao})\n")
        f.write("-" * 50 + "\n")
