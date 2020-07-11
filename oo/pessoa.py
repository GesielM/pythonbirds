class   Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é  {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3



if __name__ == '__main__':
        renzo = Mutante(nome='Renzo')
        Gesiel = Homem(renzo, nome='Gesiel')
        print(Pessoa.cumprimentar(Gesiel))
        print(id(Gesiel))
        print(Gesiel.cumprimentar())
        print(Gesiel.nome)
        print(Gesiel.idade)
        for filho in Gesiel.filhos:
            print(filho.nome)
        Gesiel.sobrenome = 'Marcelino'
        del Gesiel.filhos
        Gesiel.olhos = 1
        del Gesiel.olhos
        print(Gesiel.__dict__)
        print(renzo.__dict__)
        print(Pessoa.olhos)
        print(Gesiel.olhos)
        print(renzo.olhos)
        print(id(Pessoa.olhos), id(Gesiel.olhos), id(renzo.olhos))
        print(Pessoa.metodo_estatico(), Gesiel.metodo_estatico())
        print(Pessoa.nome_e_atributos_de_classe(), Gesiel.nome_e_atributos_de_classe())
        pessoa = Pessoa('Anonimo')
        print(isinstance(pessoa, Pessoa))
        print(isinstance(pessoa, Homem ))
        print(isinstance(renzo, Pessoa))
        print(isinstance(renzo, Pessoa))
        print(renzo.olhos)
        print(Gesiel.cumprimentar())
        print(renzo.cumprimentar())