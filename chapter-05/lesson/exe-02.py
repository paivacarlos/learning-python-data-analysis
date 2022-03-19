# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos:
# nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe.
# Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class People():
    def __init__(self, name, city, phone, email):
        self.name = name
        self.city = city
        self.phone = phone
        self.email = email
        print("People created!")

    def __str__(self):
        return f"Nome: {self.name}, Cidade: {self.city}, Fone: {self.phone}, Email: {self.email}"

people01 = People("Carlos Paiva", "São Lepoldo", "51-997064415", "paivakk22@gmail.com")
print(people01)
print(getattr(people01, "name"))
print(hash(people01))

people02 = People("Adolfo Paiva", "Porto Alegre", "51-34281836", "adolfo10@gol.com.br")
print(people02)
print(hash(people02))