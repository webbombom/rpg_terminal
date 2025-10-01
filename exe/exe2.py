loja_carros = {
    'fusca': {'preco': 15000, 'cor': 'azul'},
    'gol': {'preco': 25000, 'cor': 'preto'},
    'onix': {'preco': 45000, 'cor': 'rosa'}
}

# Consultando o preço e a cor do 'onix'
preco_onix = loja_carros.get('onix', {})
print('onix', preco_onix)

# Atualizando os preços e cores e adicionando o 'civic'
loja_carros.update({
    'onix': {'preco': 47000, 'cor': 'rosa'},
    'civic': {'preco': 90000, 'cor': 'preto'}
})

print(loja_carros, '#civic adicionado')

# Exibindo os preços com 15% de aumento e as cores
for chave, valor in loja_carros.items():
    preco_com_ajuste = valor['preco'] * 1.15
    print(f'key:{chave}: price:{valor["preco"]} -> adjusted price: {preco_com_ajuste}, color: {valor["cor"]}')
