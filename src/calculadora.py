def calcular_economia_mensal(valor_meta, prazo_meses):
    """
    Calcula quanto deve ser economizado por mês
    para alcançar uma meta em determinado prazo.

    A simulação não considera juros, taxas ou rendimentos.
    """
    if valor_meta <= 0:
        raise ValueError("O valor da meta deve ser maior que zero.")

    if prazo_meses <= 0:
        raise ValueError("O prazo deve ser maior que zero.")

    return valor_meta / prazo_meses


def formatar_reais(valor):
    """
    Formata um número para apresentação em reais.
    """
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
