import requests

lista_ceps = ['0985888', '097260000', '011555555']
lista_enderecos = []

for cep in lista_ceps:
    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
    req = requests.get(url, timeout=3)
    endereco = req.json()

    # Create a dictionary with the desired name-value pairs
    formatted_endereco = {
        "cep": endereco["cep"],
        "Endereco": endereco["logradouro"],
        "localidade": endereco["localidade"]
    }

    lista_enderecos.append(formatted_endereco)

for item in lista_enderecos:
    print(item)
