#Programação Orientada a Objetos
class Cachorros:
#método(construtor) que permite criar varios obejtos de uma mesma class, os paramêntros são os atributos
    def __init__(self,nome, cor_de_pelo,idade, tamanho):
        self.nome=nome
        self.cor_de_pelo= cor_de_pelo
        self.idade= idade
        self.tamanho= tamanho
    #método 
    def latir(self):
        print('au au') 
    def correr(self):
        print(f'{self.nome} esta correndo')       

#Instanciando um objeto (criando um obejto)
cachorros_1= Cachorros('Toby','marrom', 5,'grande')

'''
print(cachorros_1.nome)
print(cachorros_1.idade)
cachorros_1.idade =8
print(cachorros_1.idade)

'''
#chamando o método do objeto cachorro
cachorros_1.latir()
cachorros_1.correr()


cachorros_2= Cachorros('Max','preto',3,'pequeno')
