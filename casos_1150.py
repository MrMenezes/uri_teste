#Ultrapassando Z
casos = [{'entrada': '3 \n1 \n20\n', 'saida': '5\r\n'}]

'''Descricao:Faa um programa que leia dois inteiros: X e Z (devem ser lidos tantos valores para Z quantos necessrios, at que seja digitado um valor maior do que X para ele). Conte quantos nmeros inteiros devem ser somados em sequncia (considerando o X nesta soma) para que a soma ultrapasse a Z o mnimo possvel. Escreva o valor final da contagem.   
                    A entrada pode conter, por exemplo, os valores 21 21 15 30. Neste caso,  ento assumido o valor 21 para X enquanto os valores 21 e 15 devem ser desconsiderados pois so menores ou iguais a X. Como o valor 30 est dentro da especificao (maior do que X) ele ser vlido e ento deve-se processar os clculos para apresentar na sada o valor 2, pois  a quantidade de valores somados para se produzir um valor maior do que 30 (21 + 22).'''

'''Entrada:A entrada contm somente valores inteiros, um por linha, podendo ser positivos ou negativos. O primeiro valor da entrada ser o valor de X. A prxima linha da entrada ir conter Z. Se Z no atender a especificao do problema, ele dever ser lido  novamente, tantas vezes quantas forem necessrias.'''

'''Saida:Imprima uma linha com um nmero inteiro que representa a quantidade de nmeros inteiros que devem ser somadas, de acordo com a especificao acima.'''