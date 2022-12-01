# Import modules
from words import palavras
import random

# Select Words (In this case words are in Portuguese)
def selecionar_palavra():
  palavra = random.choice(palavras)
  return palavra.upper()

# Start Game
def jogar(palavra):
  #Var Definition
  palavra_a_completar = "_" * len(palavra)
  adivinhou = False
  letras_utilizadas = []
  palavras_utilizadas = []
  tentativas = 6

  #Welcome
  print("Vamos Jogar")
  print(exibir_forca(tentativas))
  print(f"Esta é a palavra: {palavra_a_completar}")

  # looping

  while not adivinhou and tentativas > 0:

    tentativa = input("Digite uma palavra ou letra para continuar: ").upper()

    # only letter
    if len(tentativa) == 1 and tentativa.isalpha():
      if tentativa in letras_utilizadas:
        print("Voce já usou essa letra.")
      elif tentativa not in palavra:
        print(f"A letra {tentativa} não está na palavra.")
        tentativas -= 1
        letras_utilizadas.append(tentativa)
      else:
        print(f"Você acertou! A letra {tentativa} está na palavra.")
        letras_utilizadas.append(tentativa)
        palavra_lista = list(palavra_a_completar)
        indices = [i for i, letra in enumerate(palavra) if letra == tentativa]
        for indice in indices:
          palavra_lista[indice] = tentativa

        palavra_a_completar = "".join(palavra_lista)

        if "_" not in palavra_a_completar:
          adivinhou = True
    
    elif len(tentativa) == len(palavra) and tentativa.isalpha():
      if tentativa in palavras_utilizadas:
        print(f"Você já usou essa palavra{tentativa}")
      elif tentativa != palavra:
        print(f"A palavra {tentativa} está errada.")
        tentativas -= 1
        palavras_utilizadas.append(tentativa)
      else:
        adivinhou = True
        palavra_a_completar = palavra

    else:
      print("Tentativa inválida, tente novamente. ")  
    
    print(exibir_forca(tentativas))
    print(palavra_a_completar)

  if adivinhou:
    print("Parabéns você acertou a palavra.")
  else:
    print(f"GAME OVER. A Palavra era {palavra}.")



# game status
def exibir_forca(tentativas):
  estagios = [  # Game Over
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              # 1
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              # 2
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              # 2
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              # 3
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              # 4
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              # Start
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
  ]

  return estagios[tentativas]

#Start game and continue

def iniciar():
  palavra = selecionar_palavra()
  jogar(palavra)
  while input("Jogar Novamente? S/N: ").upper() == "S":
    palavra = selecionar_palavra()
    jogar(palavra)

iniciar()
