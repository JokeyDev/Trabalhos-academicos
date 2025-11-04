class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


class CarrinhoDeCompra:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao seu carrinho.")

    def remover_produto(self, nome_produto: str):
        for produto in self.produtos:
            if produto.nome.lower() == nome_produto.lower():
                self.produtos.remove(produto)
                print(f"Produto '{produto.nome}' removido do carrinho.")
                return
        print(f"Produto '{nome_produto}' não encontrado no carrinho.")

    def listar_produtos(self):
        if not self.produtos:
            print("Carrinho vazio.")
        else:
            print("Produtos no carrinho:")
            for produto in self.produtos:
                print(f"- {produto}")

    def calcular_total(self):
        total = sum(produto.preco for produto in self.produtos)
        return total


# Exemplo de uso do código
if __name__ == "__main__":
    p1 = Produto("Notebook", 3500.00)
    p2 = Produto("Mouse", 70.00)
    p3 = Produto("Teclado", 100.00)

    carrinho = CarrinhoDeCompra()

    carrinho.adicionar_produto(p1)
    carrinho.adicionar_produto(p2)
    carrinho.adicionar_produto(p3)

    carrinho.listar_produtos()

    carrinho.remover_produto("Mouse")

    carrinho.listar_produtos()

    print(f"Total da compra: R$ {carrinho.calcular_total():.2f}")
