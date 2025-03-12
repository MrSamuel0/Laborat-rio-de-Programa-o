programa 
{
  inclua biblioteca Matematica --> mat

  funcao inicio() 
  {
    inteiro esc, l, a
    real lado, r

    escreva("Rotina que calcula a área de algumas formas.\n")

    escreva("Digite 1 para quadrado, 2 para círculo e 3 para retângulo: ")
    leia(esc)

    enquanto (esc != 1 e esc != 2 e esc != 3)
    {
      escreva("O valor digitado é inválido\n")

      escreva("Digite 1 para quadrado, 2 para círculo e 3 para retângulo: ")
      leia(esc)
    }

    se (esc == 1)
    {
      escreva("Digite o valor do lado: ")
      leia(lado)

      escreva("A área do quadrado é: ", areaQuadrado(lado))
    }

    senao se (esc == 2)
    {
      escreva("Digite o valor do raio: ")
      leia(r)

      escreva("A área do círculo é: ", areaCirculo(r))
    }

    senao se (esc == 3)
    {
      escreva("Digite o valor da largura: ")
      leia(l)

      escreva("Digite o valor da altura: ")
      leia(a)

      enquanto (l == a)
      {
        escreva("Os valores que você digitou não são compativeis a um retângulo\n")

        escreva("Digite novamente o valor da largura: ")
        leia(l)

        escreva("Digite novamente o valor da altura: ")
        leia(a)
      }

      escreva("A área do retângulo é: ", areaRetangulo(l, a))
    }
  }

  funcao real areaQuadrado (real l)
  {
    retorne mat.potencia(l, 2.0)
  }

  funcao real areaCirculo (real raio)
  {
    real raioQuadrado = mat.potencia(raio, 2.0)
    real area = (2 * 3.14) + raioQuadrado
    retorne area
  }

  funcao inteiro areaRetangulo (inteiro b, inteiro a)
  {
    retorne a * b
  }
}
