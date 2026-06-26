def calcular_tarifa_consumo(consumo: float) -> float:
  """Cálculo do valor da base da tarifa usando faixas progressivas."""
  if consumo <= 100: # Faixa 1: Até 100 kWh -> cosip isento
    valor_base = consumo * 0.85
  elif consumo > 100 and consumo <= 200: # Faixa 2: De 101 a 200 kWh -> cosip = 10,67 reais
    valor_base = (consumo * 0.85) + 10.67
  elif consumo > 200 and consumo <= 300: # Faixa 3: de 201 a 300 kWh -> cosip = 21,33 reais
    valor_base = (consumo * 0.85) + 21.33
  elif consumo > 300 and consumo <= 500: # Faixa 4: de 301 a 500 kWh -> cosip = 32,00 reais
    valor_base = (consumo * 0.85) + 32.00
  elif consumo > 500 and consumo <= 1000: # Faixa 5: de 501 a 1000 kWh -> cosip = 53,33 reais
    valor_base = (consumo * 0.85) + 53.33
  elif consumo > 1000 and consumo <= 1500: # Faixa 6: de 1001 a 1500 kWh -> cosip = 80,00 reais
    valor_base = (consumo * 0.85) + 80.00
  elif consumo > 1500 and consumo <= 2000: # Faixa 7: de 1501 a 2000 kWh -> cosip = 106,65
    valor_base = (consumo * 0.85) + 106.65
  else: # Faixa 8: acima de 2000 kWh -> cosip = 122,65 reais
    valor_base = (consumo * 0.85) + 122.65

  return valor_base


def calcular_adicional_bandeira(consumo: float, bandeira: str) -> float:
  """Calcula o custo adicional baseado na bandeira tarifária."""
  bandeira = bandeira.lower().strip()

  if bandeira == "verde":
    adicional_por_kwh = 0.00
  elif bandeira == "amarela" or bandeira == "amarelo":
    adicional_por_kwh = 0.01885  # R$ 1,885 a cada 100 kWh
  elif bandeira == "laranja":
    adicional_por_kwh = 0.04463  # R$ 4,463 a cada 100 kWh
  elif bandeira == "vermelho" or bandeira == "vermelha":
    adicional_por_kwh = 0.07877  # R$ 7,877 a cada 100 kWh
  else:
    print("Bandeira inválida! Considerando bandeira Verde por padrão.")
    adicional_por_kwh = 0.00

  return consumo * adicional_por_kwh


def calcular_conta_total(consumo: float, bandeira: str) -> float:
  """Une o cálculo da tarifa baseado no consumo com a bandeira tarifária."""
  tarifa_base = calcular_tarifa_consumo(consumo)
  adicional_bandeira = calcular_adicional_bandeira(consumo, bandeira)
  return tarifa_base + adicional_bandeira


def simular_troca_eletrodomestico(consumo_atual: float, bandeira: str) -> None:
  """Simula o impacto da troca de um aparelho ineficiente por um mais eficente."""
  print("\n" + "="*20 + " SIMULADOR DE TROCA " + "="*20)
  potencia_antiga = float(input("Potência do aparelho antigo (em Watts): "))
  potencia_nova = float(input("Potência do aparelho novo (em Watts): "))
  horas_uso_diario = float(input("Horas de uso estimado por dia: "))

  # Cálculo do consumo mensal (30 dias) de cada um em kWh, Fórmula: (Watts * horas * dias) / 1000
  consumo_antigo = (potencia_antiga * horas_uso_diario * 30) / 1000
  consumo_novo = (potencia_nova * horas_uso_diario * 30) / 1000

  # Novo consumo total da casa
  novo_consumo_total = consumo_atual - consumo_antigo + consumo_novo

  # Cálculos financeiros
  custo_atual = calcular_conta_total(consumo_atual, bandeira)
  novo_custo = calcular_conta_total(novo_consumo_total, bandeira)
  economia_reais = custo_atual - novo_custo
  economia_kwh = consumo_atual - novo_consumo_total

  # Exibição dos resultados formatados
  print("\n" + "-"*15 + " RESULTADO DA SIMULAÇÃO " + "-"*15)
  print(f"Consumo do aparelho antigo: {consumo_antigo:.2f} kWh/mês")
  print(f"Consumo do aparelho novo:   {consumo_novo:.2f} kWh/mês")
  print(f"Redução no consumo total:   {economia_kwh:.2f} kWh")
  print(f"Conta Atual:                R$ {custo_atual:.2f}")
  print(f"Nova Conta Estimada:        R$ {novo_custo:.2f}")

  if economia_reais > 0:
    print(f"Economia mensal estimada: R$ {economia_reais:.2f}")
  elif economia_reais < 0:
    print(f"Atenção: O novo aparelho vai aumentar sua conta em R$ {abs(economia_reais):.2f}")
  else:
    print("A troca não alterou o valor do consumo.")


# --- FLUXO PRINCIPAL DO PROGRAMA ---
def main():
  print("="*15 + " SISTEMA DE TARIFAS DE ENERGIA " + "="*15)

  # Entradas do usuário
  consumo_usuario = float(input("Digite o consumo do mês (em kWh): "))
  bandeira_usuario = input("Digite a bandeira tarifária (Verde, Amarela, Laranja ou Vermelha): ")

  # Processamento da conta atual
  conta_atual = calcular_conta_total(consumo_usuario, bandeira_usuario)

  # Saída formatada
  print("\n" + "-"*20 + " SUA CONTA " + "-"*20)
  print(f"Consumo informado: {consumo_usuario:.2f} kWh")
  print(f"Bandeira vigente: {bandeira_usuario.upper()}")
  print(f"Valor total a pagar: R$ {conta_atual:.2f}")

  # Menu de simulação de troca de aparelho
  simular = input("\nDeseja simular a troca de algum eletrodoméstico? (S/N): ").upper().strip()
  if simular == "S":
    simular_troca_eletrodomestico(consumo_usuario, bandeira_usuario)

  print("\nObrigado por utilizar o nosso sistema de cálculo de consumo de energia!")

if __name__ == "__main__":
    main()