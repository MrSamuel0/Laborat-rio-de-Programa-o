programa {
  funcao inicio() {
    // 1.Elabore um algoritmo que leia um número inteiro e mostre o seu antecessor e seu sucessor.
    
    //inteiro num, ant, suc
    
    escreva("digite um número: ")
    leia(num)   
     
    ant = num - 1
    suc = num + 1
    
    escreva("o antecessor é: ", ant)
    escreva("\no sucessor é: ", suc)*/

    // 2.Elabore um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte.

    real num, dob, ter
    
    escreva("digite um número: ")
    leia(num)
    
    dob = num * 2
    ter = num / 3
    
    escreva("o dobro é: ", dob)
    escreva("\na terça parte é: ", ter)

    // 3.Elabore um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$5,15.
    
    real dindin, dol
    
    escreva("dgite a quantidade de dinheiro: ")
    leia(dindin)
    
    dol = dindin / 5.15
    
    escreva("voce pode comprar: ", dol, "$")
    
    // 4.Elabore um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados.
    
    real alt, lar, area, qtd
    
    escreva("digite a altura da parede: ")
    leia(alt)
    
    escreva("digite a largura da parede: ")
    leia(lar)
    
    area =  alt * lar
    qtd = area / 2
    
    escreva("a área é: ", area)
    escreva("\nserão necessários ", qtd, "litros de tinta")

    
    // 5.Elabore um algoritmo que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.

    real prec, prom
    
    escreva("qual é o preço do produto? ")
    leia(prec)
    
    prom = prec - (prec * 0.05)
    
    escreva("o preço promocional é: ", prom)

    // 6.Elabore um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.

    real sal, augm

    escreva("digite o seu salário: ")
    leia(sal)

    augm = sal + (sal * 0.15)

    escreva("o valor do reajuste salarial ficou em: ", augm, "R$")
  }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1667; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */