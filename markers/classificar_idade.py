def classifica_idade(idade):
    if idade < 13:
        return 'crianca'
    if idade < 20:
        return 'adolescente'
    if idade < 60:
        return 'adulto'
    return 'idoso'