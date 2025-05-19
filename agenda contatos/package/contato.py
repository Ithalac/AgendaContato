class Pessoa:
    def __init__(self, nome, telefone,):
        self.nome = nome
        self.telefone = telefone


    def exibir_info(self):
        return f"{self.nome} - {self.telefone}"

class ContatoPessoal(Pessoa):
    def __init__(self, nome, telefone, aniversario):
        super().__init__(nome, telefone,)
        self.aniversario = aniversario

    def exibir_info(self):
        return super().exibir_info() + f" - Aniversário: {self.aniversario}"

class ContatoProfissional(Pessoa):
    def __init__(self, nome, telefone, empresa):
        super().__init__(nome, telefone,)
        self.empresa = empresa

    def exibir_info(self):
        return super().exibir_info() + f" - Empresa: {self.empresa}"
