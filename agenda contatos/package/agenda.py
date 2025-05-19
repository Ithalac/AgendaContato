from package.contato import ContatoPessoal, ContatoProfissional
from package.persistencia import SalvadorDeDados

class Agenda(SalvadorDeDados):
    def __init__(self):
        self.contatos = self.carregar()
        print("------Agenda inicializada------")
        self.start()

    def start(self):
        self.run = True
        self.loop()

    def loop(self):
        while self.run:
            escolha = input(
                ""
                "========== AGENDA DE CONTATOS ==========\n"
                "  1 - Adicionar novo contato\n"
                "  2 - Listar contatos\n"
                "  3 - Remover contato\n"
                "  4 - Editar contato\n"
                "  5 - Sair do programa\n"
                "========================================\n"

            )

            opcoes = {
                "1": self.criar,
                "2": self.ver,
                "3": self.remover,
                "4": self.editar,
                "5": self.sair
            }

            opcoes.get(escolha, self.warning)()

    def warning(self):
        print(
            "\n========= !ERRO! ===========\n"
            " Opção inválida. Digite novamente.\n"
            "===========================\n"
        )

    def criar(self):
        tipo = input(
            "\n========== TIPO DE CONTATO ==========\n"
            "1 - Pessoal\n"
            "2 - Profissional\n"
            "======================================\n"
        )

        if tipo not in ["1", "2"]:
            print(
                "\n========= !ERRO! ===========\n"
                " Opção inválida.\n"
                "===========================\n"
            )
            return  

        nome = input(
            "\n========== CRIANDO CONTATO ==========\n"
            "Digite o NOME da pessoa:\n"
            "======================================\n"
        )

        if any(char.isdigit() for char in nome):
            print(
                "\n========= !ERRO! ===========\n"
                "Não deve conter números.\n"
                "===========================\n"
            )
            return

        telefone = input(
            "\n========== CRIANDO CONTATO ==========\n"
            "Digite o TELEFONE da pessoa:\n"
            "======================================\n"
        )

        if not telefone.isdigit():
            print(
                "\n========= !ERRO! ===========\n"
                "Deve conter apenas números.\n"
                "===========================\n"
            )
            return

        if tipo == "1":
            nascimento = input(
                "\n========== CRIANDO CONTATO ==========\n"
                "Digite a DATA DE NASCIMENTO (DDMMAAAA):\n"
                "======================================\n"
            )

            if not nascimento.isdigit() or len(nascimento) != 8:
                print(
                    "\n========= !ERRO! ===========\n"
                    "Data inválida. Deve conter 8 dígitos.\n"
                    "===========================\n"
                )
                return

            contato = ContatoPessoal(nome, telefone, nascimento)

        elif tipo == "2":
            empresa = input(
                "\n========== CRIANDO CONTATO ==========\n"
                "Digite a EMPRESA da pessoa:\n"
                "======================================\n"
            )
            contato = ContatoProfissional(nome, telefone, empresa)

        else:
            print(
                "\n========= !ERRO! ===========\n"
                " Tipo inválido.\n"
                "===========================\n"
            )
            return

        self.contatos.append(contato)
        self.salvar(self.contatos)
        print(
            "\n==============================\n"
            " CONTATO SALVO COM SUCESSO\n"
            "==============================\n"
        )

    def ver(self):
        if not self.contatos:
            print(
                "\n========= LISTA DE CONTATOS ===========\n"
                " Nenhum contato salvo.\n"
                "===========================\n"
            )
            return
        for i, contato in enumerate(self.contatos):
            print(f"[{i}] {contato.exibir_info()}")

    def remover(self):
        self.ver()
        try:
            i = int(input(
                "\n========== REMOVENDO CONTATO ==========\n"
                "Digite o número do contato que deseja remover:\n"
                "==============================================\n"
            ))
            del self.contatos[i]
            self.salvar(self.contatos)
            print(
                "\n==============================\n"
                " CONTATO REMOVIDO COM SUCESSO\n"
                "==============================\n"
            )
        except (ValueError, IndexError):
            print(
                "\n========= !ERRO! ===========\n"
                " Índice inválido.\n"
                "===========================\n"
            )

    def editar(self):
        self.ver()
        try:
            i = int(input(
                "\n========= EDITANDO CONTATO ===========\n"
                "Digite o número do contato que deseja editar:\n"
                "=============================================\n"
            ))

            if i < 0 or i >= len(self.contatos):
                raise IndexError
            
            contato = self.contatos[i]
            nome = input(
                f"\n========== EDITANDO CONTATO ==========\n"
                f"Digite o novo NOME do contato\n"
                f"(Atual: {contato.nome})\n"
                f"=======================================\n>> "
            ) or contato.nome

            if any(char.isdigit() for char in nome):
                print(
                    "\n========= !ERRO! ===========\n"
                    "Deve conter números.\n"
                    "===========================\n"
                )
                return

            telefone = input(
                f"\n========== EDITANDO CONTATO ==========\n"
                f"Digite o novo TELEFONE do contato\n"
                f"(Atual: {contato.telefone})\n"
                f"=======================================\n>> "
            ) or contato.telefone

            if not telefone.isdigit():
                print(
                    "\n========= !ERRO! ===========\n"
                    "Deve conter apenas números.\n"
                    "===========================\n"
                )
                return

            if hasattr(contato, 'nascimento'):
                nascimento = input(
                    f"\n========== EDITANDO CONTATO ==========\n"
                    f"Digite a nova DATA DE NASCIMENTO (DDMMAAAA)\n"
                    f"(Atual: {contato.nascimento})\n"
                    f"=======================================\n>> "
                ) or contato.nascimento

                if not nascimento.isdigit() or len(nascimento) != 8:
                    print(
                        "\n========= !ERRO! ===========\n"
                        "Data inválida. Deve conter 8 dígitos.\n"
                        "===========================\n"
                    )
                    return
                
                contato = ContatoPessoal(nome, telefone, nascimento)

            elif hasattr(contato, 'empresa'):
                empresa = input(
                    f"\n========== EDITANDO CONTATO ==========\n"
                    f"Digite a nova EMPRESA do contato\n"
                    f"(Atual: {contato.empresa})\n"
                    f"=======================================\n>> "
                ) or contato.empresa

                contato = ContatoProfissional(nome, telefone, empresa)

            self.contatos[i] = contato
            self.salvar(self.contatos)
            print(
                "\n==============================\n"
                " CONTATO ATUALIZADO COM SUCESSO\n"
                "==============================\n"
            )
        except (ValueError, IndexError):
            print(
                "\n========= !ERRO! ===========\n"
                " Índice inválido.\n"
                "===========================\n"
            )

    def sair(self):
        print("------Agenda finalizada------")
        self.run = False
