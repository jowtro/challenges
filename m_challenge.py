#!/usr/bin/python3

def get_vigent_facts(facts, schema):

    # extract the tuples with joao
    if(schema[0][0] == "endereço" and schema[0][2] == 'one'):
        list_with_falses = [t for t in facts if not t[3]]
        list_joao_endereco = [t for t in facts if t[0]== 'joão' and t[1] == 'endereço']
        joao_current_address = list_joao_endereco[:: -1][0]
        list_final = [t for t in facts if t[3] and not (t[0] == 'joão' and t[1] == 'endereço')]
        # list on reverse and get the first element (the current tuple with endereco)
        list_final.append(joao_current_address)
        # iterate over list_with_falses to remove the respective elements in list_final
        for tupla in list_with_falses:
            lista_aux = list(tupla)
            lista_aux[3] = True
            list_final.remove(tuple(lista_aux))

        list_final.sort()
    # IMPORTANT just for better visualization on console.
    # FINAL RESULT!
    for elem in list_final:
        print(elem)
    # print("latest joao address {}".format(joao_address))


if __name__ == "__main__":
    facts = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua alice, 10', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '234-5678', True),
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', False),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True),
    ]
    schema = [
        ('endereço', 'cardinality', 'one'),
        ('telefone', 'cardinality', 'many')
    ]
    get_vigent_facts(facts, schema)
