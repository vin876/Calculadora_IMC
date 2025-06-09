def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III (mórbida)"
        
def mostrar_historico(historico):
    print("\n📜 Histórico de Cálculos:")
    for i, entrada in enumerate(historico, 1):
        peso, altura, imc, classificacao = entrada
        print(f"{i}. Peso: {peso} kg | Altura: {altura} m → IMC: {imc:.2f} ({classificacao})")
if __name__ == "__main__":
    
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        print(f"Seu IMC é {imc:.2f} - {classificacao}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        continue

continuar = input("Deseja calcular outro IMC? (s/n): ").strip().lower()
        if continuar != 's':
            break

    if historico:
        mostrar_historico(historico)

from salvar_historico import salvar_historico_txt

# depois de mostrar_historico(historico):
salvar_historico_txt(historico)
print(f"\n📝 Histórico salvo em 'historico_imc.txt'")
