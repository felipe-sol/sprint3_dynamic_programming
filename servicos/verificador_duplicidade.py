def verificar_duplicidade_recursivo(leads, novo_lead, indice=0):
    if indice >= len(leads):
        return False

    atual = leads[indice]

    if (
        atual.cpf == novo_lead.cpf or
        atual.email == novo_lead.email or
        atual.telefone == novo_lead.telefone
    ):
        return True

    return verificar_duplicidade_recursivo(leads, novo_lead, indice + 1)