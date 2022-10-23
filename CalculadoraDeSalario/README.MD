# Especificação

Deve-se implementar uma calculadora de salário de funcionários. Um funcionário contém nome, e-mail, salário-base e cargo. De acordo com seu cargo, a regra para cálculo do salário líquido é diferente:

- Caso o cargo seja DESENVOLVEDOR, o funcionário terá desconto de 20% caso o salário seja maior ou igual que 3.000,00, ou apenas 10% caso o salário seja menor que isso.
  - No sistema, DESENVOLVEDOR foi chamado de `Developer`
- Caso o cargo seja DBA, o funcionário terá desconto de 25% caso o salário seja maior ou igual que 2.000,00, ou apenas 15% caso o salário seja menor que isso.
  - No sistema, DBA foi chamado de `DBA`
- Caso o cargo seja TESTADOR, o funcionário terá desconto de 25% caso o salário seja maior ou igual que 2.000,00, ou apenas 15% caso o salário seja menor que isso.
  - No sistema, TESTADOR foi chamado de `Tester`
- Caso o cargo seja GERENTE, o funcionário terá desconto de 30% caso o salário seja maior ou igual que 5.000,00, ou apenas 20% caso o salário seja menor que isso.
  - No sistema, GERENTE foi chamado de `Manager`

# Avaliação do uso do TDD

Implementação por: [Túlio](https://github.com/tulioac)

O que foi bom? O que foi ruim? O que foi difícil? 

O uso do TDD se mostrou bastante vantajoso para entregar confiança no código escrito, uma vez que para implementar uma funcionalidade, teve-se que se criar um teste que motivasse sua implementação e por esse motivo, a implementação era extremamente direcionada ao teste e não se codificou nada a mais do que o necessário para o teste. Com isso, obtive um sentimento que coesão do que estava sendo feito. 

Além disso, o processo de criar uma implementação simplória para cada teste, possibilita que a pessoa desenvolvedora tenha um tempo para amadurecer uma implementação de maior qualidade e perceber também pontos que poderiam quebrar o sistema, dando espaço para criação de mais testes que vão garantir que o código não caia em situações problemáticas. 

Contudo, a codificação utilizando o TDD se mostrou demorada quando comparada a uma abordagem sem ela. Talvez esse fator se dê pela falta de experiência do desenvolvedor de codificar utilizando essa abordagem ou que ela realmente consuma mais tempo que o padrão mesmo.

No geral, a maior dificuldade foi se conter para não escrever o código mais complexo nos primeiros passos, realmente definir pequenos blocos que não façam mais nada do que o teste espera como resultado. Porém quando esses testes mais básicos são definidos e casos mais complexos são cobertos, tem-se uma sensação de completude e satisfação sobre o código que está sendo feito.
