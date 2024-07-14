def classifica_idade(idade):
    if idade < 12:
        return 'crianca'
    if idade < 18:
        return 'adolescente'
    if idade < 60:
        return 'adulto'
    return 'idoso'