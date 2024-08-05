# Projeto-IP

Projeto de Introdução à Programação do semestre 2024.1, voltado para a utilização prática dos conhecimentos e ferramentas, com ênfase na Programação Orientada a Objetos aprendidos ao longo da cadeira, assim como da iniciação do trabalho colaborativo com o compartilhamento do código via GitHub e Git para a criação de um Sistema Interativo.

## Título do Projeto >> Cincontre

## Link do repositório no GitHub do projeto: [Link](https://github.com/marisfreire/projetoIP2024.1.git)

## Organização técnica do Código

O código foi dividido em módulos, como aconselhado pelos professores em grandes projetos como esse em questão, os quais estão organizados em:

* **Main**: é o módulo "chefe", ele que inicia o jogo e, para isso, é o responsável por criar a tela em que o jogo passará, além de importar todos os outros módulos do projeto;
* **Config**: contém as configurações básicas do jogo e que serão fixas, como largura e comprimento de tela, taxa de FPS;
* **Monster**: contém as configurações dos monstros do jogo 
* **Player**: contém as configurações do personagem do jogo 
* **Coletaveis**: contém as configurações dos coletaveis do jogo
* **collision**: como a função de check_collision foi muito usada, resolvemos deixa-la separada
* **funções_auxiliares**: contém funções que poderiam ficar fora da main como: a parte de desenho dos corações e do puzzle, além dos butões usados no jogo


## Ferramentas utilizadas

O jogo foi desenvolvido em Python aliado ao Pygame, um conjunto de módulos para essa linguagem, escolhida pelas suas inúmeras ferramentas que permitem a criação de inúmeros jogos, o que foi mais prático para o grupo assim como pelo grande acervo em relação a documentação e tutoriais

## Instalação do Pygame

Para rodar o jogo é necessário ter instalado o [Python3](https://www.python.org/downloads/) e o módulo [Pygame](https://www.pygame.org/news)

Para instalar o Pygame, pode-se usar o comando

```bash
python3 -m pip install -U pygame --user
```
Outra ferramenta importante foi o 
piskel <falar mais sobre >

## Sobre o Projeto


## Contribuidores e suas respectivas funções

* Dayane Carla [Github]() 
    * funcao 1
    * funcao 2
* Giovanna Marques Mafra [Github](https://github.com/GiovannaMafra) 
    * funcao 1
    * funcao 2
* Layla Beatriz [Github](https://github.com/laylabeatriz) 
    * funcao 1
    * funcao 2
* Luma Rios [Github]() 
    * funcao 1
    * funcao 2
* Mariana Freire [Github](https://github.com/marisfreire)
    * funcao 1
    * funcao 2 
* Rafael Mendes Bezerra Xavier [Github](https://github.com/rxavier1904) 
    * funcao 1
    * funcao 2

## Conceitos vistos na disciplina e usados no código

* **Programação Orientada a Objetos**: foi um conceito que tivemos que estudar durante o desenvolvimento do jogo, mas que nos possibilitou dividir o sistema em classes como: player, monster, coletáveis, cada um com seus atributos e métodos, e foi visível a grande importância dessa forma de programação em grandes projetos como esse jogo, pois facilitou a compreensão, organização, compartilhamento de características, funções, etc. 
* **Funções**:  As funções foram amplamente empregadas no código do jogo, especialmente por ser um grande projeto, devido à sua importância na organização e modularização do código. Funções são essenciais para a definição clara de objetivos específicos dentro do desenvolvimento, e evitam a repetição desnecessária de código. Exemplos de sua aplicação no projeto incluem as telas de derrota e vitória, criação do mapa, o loop principal do jogo, verificação de colisões e entre outros.
* **Dicionários**: utilizado para guardar os tipos de coletáveis.
* **Condicionais**: Foi utilizado para saber qual tipo de coletável aconteceu uma colisão, conferir o tipo de eventos nos botões na tela de derrota, conferir se o personagem ainda tem vidas suficientes para a continuação do jogo, ou seja, são unidades fundamentais e estão por quase todos os módulos.

## Desafios e Erros
* **Maior erro**: 
* **Maior desafio**: 
* **Lições aprendidas**: 

