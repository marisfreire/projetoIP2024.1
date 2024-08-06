# Projeto-IP

Projeto de Introdução à Programação do semestre 2024.1, voltado para a utilização prática dos conhecimentos e ferramentas, com ênfase na Programação Orientada a Objetos aprendidos ao longo da cadeira, assim como da iniciação do trabalho colaborativo com o compartilhamento do código via GitHub e Git para a criação de um Sistema Interativo.

## Título do Projeto >> Cincontre

## Link do repositório no GitHub do projeto: [Link](https://github.com/marisfreire/projetoIP2024.1.git)

## Organização técnica do Código

O código foi dividido em módulos, como aconselhado pelos professores em grandes projetos como esse em questão, os quais estão organizados em:

* **Main**: é o módulo "chefe", ele que inicia o jogo e, para isso, é o responsável por criar a tela em que o jogo passará, além de importar todos os outros módulos do projeto;
* **Config**: contém as configurações básicas do jogo e que serão fixas, como largura e comprimento de tela, taxa de FPS;
* **Monster**: contém as configurações dos monstros do jogo;
* **Player**: contém as configurações do personagem do jogo;
* **Coletaveis**: contém as configurações dos coletaveis do jogo;
* **collision**: como a função de check_collision foi muito usada, resolvemos deixa-la separada;
* **funções_auxiliares**: contém funções que poderiam ficar fora da main como: a parte de desenho dos corações e do puzzle, além dos butões usados no jogo;
* **Wall**: contém as configurações das paredes do jogo;

## Ferramentas utilizadas

O jogo foi desenvolvido em Python aliado ao Pygame, um conjunto de módulos para essa linguagem, escolhida pelas suas inúmeras ferramentas que permitem a criação de inúmeros jogos, o que foi mais prático para o grupo assim como pelo grande acervo em relação a documentação e tutoriais.

## Instalação do Pygame

Para rodar o jogo é necessário ter instalado o [Python3](https://www.python.org/downloads/) e o módulo [Pygame](https://www.pygame.org/news)

Para instalar o Pygame, pode-se usar o comando

```bash
python3 -m pip install -U pygame --user
```
Outra ferramenta importante foi o Piskel, um editor online de para criação de pixel art e sprites, ou obtidos de bibliotecas de arte da internet e o Tiled é um editor de mapas para desenvolvimentos de jogos. Utilizamo-nos dele para conceber o mapa do nosso jogo


## Sobre o Projeto

Cincontre surgiu da ideia de criar um jogo estilo Pacman que não fosse tão fiel ao clássico e que incorpora o Cin como tema.

Nele, nosso jogador precisa desviar da Procrastinação e conseguir encontrar todos os arquivos para completar seu código antes que o tempo acabe! Para isso, ele pode contar com a ajuda de um bom cafézinho para energizá-lo e ajudá-lo a não perder seu crachá!

## Contribuidores e suas respectivas funções

* Dayane Carla [Github]() 
    * comportamento dos coletáveis.
    * visuais do jogador e do inimigo.
* Giovanna Marques Mafra [Github](https://github.com/GiovannaMafra) 
    * tela de derrota.
    * mecânica do puzzle.
    * relatório.
* Layla Beatriz [Github](https://github.com/laylabeatriz) 
    * tela de vitória e de instruções.
    * timer.
* Luma Rios [Github]() 
    * visual dos coletáveis.
    * movimento e comportamento do jogador.
* Mariana Freire [Github](https://github.com/marisfreire)
    * concepção do mapa.
    * código base.
    * organização do código.
* Rafael Mendes Bezerra Xavier [Github](https://github.com/rxavier1904) 
    * comportamento das vidas.
    * coletável vida.
    * interação player-inimigo.


## Conceitos vistos na disciplina e usados no código

* **Programação Orientada a Objetos**: foi um conceito que tivemos que estudar durante o desenvolvimento do jogo, mas que nos possibilitou dividir o sistema em classes como: player, monster, coletáveis, cada um com seus atributos e métodos, e foi visível a grande importância dessa forma de programação em grandes projetos como esse jogo, pois facilitou a compreensão, organização, compartilhamento de características, funções, etc. 
* **Funções**:  As funções foram amplamente empregadas no código do jogo, especialmente por ser um grande projeto, devido à sua importância na organização e modularização do código. Funções são essenciais para a definição clara de objetivos específicos dentro do desenvolvimento, e evitam a repetição desnecessária de código. Exemplos de sua aplicação no projeto incluem as telas de derrota e vitória, criação do mapa, o loop principal do jogo, verificação de colisões e entre outros.
* **Dicionários**: utilizado para guardar os tipos de coletáveis.
* **Condicionais**: Foi utilizado para saber qual tipo de coletável aconteceu uma colisão, conferir o tipo de eventos nos botões na tela de derrota, conferir se o personagem ainda tem vidas suficientes para a continuação do jogo, ou seja, são unidades fundamentais e estão por quase todos os módulos.
* **Listas**: utilizadas para guardar imagens das vidas e do puzzle.

## Desafios e Erros
* **Maior erro**: Certamente, um dos principais desafios enfrentados foi a organização e o gerenciamento do tempo. Como para a maioria dos membros do grupo esta foi a primeira experiência em desenvolvimento de software colaborativo, utilizando ferramentas como o Git, não tivemos uma compreensão clara sobre o tempo necessário para o desenvolvimento e implementação de cada componente do jogo. Isso resultou em um período de idealização mais longo do que inicialmente previsto.
* **Maior desafio**: A principal dificuldade enfrentada no projeto foi, sem dúvida, a falta de familiaridade e segurança no uso das ferramentas Git e GitHub para a produção coletiva do código. Até então, estávamos acostumados a desenvolver de forma individual, o que tornou essa transição desafiadora. Para superar essa dificuldade, foi necessário adotar uma organização rigorosa na separação das tarefas e manter uma comunicação constante entre os membros da equipe, garantindo que todos estivessem cientes do progresso e das atualizações realizadas no código, especialmente quando era feito um push.
* **Lições aprendidas**: Este projeto foi extremamente valioso, tanto no aspecto técnico quanto no desenvolvimento de habilidades pessoais. Ele nos proporcionou a oportunidade de aplicar na prática os conceitos aprendidos na disciplina e de adquirir novos conhecimentos, como a importância da programação orientada a objetos e o uso de ferramentas como o Git. Além disso, tivemos a chance de vivenciar o processo de construção de um software de maneira mais profissional, indo além das atividades propostas no Dikastis. No âmbito das soft skills, o projeto nos permitiu desenvolver competências essenciais, como comunicação, organização e planejamento, que foram fundamentais para o sucesso do trabalho em equipe.

## Créditos
* **Trilha sonora**: Jazzy Frenchy - Benjamin Tissot [bensound.com](https://www.bensound.com/royalty-free-music/track/jazzy-frenchy-upbeat-funny), coletou.mp3, fail.mp3, botao.mp3 e vitoria.mp3 [Pixabay](https://pixabay.com/)
* **Fontes**: Upheaval e Big Pixel (Versão Demo) [Dafont](https://www.dafont.com/pt/)

