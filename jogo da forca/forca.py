palavra_secreta = "girafa"
letras_acertadas = ["_"] * len(palavra_secreta)
tentativas = 6

while tentativas > 0 and "_" in letras_acertadas:
    palpite = input("Digite uma letra: ").lower()

    if palpite in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if palpite == letra:
                letras_acertadas[i] = letra
    else:
        tentativas -= 1
        print(f"Você tem {tentativas} tentativas restantes.")

    print(" ".join(letras_acertadas))

if "_" not in letras_acertadas:
    print("Parabéns, você ganhou!")
else:
    print(f"Fim de jogo! A palavra era: {palavra_secreta}")