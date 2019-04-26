# Trabalho 1 - Algoritmos de criptografia


Primeiramente foi usado uma função da biblioteca "Simple Crypt" para fazer uma criptografia simples da mensagem enviada o IP de destino.
Posteriomente, utilizamos o algoritmo de criptografia AES, como sugerido em sala pelo professor, 
fizemos a comparação do tempo de encriptação, envio e decriptação com o algoritmo da bibliteca "Simple Crytpt".

Prinmeira observação: o AES exige um tamanho de chave múltiplo de 16bytes, sendo este o menor tamanho, enquanto a 
simple crypt não exige tamanho minimo de chave.

Segunda observação: O AES mostrou-se bem mais rápido tanto da encriptação quanto na decriptção.
