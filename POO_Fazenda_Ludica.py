# Classe base: Animal
class Animal:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return "O animal emite um som."

    def apresentar(self):
        return f"Olá, sou {self.nome} e tenho {self.idade} anos."

# Subclasse: Cachorro
class Cachorro(Animal):
    def _init_(self, nome, idade, raca):
        super()._init_(nome, idade)
        self.raca = raca

    def emitir_som(self):
        return "Au! Au!"

# Subclasse: Gato
class Gato(Animal):
    def _init_(self, nome, idade, cor_pelo):
        super()._init_(nome, idade)
        self.cor_pelo = cor_pelo

    def emitir_som(self):
        return "Miau!"

# Subclasse: Vaca
class Vaca(Animal):
    def _init_(self, nome, idade, producao_leite_litros):
        super()._init_(nome, idade)
        self.__producao_leite_litros = producao_leite_litros  # Encapsulamento

    def emitir_som(self):
        return "Muuu!"

    # Getter
    def obter_producao_leite(self):
        return self.__producao_leite_litros

    # Setter
    def registrar_ordenha(self, litros):
        self.__producao_leite_litros = litros

# --------------------------
# Testes e Demonstração
# --------------------------

# Criando os objetos
cachorro = Cachorro("Rex", 3, "Labrador")
gato = Gato("Mimi", 5, "Branco")
vaca = Vaca("Mimosa", 7, 25.5)

# Apresentação
print(cachorro.apresentar())
print(gato.apresentar())
print(vaca.apresentar())

# Emissão de sons
print(cachorro.emitir_som())
print(gato.emitir_som())
print(vaca.emitir_som())

# Teste de Encapsulamento
print(f"Produção atual de leite: {vaca.obter_producao_leite()} litros")
vaca.registrar_ordenha(28.0)
print(f"Nova produção de leite: {vaca.obter_producao_leite()} litros")