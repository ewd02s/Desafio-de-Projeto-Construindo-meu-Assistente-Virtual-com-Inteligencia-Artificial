
def calcular_economia_mensal(valor_meta, prazo_meses):
    if valor_meta <= 0 or prazo_meses <= 0:
        raise ValueError("Os valores devem ser maiores que zero.")

    return valor_meta / prazo_meses


valor = float(input("Qual é o valor da sua meta? R$ "))
prazo = int(input("Em quantos meses deseja alcançar a meta? "))

mensal = calcular_economia_mensal(valor, prazo)

print(f"\nVocê precisa guardar R$ {mensal:.2f} por mês.")
print("Simulação sem considerar juros, taxas ou rendimentos.")

