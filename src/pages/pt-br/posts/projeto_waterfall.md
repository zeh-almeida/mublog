---
title: Ciclo de Vida de Projetos - A Cascata (Waterfall)
description: o que é o Modelo Cascata, também conhecido como "Gestão Básica de Projeto"
date: 2023-08-17
modified: 2023-08-17
tags: projeto,gestão,ágil,cascata,waterfall,requerimento,regra de negócio,análise,problema,iteração,navegação,trabalho,resultado,entrega
---
# <i class="fa-solid fa-water"></i> Ciclo de Vida de Projetos - A Cascata (Waterfall)

## <i class="fa-solid fa-triangle-exclamation"></i> Atenção

> A maior parte das coisas que escrevi está em formato livre e toda a tradução foi feita diretamente por mim. Claro, eu fiz minha pesquisa e deixei os links com as fontes no texto mas não leve o conteúdo tão a sério: eu não sou um cientista da computação muito menos um pesquisador.
**Em caso de dúvida, consulte as fontes**. Obrigado e que o show continue!

## <i class="fa-solid fa-list-ul"></i> Índice

- [Antes de Mais Nada: O que é um Ciclo de Vida de Projeto?](#antes-de-mais-nada-o-que-é-um-ciclo-de-vida-de-projeto)
- [Navegando Pela Cascata](#navegando-pela-cascata)
- [Com Seu Barco na Água](#com-seu-barco-na-água)
    - [A Água Deve Ser Funda o Suficiente](#a-água-deve-ser-funda-o-suficiente)
- [All the Fools Sailed Away (E Os Tolos Navegaram)](#all-the-fools-sailed-away-e-os-tolos-navegaram)
    - [O Dedo Verde](#o-dedo-verde)
- [Navegando As Cartas Marítimas](#navegando-as-cartas-marítimas)
    - [Território Desconhecido](#território-desconhecido)
- [Que Ronquem Os Motores](#que-ronquem-os-motores)
    - [De Olho Naquelas Nuvens](#de-olho-naquelas-nuvens)
- [Cuidado Com o Motor e Combustível](#cuidado-com-o-motor-e-combustível)
    - [Ora, Aqui Está Seu Problema](#ora-aqui-está-seu-problema)
- [Você Chegou! A Alfândega Fica à Esquerda](#você-chegou-a-alfândega-fica-à-esquerda)
    - [Esse item Não Foi Declarado](#esse-item-não-foi-declarado)
- [Então Pra Que Serve a Cascata?](#então-pra-que-serve-a-cascata)
    - [Onde a Cascata é um Sucesso](#onde-a-cascata-é-um-sucesso)
    - [Onde a Cascata Falha](#onde-a-cascata-falha)
    - [Continue a Girar](#continue-a-girar)
- [Finalmente, Vamos Descansar](#finalmente-vamos-descansar)

___
## [>](#index) <i class="fa-solid fa-chart-line"></i> Antes de Mais Nada: O que é um Ciclo de Vida de Projeto?

Digamos que você tenha um problema. Não deve ser algo muito difícil de imaginar, né?

Claro, você é uma pessoa inteligente, então você vai tomar os cuidados necessários para que, digamos, seu problema desapareça.
Vamos chamar esses cuidados necessários de `projeto`, para deixar o exemplo mais claro.

Agora que você tem seu próprio projeto, você tem tudo o que precisa para resolver seu problema? Na verdade, não.
Primeiro você precisa entender esse problema, ter certeza que você está tratando a doença e não os sintomas.

Bom, se você soubesse fazer isso, você não teria um problema, não é verdade? É isso que significa ter o `ciclo de vida de um projeto`.

É uma `coleção de passos, fases e operações que se executa para garantir que seu projeto termine com sucesso`.

## [>](#index) <i class="fa-solid fa-clipboard-question"></i> Navegando Pela Cascata

O `Ciclo de Vida de Cascata` é um dos mais antigos e provavelmente o primeiro ciclo de vida para projetos de software, [de acordo com a Wikipedia](https://en.wikipedia.org/wiki/Waterfall_model).

Esse ciclo se chama `Cascata` porquê ele começa no topo e vai até o final, sem chance de retorno.

Obviamente que antes de mudar de uma fase para a próxima tudo deve ser validado e aceito pelo time.

## [>](#index) <i class="fa-solid fa-sailboat"></i> Com Seu Barco na Água

> para chegarmos até a `Cascata`, primeiro precisamos de um barco.

Tudo começa com a `declaração do problema`:
 - O que precisa ser feito
 - Porque precisa ser feito dessa forma

Normalmente chamamos isso de `requisitos` e, na minha opinião pessoal `são as coisas mais comuns de estarem erradas num projeto`.

`Requisitos` são as coisas que o projeto **PRECISA** alcançar, sem mais nem menos: ou o projeto entrega os `requisitos` ou ele falha. Por isso é imperativo que os `requisitos` estejam claros. Senão é como pedir para um software [resolver o problema da parada](https://pt.wikipedia.org/wiki/Problema_da_parada).

Não existe limites para o número de `requisitos`. Claro que quanto maior a lista, mais difícil será a manutenção e o desenvolvimento do projeto.

> Por mais que seja uma opinião pessoal, eu acredito que o sucesso de um projeto está na seleção criteriosa de `requisitos` seletos, separados em fases de projeto distintas.

### <i class="fa-solid fa-water-ladder"></i> A Água Deve Ser Funda o Suficiente

A `fase de elicitação de requisitos` **deve** resultar num único porém extremamente detalhado artefato: O [`Documento de Requisitos`](https://en.wikipedia.org/wiki/Product_requisitos_document).

Esse documento deve ser extremamente claro e específico ao detalhar `o que o problema requer`, não `como o problema deve ser resolvido`. Essa questão será respondida em fases futuras.

Digamos que você tem o simples `requisito` de construir uma parede. Essa `declaração` pode ser simples assim:

 ```
 Para que a construção dos cômodos seja suficientemente clara, os cômodos devem ser separados por paredes.
 ```

Nessa `declaração` não temos nada como dimensão das paredes, quais materiais devemos usar, etc. A `declaração` é muito simples: ela `diz num texto simples e claro qual o problema e o que esperar como resultado`.

## [>](#index) <i class="fa-solid fa-wind"></i> [All the Fools Sailed Away (E Os Tolos Navegaram)](https://open.spotify.com/track/0SYF0IKXsDZI0XR7TM2Kxr?si=f571b8fc704a4fe0 "Ronnie James Dio, The Man on the Silver Mountain")

> Agora que seu barco está na água, para onde você vai?

Com sua `declaração de problema`agora você tem os seus `o ques` e `por ques` agora precisamos descobrir os `comos`.

Essa parte do ciclo de vida é chamada de `Análise` e é extremamente direta.
Você precisa ter certeza que:

 - Todos os `requisitos` são claros
 - Todos os `requisitos` são alcançáveis
 - Os `requisitos` não se cancelam
 - Os `requisitos` podem ser testados de uma forma clara e direta

Nessa parte da viagem pode ser impossível continuar navegando simplesmente porque uma dessas declarações não pôde ser atendida de forma satisfatória. O Modelo `Cascata` entende que os resultados de fases anteriores são verdades absolutas para continuar nas fases seguites.

Isso significa que se algum dos seus`requisitos` não estiver nos padrões esperados na fase de `análise` o projeto _deve_ ser terminado, pelo menos na teoria.

> **Realmente** deveria parar por aqui. Seu projeto não tem nenhuma chance de sucesso se os pontos da fase de `análise` não estiverem alinhados.

Uma vez que cada um dos`requisitos` for completamente analisado, eles devem ser documentados para garantir que a implementação dos mesmos esteja de acordo com o esperado.

Não importa quantos `requisitos` estiverem corretos: se um único item não for analisado e/ou documentado como esperado, por favor pare o projeto - ele vai falhar.

### <i class="fa-solid fa-thumbs-up"></i> O Dedo Verde

O resultado de passar por todos os `requisitos` e garantir que eles estão válidos é uma forma mais técnica de chegarmos nos `comos` da `declaração de problema`.

Uma ou mais `regras de negócio` podem existir para um único `requisito`. Essas regras respondem o `como` de cada `requisito`, que pode vir em vários passos.

Voltando para nosso
Going back to the [exemplo de parede](#a-água-deve-ser-funda-o-suficiente), nós podemos derivar algumas `regras`:

```
- Paredes não podem deixar nenhum espaço entre elas a não ser pelas portas e janelas;
- A posição das portas e janelas deve ser definida antes da construção das paredes;
- Paredes devem permitir a passagem de cabos elétricos e canos de água e aquecimento de forma que fiquem escondidos;
- Paredes devem seguir as regras de construção e normas associadas previamente estabelecidas;
```

Ótimo, isso deixa muito mais claro `como` o `requisito` será atingido, mesmo que meu exemplo não seja real e sirva apenas para ilustrar a situação.

Agora que temos a `lista dos requisitos que devemos atender` e `como cada requisito deve ser implementado` nós podemos seguir com a viagem.

## [>](#index) <i class="fa-regular fa-compass"></i> Navegando As Cartas Marítimas

> Agora sim: temos nosso barco na água com o destino traçado, perfeito! Como chegamos lá?

Depois dos `requisitos` se tornarem `regras de negócio` nós temos nossos  `o ques`, `por ques` e `comos`, então o que falta?

Em termos mais simples, nos precisamos saber de que forma nossas `regras de negócio` vão interagir entre elas. Nós já deixamos claro que essas `regras` estão conectadas mas não se cruzam então precisamos dar um jeito para que elas vivam juntas.

É nessa hora que a `fase do design` brilha. Pode até parecer que essa fase chegou atrasada mas não é bem assim. Para que o `design` cumpra seus objetivos, esses **PRECISAM** estar inequivocamente claros e nós acabamos de chegar nesse estágio com nossas `regras de negócio`.

Mantendo o `tema de engenharia civil` nos exemplos, essa fase seria análoga ao `design da arquitetura`: Você sabe as limitações das `paredes` e `cômodos` então você precisa `desenhar` o `projeto` de uma forma que você otimize o uso de acordo com as `regras de negócio`.

### <i class="fa-solid fa-compass-drafting"></i> Território Desconhecido

> É possível que o mapa não possua uma rota para o destino que você deseja.

Ao se organizar as muitas `regras de negócio` e suas conexões, pode se tornar impossível acomodar todas.

Imagine que você precisa de uma quantidade arbitrária de cômodos no seu primeiro andar e suas `regras de negócio` determinaram um tamanho mínimo para cada cômodo.

O que aconteceria se não houvesse mais espaço físico para caber todos os cômodos de acordo com as `regras`? Bom, isso significa que `o projeto já era`.

De forma mais direta, esse tipo de problema _poderia_ e, na verdade, **deveria** ter sido pego durante a fase de `análise` mas as vezes a complexidade e detalhes minuciosos dos `requisitos` leva um pouco mais de tempo para nor morderem.

## [>](#index) <i class="fa-solid fa-gauge-high"></i> Que Ronquem Os Motores

> Nós sabemos como chegar e para onde ir, então vamos!

Nós **finalmente** chegamos na parte onde "as coisas acontecem". Não que os outros passos não tenham "feito" nada: eles são **extremamente** necessários mas não entregaram nada que resolva o `problema` em primeiro lugar. Tudo o que fizeram foi `preparar o terreno`, por assim dizer, para a `real solução do problema`.

Vamos listar tudo o que temos até agora:

- `Requisitos`: o que precisa ser feito
- `Regras de Negócio`: como deve ser feito
- `Desenho da Solução`: como deve ser organizado

As coisas parecem boas pois temos um bom entendimento da situação que queremos atuar. O que falta agora é realmente atuar, por isso essa fase se chama de `Construção` ou em projetos de software, `o Código`.

Nessa fase as coisas começam a tomar forma: você `limpa o terreno`, `faz a terraplanagem`, `junta os tijolos, areia e concreto` no terreno, tudo muito legal.

As `Regras de Negócio` são executadas pelo time `como desenhado` e `seguindo as regras`, dessa forma a gente consegue entregar dentro do prazo, né?

**Não é?**

### <i class="fa-solid fa-cloud-showers-water"></i> De Olho Naquelas Nuvens

> Não importa quão bem detalhada e planejada foi sua viagem: a Natureza pode ser traiçoeira.

A `fase de construção` é quando os `requisitos` e as `regras de negócio` tomam forma na "realidade". Até esse ponto elas eram ideais, coisas com importância mas ainda assim, etéreas.

Uma vez que chegam nessa fase, porém, a `materialização de etéreo para real pode não ser perfeita`.

Claro que seu `desenho` foi extremamente claro e preciso nas medidas mas `alguém pediu os tijolos errados` e agora `as coisas não se alinham mais`.

O que disse? Ah, a `torneira deveria estar na outra parede`? Não dá pra só `inverter` o cômodo?

Coisas como essa são mais comuns do que gostaríamos, e acredito que todos já passaram por algo parecido antes. Imprevisibilidade é o desafio da vida, quem sabe.

Assim como antes, porém, `coisas como essas são inaceitáveis na Cascata` e significam que o projeto falha imediatamente.

## [>](#index) <i class="fa-solid fa-temperature-quarter"></i> Cuidado Com o Motor e Combustível

> A viagem segue tranquila, como planejado. Fique de olho para que o motor não esquente ou fique sem combustível, estamos quase no nosso destino!

Você consegue acreditar que `as coisas já foram feitas`? Tanto trabalho já realizado até agora e ainda temos mais o que fazer: chegamos na `fase de validação` da nossa viagem.

Se você fez um planejamento muito muito **MUITO** cuidadoso que foi seguido a risca e a `fase de construção` seguiu sem problemas, está na hora de garantir que as coisas foram feitas à risca. Como a `Cascata` não é sobre `feedbacks`, esse passo _deveria_ ser apenas uma formalidade, simplesmente uma forma de demonstrar que as coisas estão como deveriam ser.

Mas a vida é uma caixinha de surpresas e a [lei de Murphy](https://en.wikipedia.org/wiki/Murphy%27s_law) costuma aparecer quando menos esperamos.

### <i class="fa-solid fa-temperature-high"></i> Ora, Aqui Está Seu Problema

Como estamos lidando com a `Cascata`, problemas costumam a acumular até estourarem. A `fase de validação` é conhecida por se enroscar em `má interpretação de requisitos`, `regras de negócio incompatíveis` ou simplesmente `uma construção ruim`.

Mas nós não revimos todas as coisas antes de avançar os passos? Obviamente que esses problemas foram identificados e corrigidos antes, não? Bom, eles deveriam mas isso nem sempre acontece.

No caso da `construção civil`, algumas pessoas tem tanto conhecimento e experiência nos processos que isso se torna natural e elas não tem desvios. Em coisas como software por exemplo, onde cada solução é diferente pois cada problema é diferente, é muito comum encontrar esses defeitos.

Eu devo ser bem claro: isso não significa que o time é incompetente ou agiu de forma maliciosa. Construir coisas é **DIFÍCIL** e **complicado**, não importa se é um `programa de calculadora` ou um `sistema operacional multi-plataforma, direto na nuvem`.

Tenha certeza que seus defeitos estão bem documentados: isso **DEVE** incluir o que era esperado, o que foi identificado e por que isso está errado. Isso vai ajudar muito na `identificação da causa raíz` e vai melhorar o `tempo de resposta` do time na correção dos itens.

## [>](#index) <i class="fa-solid fa-building-shield"></i> Você Chegou! A Alfândega Fica à Esquerda

> Finalmente chegamos ao nosso destino! Ótimas férias, muito relaxante. Ah, não vamos esquecer de passar na Alfândega antes de voltar, trouxemos tantos souvenirs!

Finalmente nossa viagem está no fim, nós conquistamos a `Cascata`. Antes de voltarmos para casa, porém, precisamos passar na Alfândega.

É novamente como nosso exemplo de `construção civil`: uma vez que as inspeções são feitas e aprovadas, tudo o que falta é o cliente usar. Talvez seja a `casa dos sonhos` ou quem sabe até `uma grande escritório`, com certeza querem fazer uso do espaço o mais rápido possível.

Isso significa, claro, que precisamos fazer a `mudança`: `ajustar os móveis`, `subir os quadros e fotos`, `ligar os equipamentos`.... Ah, as alegrias de uma mudança!

Lembre-se que depois desse processo você está livre para usar como quiser pois **finalmente** terminamos!

### <i class="fa-solid fa-handcuffs"></i> Esse item Não Foi Declarado

Infelizmente para alguns nem tudo termina bem.

Talvez você tenha uma `standup desk` que é grande demais para entrar no cômodo e ela não pode ser desmontada, ou talvez sua nova cama não caiba no quarto porque você a comprou _depois_ das medidas dos cômodos.

Coisas assim acontecem e podem `matar o projeto`. Se você não consegue entregar o projeto, você pode dizer que ele terminou?

## [>](#index) <i class="fa-solid fa-clipboard-question"></i> Então Pra Que Serve a Cascata?

Eu fui bem incisivo durante todo o artigo que `qualquer pedra no caminho pode matar o projeto`. Isso só é _"verdade"_ na `teoria`: na `prática` as pessoas tendem a encontrar formas de trabalhar esses problemas para continuar com o andamento do projeto.

Porém mesmo que você consiga finalizar o projeto todos esses `pontos de atenção` que surgiram são coisas que **precisam** ser trabalhadas para `realmente resolvermos a declaração de problema`.

Então `pra que serve a Cascata`? Parece algo muito `burocrático` e `difícil de navegar` mas possui uma grande vantagem:

> O Modelo de Cascata é perfeito para projetos em que experiências anteriores podem ser incorporadas e reutilizadas.

### <i class="fa-regular fa-circle-check"></i> Onde a Cascata é um Sucesso

A `Cascata` parece obter sucesso em `projetos com elementos que se repetem`.
Significa que é ótima para projetos de `construção civil`, por exemplo:

 - Você provavelmente vai `sempre` subir uma parade de tijolos `da mesma forma`;
 - Você provavelmente vai `sempre` subir um painel de drywall `da mesma forma`;
 - Regras e leis de construção `levam anos para mudar` e a mudança é incremental;
 - Por mais que a tecnologia de cabos mude de rígidos para torcidos, `a forma como são passados não mudou muito`;

Obviamente que é possível ter `itens arquiteturais` que podem tornar a construção um pouco menos ordinária mas realisticamente `isso é a exceção`.

A `Cascata` é perfeita para esses cenários porque eles são `extremamente previsíveis` o que é perfeito pois a `Cascata tem aversão a mudanças`.

> Qualquer cenário onde as condições são estáticas ou o mais próximo possível disso poderão usar a `Cascata` com um alto grau de confiança para o sucesso.

### <i class="fa-regular fa-circle-xmark"></i> Onde a Cascata Falha

Existem muitas formas em que a `Cascata` vai te ajudar a chegar numa `vitória` mas também existem formas em que ela pode contribuir para uma `perda`:

> A `Cascata` odeia mudanças. Se você precisa de algum tipo de `feedback` durante a execução do `projeto` a `Cascata` **NÃO** é para você.

Antes de explicar o que eu quero dizer com `feedback`, eu prefiro apresentar alguns exemplos de onde ele é usado:

 - Projetos de Pesquisa
 - Soluções de Prototipagem
 - Interação do Time

Nessas situações você precisa `se adaptar a mudanças o mais rápido possível`. Quando se está pesquisando algo, se aplica o `método científico` onde você `testa suas hipóteses e ajusta suas teorias com os resultados`, você `recebe e abraça as mudanças em cada passo`.

> `Software é a mesma coisa`: ele **requer** um `feedback loop` para chegar nos melhores resultados. Não consigo pensar numa única instância onde `software` produzido com `o Modelo Cascata` teria sucesso.

A não ser que você tenha tempo e dinheiro infinitos, obviamente.

### <i class="fa-solid fa-arrow-rotate-left"></i> Continue a Girar

O que é esse tal de `feedback loop` que eu falo tanto?

Voltando ao exemplo de `experimentos científicos`, é quando você `itera soluções` até chegar num ``ponto de inflexão`, ou seja: `ou dá certo ou dá errado`.

Parece muito com o que a `Cascata` tenta resolver, uma vez que a ideia de `gerenciamento de projetos` é sempre obter êxito no final: a diferença é `em como a gerência do projeto é feita`.

Nos `feedback loops` você trabalha com `pequenas mudanças incrementais` fazendo com que você  `entenda o que funciona, o que não funciona e o porque`, permitindo que você e seu time `trabalhem de forma mais eficiente` e `evitem problemas conhecidos`.

> Assim como a `Cascata` porém, eles podem não servir para qualquer projeto: são apenas ferramentas de trabalho. É sua responsabilidade escolher as melhores ferramentas para cada trabalho.

Se estivermos falando de `software`, o `feedback loop` é melhor representado pelo `Framework Ágil` mas isso é assunto para artigos futuros, OK?

## <i class="fa-solid fa-umbrella-beach"></i> Finalmente, Vamos Descansar

Agora sim, a viagem terminou, sem mais surpresas. Espero que nessa altura do campeonato você tenha um melhor entendimento do que é a `Cascata` e aonde, como e quando usa-la.

Se você já sabia isso, espero que tenha sido bom refrescar a memória.

Como sempre: em caso de dúvidas ou comentários, mande um e-mail ou uma mensagem no Telegram, os links estão no topo da página.

Até logo.

___