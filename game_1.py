import random
from english_words import english_words_lower_alpha_set


def pendu_de_lol():
    mot_secret = random.choice(list(english_words_lower_alpha_set))
    taille = len(mot_secret)
    trous = ["_" for _ in range(taille)]
    vies_restantes = 12

    while vies_restantes > 0:
        print(" ".join(trous), "/", vies_restantes, "vies au compteur")
        guess_crazy = input("Tape une lettre ou tente le gros mot: ").lower()

        if len(guess_crazy) > 1:
            if guess_crazy == mot_secret:
                trous = list(mot_secret)
                print("".join(trous))
                print("Respect, t’as deviné direct")
                break
            else:
                print("Non mais t’abuses, c’est pas ça")
                vies_restantes -= 5
        elif len(guess_crazy) == 1:
            if guess_crazy in mot_secret:
                for pos_fun in range(taille):
                    if mot_secret[pos_fun] == guess_crazy:
                        trous[pos_fun] = guess_crazy
            else:
                print(f"La lettre {guess_crazy} existe même pas là-dedans")
                vies_restantes -= 1

        if "_" not in trous:
            print("".join(trous))
            print("Gagnééé, t’es trop forte")
            break

    if vies_restantes == 0:
        print(f"Perdu... le mot c’était \"{mot_secret}\"")


pendu_de_lol()
