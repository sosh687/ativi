def exibir_menu():
    print("Bem vindo ao menu de cadrastro")
    print("1 - Cadastro")
    print("2 - Verificar cadastro")
    print("3 - Sair")
    print("--------------------------------")

def cadastrar_pessoa (cadastros):
    nome  = input("Nome:")
    idade = input("Idade:")
    turma = input("Turma:")
    curso = input("Curso:")
    cadastros.append({"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso})
    print("Cadastro realizado com sucesso!")

def ver_cadrastros (cadrastros):
    if not cadrastros: 
       print("Nenhum cadrastro no sistema.")
    else:
         print("/n ------ LISTA DE CADRASTROS ------")

         for i, pessoa in enumerate (cadrastros, 1):
                print(f"(i). Nome: {pessoa['Nome']}, Idade:{pessoa['Idade']}, Turma: {pessoa['Turma']}, Curso: {pessoa['Curso']}")
    
                
def main():
     cadrastros = []
     while True:
         exibir_menu()
         opção = input("Escolha uma opção: ")
         if opção == "1":
             cadastrar_pessoa (cadrastros)
         elif opção == "2":
             ver_cadrastros (cadrastros)
         
         elif opção == "3":
            print("Obrigado por ultilizar o nosso sitema!")
            break  
         else:
           print("Opção incorreta Tente novamente")


if __name__ == "__main__":
  main()
