import pickle

class SalvadorDeDados:
    def salvar(self, contatos, nome_arquivo="contatos.pkl"):
        with open(nome_arquivo, "wb") as f:
            pickle.dump(contatos, f)

    def carregar(self, nome_arquivo="contatos.pkl"):
        try:
            with open(nome_arquivo, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []
