def exibir_menu():
    print("Bem vindo ao menu de cadrastro")
    print("1 - Novo Cadrastro")
    print("2 - Ver cadrastro ")
    print("3 - Sair")
    print("---------------------------")

    def cadrastrar_pessoa (cadrastros):
        nome = input("Nome:")
        idade = input("Idade:")
        turma = input("Turma")
        curso = input("Curso")
        cadrastro.append({"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso })