---
title: Máquinas de Turing
description: A definição mais básica de um computador
date: 2023-08-03
modified: 2023-08-03
tags: turing,máquina,computador,definição,instrução,algoritmo,fita,cabeça,alfabeto,genérico,propósito
---
# <i class="fa-solid fa-computador"></i> Máquinas de Turing - A Definição Mais Básica de um Computador

## <i class="fa-solid fa-triangle-exclamation"></i> Atenção

> A maior parte das coisas que escrevi está em formato livre e toda a tradução foi feita diretamente por mim. Claro, eu fiz minha pesquisa e deixei os links com as fontes no texto mas não leve o conteúdo tão a sério: eu não sou um cientista da computação muito menos um pesquisador.
**Em caso de dúvida, consulte as fontes**. Obrigado e que o show continue!

## <i class="fa-solid fa-list-ul"></i> Índice
- [Afinal, quem é Turing?](#afinal-quem-é-turing)
- [O Que São Essas Coisas?](#o-que-são-essas-coisas)
    - [Algoritmos](#algoritmos)
    - [Computador de Propósito Genérico](#computador-de-propósito-genérico)
    - [Máquina de Turing](#máquina-de-turing)
        - [O que é a Máquina](#o-que-é-a-máquina)
        - [O Alfabeto](#o-alfabeto)
        - [A Fita](#a-fita)
        - [A Cabeça](#a-cabeça)
- [Mas Por Que Devo me Importar?](#mas-por-que-devo-me-importar)
    - [Isso é Realmente Importante Para um Programador?](#isso-é-realmente-importante-para-um-programador)

___
## <i class="fa-solid fa-person-circle-question"></i> Afinal, quem é Turing?
> Nossos mortos nunca morrem pra nós, até que esqueçamos deles. - [George Elliot](https://www.brainyquote.com/quotes/george_eliot_148896)

**Alan Mathison Turing** foi um [matemático, cientista da computação, lógico, criptoanalista, filósofo e biólogo teórico inglês](https://en.wikipedia.org/wiki/Alan_Turing).

Ele foi um dos responsáveis pela criação e desenvolvimento da ciência da computação por definir conceitos como **algoritmos** e **computador de propósito genérico** via **Máquina de Turing**.

É incrível pensar que muito da sociedade moderna que vivemos ainda é baseada em conceitos que Turing pensou a quase um século atrás.

## <i class="fa-regular fa-circle-question"></i> O Que São Essas Coisas?

### <i class="fa-solid fa-code-branch"></i> Algoritmos

#### <i class="fa-solid fa-shuffle"></i> **[TL;DR](https://www.urbandictionary.com/define.php?term=tl%3Bdr)**

`Algoritmos` a são definição, passo-a-passo, de como resolver um problema.

É como se fosse uma receita: se você seguir os passos corretamente, na mesma ordem que foram apresentados e usando os mesmos ingredientes e medidas, você tem um resultado igual e constante todas as vezes.

#### <i class="fa-solid fa-scroll"></i> A Versão Extendida

Um `Algoritmo` é uma lista de instruções extremamente específicas que devem ser seguidas à risca e em ordem para a resolução de um problema.

Essas instruções podem conter condições e até interagir com outros `Algoritmos`, desde que todos os `algoritmos` tenham a definição de um estado final, ou seja, eventualmente eles vão finalizar com sucesso ou não.

Se você usa `Facebook`, `TikTok`, `YouTube` ou qualquer outra mídia social, você provavelmente já conhece a existência dos `Algoritmos de Recomendação`. Esses são `algoritmos` proprietários que podem ser considerados parte do cérebro dessas aplicações.

Eu acho que o Instituto Internacional de Geneva tem uma explicação muito melhor que a minha sobre `algoritmos` [aqui](https://www.iig.ch/en-en/blog/computer-science/algorithm-computer-science-definition-and-understanding) (texto em inglês).

### <i class="fa-solid fa-server"></i> Computador de Propósito Genérico

No passado a computação era usada como uma forma de executar cálculos mais rápido do que qualquer humano. Porém, esses computadores tinham uma lógica extremamente específica, de forma que eles não podiam ser reprogramados para executar cálculos diferentes daqueles para os que foram projetados em primeiro lugar.

Essa limitação, bem como a grande complexidade e tamanhos gigantescos, fez com que essas máquinas fossem muito caras e difíceis de manter, como é explicado na história do primeiro computador genérico, [o ENIAC](https://penntoday.upenn.edu/news/worlds-first-general-purpose-computer-turns-75).

Tudo isso significava que eram necessários `algoritmos` extremamente específicos para máquinas extremamente específicas. Não era possível simplesmente atualizar a lógica e re-executar. Seria necessário realinhar partes do computador ou até ter que usar uma máquina completamente diferente, o que podia ser um impeditivo.

A ideia de ter uma única máquina capaz de executar `algoritmos` diferentes, sem a necessidade de qualquer tipo de mudança na estrutura, é o que chamamos de `Computação de Propósito Genérico` e como no artigo referenciado acima, ENIAC foi a primeira máquina com essa capacidade.

### <i class="fa-solid fa-cash-register"></i> Máquina de Turing

Nesse ponto da História ficou bem claro que um computador de propósito genérico era necessário mas como definir um? Ah, é ai que Alan Turing e sua Máquina entram no circuito!

Turing foi capaz de definir em termos muito simples o que a máquina genérica seria e como opera-la. Claro, sua definição é de uma máquina abstrata, não de uma máquina física.

Essa máquina é capaz de executar qualquer tipo de `algoritmo`, desde que sigam a regra do estado finito, discutido anteriormente.

#### <i class="fa-solid fa-satellite"></i> O que é a Máquina?

A `Máquina de Turing` é feita de algumas, digamos, partes: a `Cabeça`, a `Fita` e o `Alfabeto`.

#### <i class="fa-solid fa-braille"></i> O Alfabeto

Para que a máquina funcione, um `Alfabeto` precisa ser definido, assim a máquina pode executar suas ações a partir do significado desses símbolos.

Isso é análogo ao que chamados de [`instruções de máquina`](https://pclt.sites.yale.edu/cpu-instructions) hoje.

#### <i class="fa-solid fa-tape"></i> A Fita

`A Fita` da máquina é análogo a `memória` que temos nos computadores de hoje.

Nessa máquina abstrata, essa `fita infinita` é dividida em células, todas do mesmo tamanho. Cada célula contem um símbolo do  `Alfabeto` ou então fica vazia.

#### <i class="fa-solid fa-thumbtack"></i> A Cabeça

`A Cabeça` da máquina é capaz de se mover entre qualquer uma das células da `Fita`, em qualquer direção mas apenas uma de cada vez.

Uma vez que a `cabeça` entra numa célula, ela escaneia o conteúdo e a partir da definição do `Alfabeto`, se move para outra célula ou escreve um novo símbolo na célula atual.

isso é análogo ao modo como as [CPUs modernas trabalham](https://en.wikipedia.org/wiki/Instruction_cycle).

## <i class="fa-regular fa-star"></i> Mas Por Que Devo me Importar?

Como mencionado várias vezes no artigo, praticamente todos os computadores desde a invenção da `Máquina de Turing` usam esse modelo.

Entender esse modelo pode ajudar a interagir melhor com a tecnologia também, uma vez que é possível se "comunicar" melhor com essas máquinas.

Não importa se a máquina é um IBM PC Original de 1980 ou o ficcional (por enquanto) iPhone 99x Pro: ambos possuem uma CPU modelada a a partir da `Máquina de Turing`.

E sim, mesmo aqueles "[joguinhos](https://www.pinterest.com/pin/102105116538007472/)" são `Máquinas de Turing` de uma forma.

Vamos listar alguns objetos que também são `Máquinas de Turing`:

- Smart TVs
- Tablets
- Veículos
- Qualquer aparelho "_smart_"

A lista continua indefinidamente...

### <i class="fa-solid fa-terminal"></i> Isso é Realmente Importante Para um Programador?

Numa palavra? Sim. Em outra palavra? **Absolutamente**. Toda a existência de um programador é criar `Algoritmos` para as `Máquinas de Turing` processarem.

> Na minha opinião, nada é mais importante no mundo de hoje do que um `algoritmo` bem definido e bem documentado, independente da sua aplicação.

Mesmo utilizando linguagens de programação como `Python`, `Javascript`, `Java`, `C#`, `Rust` ou `C/C++` esse código eventualmente vai se tornar `assembly`, diretamente via compilação como é o caso de `Rust` e `C/C++` ou via interpretação no caso dos outros exemplos.

Toda arquitetura de computadores tem seu próprio `alfabeto assembly` e aqui estão algumas arquiteturas que eu consigo lembrar no momento:

- [x86/x64](https://en.wikipedia.org/wiki/X86-64) - Praticamente todo computador Windows, desde sempre. Certo, existe a questão das eras de  `16`, `32` e `64-bit` mas isso é um tópico para outra discussão.
- [ARM](https://en.wikipedia.org/wiki/ARM_architecture_family) - Praticamente todo aparelho que existe como TVs, celulares, etc.
- [MIPS](https://en.wikipedia.org/wiki/MIPS_architecture) - Ah os bons e velhos N64 e PlayStation...
- [RISC V](https://en.wikipedia.org/wiki/RISC-V) - Nova no mercado, comparável com ARM mas é uma arquitetura a parte.
- [POWER](https://en.wikipedia.org/wiki/IBM_POWER_architecture) - Arquitetura IBM. Usada principalmente em mainframes e aplicações industriais.
- [6502](https://en.wikipedia.org/wiki/MOS_Technology_6502) - Usada no Nintendo Entertainment System, Apple II e muitos outros.

___