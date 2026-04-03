def melhor_agendamento(intervalos, indice=0, memo=None):
    if memo is None:
        memo = {}

    if indice >= len(intervalos):
        return 0

    if indice in memo:
        return memo[indice]

    pular = melhor_agendamento(intervalos, indice + 1, memo)

    fim_atual = intervalos[indice][1]
    proximo = indice + 1

    while proximo < len(intervalos) and intervalos[proximo][0] < fim_atual:
        proximo += 1

    pegar = 1 + melhor_agendamento(intervalos, proximo, memo)

    memo[indice] = max(pular, pegar)
    return memo[indice]