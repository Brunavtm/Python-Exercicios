def leiadinheiro(msg):
    while True:
        if msg is int or float:
            break
        else:
            print(f'ERRO! {msg} é um preço inválido.')
