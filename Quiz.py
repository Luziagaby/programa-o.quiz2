# Escola: Instituto Federal de Educação, ciencia e Tecnologia rio grande do norte.
# Disciplina: Quiz de Programação
# Turma: INFOR1m
# Alunos: Luzia Graziellz Gomes de Carvalho
# professora: pricila

def menu_principal():
    print("\nMenu de Opções:")
    print("1. Responder quiz de Alvin e os Esquilos")
    print("2. Responder quiz de Turma da Mônica")
    print("3. Responder quiz de As Aventuras de Ladybug")
    print("4. Sair")

def calcular_percentual(acertos, total_perguntas):
    return (acertos / total_perguntas) * 100

def quiz_alvin():
    perguntas = [
        {"pergunta": "Quem é o líder dos Esquilos?",
         "opcoes": ["a) Alvin", "b) Simon", "c) Theodore", "d) Dave"],
         "resposta": "a"},
        {"pergunta": "Qual o nome do pai adotivo dos Esquilos?",
         "opcoes": ["a) Thomas", "b) Dave", "c) Michael", "d) Alan"],
         "resposta": "b"},
        {"pergunta": "Qual é o esquilo mais inteligente?",
         "opcoes": ["a) Alvin", "b) Simon", "c) Theodore", "d) Jeanette"],
         "resposta": "b"},
        {"pergunta": "Qual é o esquilo mais fofo?",
         "opcoes": ["a) Alvin", "b) Simon", "c) Theodore", "d) Eleanor"],
         "resposta": "c"}
    ]
    return realizar_quiz(perguntas)

def quiz_monica():
    perguntas = [
        {"pergunta": "Qual é o principal personagem da Turma da Mônica?",
         "opcoes": ["a) Cebolinha", "b) Cascão", "c) Mônica", "d) Magali"],
         "resposta": "c"},
        {"pergunta": "Qual o nome do coelhinho da Mônica?",
         "opcoes": ["a) Sansão", "b) Bugu", "c) Floquinho", "d) Mingau"],
         "resposta": "a"},
        {"pergunta": "Quem é o melhor amigo do Cebolinha?",
         "opcoes": ["a) Cascão", "b) Chico Bento", "c) Bidu", "d) Zé Lelé"],
         "resposta": "a"},
        {"pergunta": "Qual personagem tem medo de tomar banho?",
         "opcoes": ["a) Cebolinha", "b) Cascão", "c) Magali", "d) Mônica"],
         "resposta": "b"}
    ]
    return realizar_quiz(perguntas)

def quiz_Ladybug():
    perguntas = [
        {"pergunta": "Quem é o protagonista de As Aventuras de Ladybug?",
         "opcoes": ["a) Marinete", "b) Edrien", "c) Ladybug", "d) tikki"],
         "resposta": "c"},
        {"pergunta": "Qual é o objetivo de Ladybug em suas aventuras?",
         "opcoes": ["a) Encontrar tesouros", "b) Ajudar amigos", "c) Descobrir novos mundos", "d) Lutar contra vilões"],
         "resposta": "b"},
        {"pergunta": "Qual o nome do melhor amiga de Ladybug?",
         "opcoes": ["a) tikki", "b) alya", "c) kagami tisurigi", "d) Chloé Bourgeois"],
         "resposta": "b"},
        {"pergunta": "Onde Ladybug vive suas aventuras?",
         "opcoes": ["a) paris", "b) No espaço", "c) Na floresta", "d) No mar"],
         "resposta": "a"}
    ]
    return realizar_quiz(perguntas)

def realizar_quiz(perguntas):
    acertos = 0
    for pergunta in perguntas:
        print(f"\n{pergunta['pergunta']}")
        for opcao in pergunta["opcoes"]:
            print(opcao)
        resposta = input("Digite a letra da resposta correta: ").lower()
        if resposta == pergunta["resposta"]:
            acertos += 1
    total_perguntas = len(perguntas)
    percentual_acertos = calcular_percentual(acertos, total_perguntas)
    print(f"\nVocê acertou {acertos} de {total_perguntas} perguntas.")
    print(f"Percentual de acertos: {percentual_acertos}%")
    return percentual_acertos

def main():
    while True:
        menu_principal()
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            quiz_alvin()
        elif escolha == "2":
            quiz_monica()
        elif escolha == "3":
            quiz_Ladybug()
        elif escolha == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
main()