clientes = [
        ('Ana', 'xxx', 'xxx@gmail.com'),
        ('João', 'yyy', 'yyygmail.com'),
    ]

for nome, cpf, email in clientes:
    if '@' in email:
        print(f'Email válido para {nome}')
    else:
        print(f'Email inválido para {nome}')