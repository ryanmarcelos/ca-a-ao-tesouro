import random

def introducao():
    print("🏝️ Bem-vindo à Ilha do Tesouro!")
    print("Você tem 3 lugares possíveis para cavar:")
    print("1. Debaixo da palmeira 🌴")
    print("2. Perto das rochas 🪨")
    print("3. Ao lado do barco naufragado 🚤\n")

def jogar():
    locais = ("palmeira", "rochas", "barco")  #tupla 
    tesouro = random.choice(locais)
    tentativas = []

    while True:
        escolha = input("Onde você quer cavar? ").strip().lower()
        if escolha not in locais:
            print("❌ Lugar inválido! Tente: palmeira, rochas ou barco.\n")
            continue

        if escolha in tentativas:
            print("⛏️ Você já cavou aí! Escolha outro lugar.\n")
            continue

        tentativas.append(escolha)

        if escolha == tesouro:
            print(f"💰 Parabéns! Você encontrou o tesouro enterrado sob a {escolha}!")
            break
        else:
            print(f"😬 Nada sob a {escolha}...")
            if len(tentativas) == 3:
                print(f"\n💀 Fim de jogo! O tesouro estava na {tesouro}.")
                break

def jogo():
    introducao()
    jogar()

# Executar o jogo
if __name__ == "__main__":
    jogo()
