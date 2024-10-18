class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade
        
    def atualizar_preco(self, novo_preco):
        self._preco = novo_preco
        print("Preço atualizado.\n")
        
    def atualizar_quantidade(self, nova_quantidade):
        self._quantidade = nova_quantidade
        print("Quantidade atualizada.")
        
    def mostrar_info(self):
        print(f"Produto: {self._nome}")
        print(f"Preço unitário: {self._preco}")
        print(f"Quantidade em estoque: {self._quantidade}")
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
    
    @property
    def quantidade(self):
        return self._quantidade
    
    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.preco = novo_preco
        else:
            print("Preço inválido.")
            
    @quantidade.setter
    def quantidade(self, quantidade):
        if quantidade > 0:
            self.quantidade = quantidade
        else:
            print("Quantidade inválida.")