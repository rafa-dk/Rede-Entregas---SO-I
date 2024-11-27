# Rede-Entregas---SO-I
Projeto final da disciplina de Sistemas Operacionais I
Integrantes:
Rafael Daiki Kaneko
Ryan Hideki Tadeo Guimarães

Para cumprir os requisitos abordados na prorposta do projeto, tomamos uma abordagem mais modularizada, separando caminhão, encomenda e posto de encomenda em scripts, e classes diferentes, com seus métodos próprios.
Inspirados nos exemplos passados em sala de aula, como a situação "produtor/consumidor", utilizamos mutex para bloquear e permitir que apenas 1 caminhão executasse as ações de pegar/entregar encomendas. O uso deste, permite uma maior segurança e controle de quem está acessando aqueles recursos, evitando condições de corrida. Adicionalmente, utilizamos semáforos (mais especificamente, na classe Caminhao) para definir se o caminhão possui ou não espaços para pegar ou descarregar as encomendas, garantindo que o numero de encomendas nunca ultrapasse o valor máximo permitido.

A classe Encomenda segue o mesmo padrão de modularidade, com vários getters e setters, a fim de melhor comunicação entre os objetos, além de possuir a função escreverArq (), que guarda os dados de toda sua jornada, desde sua chegada num dos postos, até sua coleta, e por fim, sua entrega.

A classe Posto Encomenda, representa os pontos de distribuição das mesmas, onde os caminhões irão interagir e entrar na fila caso haja algo para eles fazerem.

