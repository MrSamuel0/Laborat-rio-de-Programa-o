programa {
  funcao inicio() {
    real nota, nota1, media

    escreva("Digite a nota 1: ")
    leia(nota)

    escreva("Digite a nota 2: ")
    leia(nota1)

    media = (nota + nota1) / 2

    se (nota >= 7 e media <= 10) 
    {
      escreva("Você passou!")
    }

    senao se (media <= 6.9 e media >= 5.0)
    {
      escreva("Recuperação!")
    }

    senao se (nota <= 4.9)
    {
      escreva("Reprovado!")
    }

    senao
    {
      escreva("Você digitou um valor inválido!!")
    }
  }
}

programa {
  funcao inicio() {
    inteiro x, y

    escreva("Digite um número: ")
    leia(x)

    escreva("Digite outro número: ")
    leia(y)

    se (x > y)
    {
      escreva(x, " é maior que ", y)
    }

    senao se (y > x)
    {
      escreva(y, " é maior que ", x)
    }

    senao
    {
      escreva(x, " é igual a ", y)
    }
  }
}

programa {
  funcao inicio() {
    real larg, comp, per, area

    escreva("Digite o comprimento do terreno: ")
    leia(comp)

    escreva("Digite a largura do terreno: ")
    leia(larg)

    per = (larg * 2) + (comp * 2)
    area = larg * comp

    se (area < 100 )
    {
      escreva("Terreno popular")
      
    }
  }
}

