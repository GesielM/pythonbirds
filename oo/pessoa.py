class   Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
        renzo = Pessoa(nome='Renzo')
        Gesiel = Pessoa(renzo, nome='Gesiel')
        print(Pessoa.cumprimentar(Gesiel))
        print(id(Gesiel))
        print(Gesiel.cumprimentar())
        print(Gesiel.nome)
        print(Gesiel.idade)
        for filho in Gesiel.filhos:
            print(filho.nome)
        Gesiel.sobrenome = 'Marcelino'
        del Gesiel.filhos
        print(Gesiel.__dict__)
        print(renzo.__dict__)

