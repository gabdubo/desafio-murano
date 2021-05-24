import pandas as pd


def inserir(dre, curso, nome, genero, data_nascimento, altura, peso, cra, creditos_obtidos, renda):
    global alunos_df

    alunos_dict = {'Dre': dre, 'Curso': curso, 'Nome': nome, 'Gênero': genero, 'Data de Nascimento': data_nascimento,
                   'Altura': altura, 'Peso': peso, 'CRA': cra, 'Créditos Obtidos': creditos_obtidos, 'Renda': renda}

    alunos_df = alunos_df.append(alunos_dict, ignore_index=True)
    alunos_df.to_csv('alunos.csv', index=False)


def contagem(nome_coluna=None, igual=None, maior_que=None, menor_que=None):
    global alunos_df

    if nome_coluna is not None:
        if igual is not None:
            alunos_df = alunos_df.where(alunos_df[nome_coluna] == igual)
        if maior_que is not None:
            alunos_df = alunos_df.where(alunos_df[nome_coluna] > maior_que)
        if menor_que is not None:
            menor_que = float(menor_que)
            alunos_df = alunos_df.where(alunos_df[nome_coluna] < menor_que)

        count = alunos_df.count()
    else:
        count = len(alunos_df.index)
    print('Contagem:')
    print(count)
    return count


def media(nome_coluna):
    assert nome_coluna not in ['Dre', 'Curso', 'Nome', 'Gênero', 'Data de Nascimento']

    mean = alunos_df.filter([nome_coluna]).mean(axis=0)
    print('Média:')
    print(mean)
    return mean


def desvio_padrao(nome_coluna):
    assert nome_coluna not in ['Dre', 'Curso', 'Nome', 'Gênero', 'Data de Nascimento']

    std = alunos_df.filter([nome_coluna]).std(axis=0)
    print('Desvio padrão:')
    print(std)
    return std

alunos_df = pd.read_csv('alunos.csv')
# contagem()
# contagem(nome_coluna='Gênero', igual='feminino')
# contagem(nome_coluna='CRA', maior_que=5)
# contagem(nome_coluna='Peso', menor_que=60)
# media(nome_coluna='Renda')
# desvio_padrao('CRA')
