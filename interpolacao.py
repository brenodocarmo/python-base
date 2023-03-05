email_tmpl = """
     Olá, %(nome)s

     Tem interesse em comprar %(produto)s?

     Este produto é ótimo para resolver
     %(texto)s

     Clique agora em %(link)s

     Apenas %(qunatidade)d disponivel!

     Preço proocional %(preco).2f
     """

clientes = ["Maria", "Joao", "Breno"]

for cliente in clientes:
    print(
        email_tmpl
         % {
             'nome': cliente,
             'produto': 'caneta',
             'texto': 'Escreve muito bem',
             'link': 'https://canetaslegais.com',
             'quantidade': 1,
             'preco': 50.50
            }
    )
