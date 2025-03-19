def exibir_menu():
    print("Bem vindo, ja se cadastrou?")
    print("1 - Cadastro")
    print("2 - Verificar cadastro")
    print("3 - Sair")
    print("--------------------------------")

def cadastrar_pessoa (cadastros):
    nome = input("Nome")
    idade = input("Idade")
    turma = input("Turma")
    curso = input("Curso")
    cadastros.append({"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso})
    print("Cadastro realizado com sucesso")