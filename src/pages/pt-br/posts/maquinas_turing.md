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
    - [Isso é Realmente Importante para um Programador?](#isso-é-realmente-importante-para-um-programador)
- [Como que essas Arquiteturas Implementam o Modelo da Máquina de Turing?](#como-que-essas-arquiteturas-implementam-o-modelo-da-máquina-de-turing)
    - [É Tudo Preto ou Branco](#é-tudo-preto-ou-branco)
    - [Quantos Bits você Aguenta?](#quantos-bits-você-aguenta)
        - [Qual é a Palavra?](#qual-é-a-palavra)
    - [O Alfabeto do 6502](#o-alfabeto-do-6502)
        - [Por Favor, me Instrua](#por-favor-me-instrua)
        - [Hora de Exemplificar](#hora-de-exemplificar)
        - [Ao Vencedor, os Espólios](#ao-vencedor-os-espólios)
- [Execução Terminada](#execução-terminada)

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

### <i class="fa-solid fa-terminal"></i> Isso é Realmente Importante para um Programador?

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

## <i class="fa-solid fa-robot"></i> Como que essas Arquiteturas Implementam o Modelo da Máquina de Turing?

Antes de mais nada, vamos deixar algo claro: CPUs são coisas extremamente complexas. é MUITO difícil explica-las porque você começa a entrar no território do `bit` e olha, começa a ficar complicado bem rápido!

Como mencionei anteriormente, eu não sou um cientista da computação. Eu sou só meio louco que ama programar e meu conhecimento se dá pela minha curiosidade e quantidade de leituras que fiz sobre o assunto.

Tudo isso é pra dizer que vou tentar fazer a melhor explicação do assunto como se você tivesse 5 anos. Ano que vem você terá 6 e com certeza será ainda mais fácil de entender.

Eu vou usar a arquitetura [MOS 6502](https://en.wikipedia.org/wiki/MOS_Technology_6502) como exemplo porque é (relativamente) simples e direta.

### <i class="fa-solid fa-palette"></i> É Tudo Preto ou Branco

Não exatamente `preto` ou `branco`, está mais para `uns` e `zeros`.

Usando esse exemplo novamente, não importa se você tem um IBM PC Original de 1980 ou o ficcional (por enquanto) iPhone 99x Pro, ambos são `máquinas binárias`, o que significa que só entendem valores que são `1` ou `0`.

### <i class="fa-solid fa-drumstick-bite"></i> Quantos Bits você Aguenta?

(Essa piada se perdeu na tradução... `bits` em inglês podem significar `partes`)

O `6502` implementa a `Máquina de Turing` com as seguintes características:

- O `Alfabeto` é composto de `palavras` de `8-bit`;
- A `Fita` pode ter até `65,535` células (nesse caso, `bits`);
- A `Cabeça` tem células exclusivas chamadas de `registradores` para guardar algumas informações de execução como `índice da célula na Fita`, por exemplo;

#### <i class="fa-solid fa-dove"></i> Qual é a Palavra?

(Outra piada que se perdeu na tradução... [the bird is the word](https://youtu.be/9Gc4QTqslN4))

É um pouco estranho comparar `Alfabeto` com `Palavras` mas eu posso explicar:

- O `bit` é uma `letra` muito limitada, digamos, porque seu valor só pode ser `1` ou `0`;
- Como uma CPU pode realizar inúmeras operações, o `símbolo` no `Alfabeto` precisa ser único.

Esse conjunto de características faz com que a natureza binária do `bit` seja muito difícil de usar na criação de um `Alfabeto` de múltiplos `símbolos`.
A única resposta então é: vamos fazer o `símbolo` ser uma combinação de `8-bits` e vamos chamar essa combinação de `palavra`.

### <i class="fa-solid fa-microchip"></i> O Alfabeto do 6502

Para fins deste exemplo, eu não vou explicar o `alfabeto` completo do 6502, também conhecido como `set de instruções`, por ser muito técnico e complexo.

O que farei, então, é explicar algumas `palavras`, ou `instruções`, específicas apenas para ilustrar como o computador as processaria.

#### <i class="fa-solid fa-chalkboard-user"></i> Por Favor, me Instrua

> Para o pedante: eu sei que o 6502 tem modos de endereçamento e outros detalhes mas eles não são relevantes aqui. Por sinal, eu escrevi um [emulador do 6502](https://github.com/zeh-almeida/6502-sharp) que entra nesses detalhes, se tiver interesse.

Tentarei explicar algumas `instruções` que serão apresentadas num exemplo posterior:

##### Clear Carry Flag ([CLC](https://masswerk.at/6502/6502_instruction_set.html#CLC))

Instrui a `Cabeça` a marcar o `registrador carry` com `zero`.

##### Load Accumulator ([LDA](https://masswerk.at/6502/6502_instruction_set.html#LDA))

Instrui a `Cabeça` a definir o valor do `registrador acumulador` com o valor que definirmos.

##### Add With Carry ([ADC](https://masswerk.at/6502/6502_instruction_set.html#ADC))

Lê uma `célula` da `Fita` e incrementa o `registrador acumulador` na `Cabeça`.

Se o resultado do incremento for maior que `255`, o maior valor possível para um número de `8-bit`, ele recomeça do `0` e marca o `registrador carry` da `Cabeça` com `1`.

Isso significa que é possível adicionar números além do valor de `255` porque você sempre saberá que o valor "resetou" ou não.

##### Branch Carry Clear ([BCC](https://masswerk.at/6502/6502_instruction_set.html#BCC))

Instrui a `Cabeça` a pular para uma `célula` específica se o `registrador carry` for `zero`.

#### <i class="fa-solid fa-flask-vial"></i> Hora de Exemplificar

Vamos criar um `algoritmo` muito simples com o único propósito de contar até `255` e finalizar assim que atingir esse valor.

Como `Máquinas de Turing` operam um `símbolo` de cada vez, nós precisamos dar mais detalhes ao `algoritmo`:

```
Começando do zero, incremente o valor em uma unidade até chegar em 255, então finalize.
```
Agora sim estamos chegando lá mas ainda não é algo que o `6502` possa processar. Ainda bem que já sabemos quais `instruções"` nós precisamos para escrever esse `algoritmo`:

<div class="code-block">
```
CLC     ; Garante que o registrador carry tenha valor igual a zero

LDA #0  ; Garante que o registrador acumulador tenha valor igual a zero

ADC #1  ; Adiciona 1 no valor do registrador acumulador

BCC FC  ; Pula para a célula anterior quando o registrador carry tiver valor igual a zero.
        ; Senão, finaliza o programa.
```
</div>

Aposto que você está vendo esse valor `FC` e se perguntando: Que?

Realmente, parece que esse valor veio do nada. Esse número é o resultado de `255` menos `3 bytes`, o que faz com que ele caia na `célula` da `instrução` `ADC` só que expressado na [notação hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal).

#### <i class="fa-solid fa-flag-checkered"></i> Ao Vencedor, os Espólios

Parabéns, você acaba de entender (talvez) um `código assembly` básico de `6502`!

Não só isso, você também programou seu primeiro `algoritmo`, aí sim!

Eu espero que esse exemplo seja suficiente para explicar como o modelo da `Máquina de Turing` é implementado em CPUs comuns. E claro, se isso não foi suficiente, por valor me mande um e-mail, gostaria muito de saber suas opiniões a respeito.

## <i class="fa-solid fa-trophy"></i> Execução Terminada

Com isso chegamos a épica conclusão do meu conto sobre `Máquinas de Turing`, o design que revolucionou o mundo.

Eu sinceramente espero que os exemplos tenham sido claros e espero que você tenha entendido essa coisa de `assembly` com certa facilidade.

Caso tenha perguntas ou comentários, estou 100% disposto a recebe-los via e-mail, no topo da página.

Espero que você venha novamente para ler outros artigos no futuro.


___