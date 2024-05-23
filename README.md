# Desafios de Código SQUADIO - Intermediário
Os desafios SQUADIO contribuem com a prática e a aplicação dos conceitos apresentados nas aulas e exercícios.

## O Robô Inteligente
Você foi contratado pela empresa DIO Robots para programar um robô capaz de classificar números em uma das seguintes categorias: negativo, positivo ou zero. Para isso, você deve criar uma função de classificação que receba um número como parâmetro e retorne a mensagem "negativo!" ou " positivo!", de acordo com sua categoria.

O programa deve ser executado continuamente, permitindo que o usuário insira vários números. Quando ele quiser encerrar a execução, deverá digitar um número igual a zero. A cada novo número inserido, o robô deve classificá-lo e exibir a mensagem correspondente. Ao final da execução, o programa deverá exibir a quantidade de números positivos, negativos e zeros que foram inseridos. To do:
- Crie a Função para classificar um número como positivo, negativo ou zero;
- Faça a verificação para saber quantos números positivos e negativos foram inseridos.

## A Jornada da Classificação Frutífera
Nesta missão, sua tarefa é mais desafiadora do que nunca! Em um pomar mágico, as frutas têm características únicas que as diferenciam. Seu objetivo é criar um modelo de machine learning capaz de classificar frutas com base em três características: peso, textura (suave ou áspera) e cor (vermelha, laranja ou amarela). Cada tipo de fruta tem limites específicos para essas características.

**Morango:**
- Peso mínimo: 150 gramas;
- Textura: Suave;
- Cor: Vermelha.

**Laranja:**
- Peso mínimo: 120 gramas;
- Textura: Suave;
- Cor: Laranja.

**Banana:**
- Peso mínimo: 150 gramas;
- Textura: Áspera;
- Cor: Amarela.

**Maçã:**
- Peso mínimo: 130 gramas;
- Textura: Ápera;
- Cor: Vermelha.

### Importante:
É necessário que a ordem das condições elif seja respeitada conforme a descrição do desafio. Lembrando que, no Python, a indentação é fundamental para a definição de blocos de código, como os que pertencem a loops e funções. Se a indentação estiver incorreta, o Python não conseguirá interpretar corretamente o bloco de código, resultando em erros ou comportamento inesperado.

To do:
- Desenvolva a função para prever a classe da fruta.

# A Questão Intrincada da Magia Preditiva
No reino mágico onde cada feiticeiro possui uma afinidade elemental única, seu desafio é criar um modelo de machine learning para prever essa afinidade. Os feiticeiros podem pertencer a um dos quatro elementos mágicos: Fogo, Água, Terra ou Ar. A predição será baseada em cinco atributos mágicos: intensidade do feitiço, presença de componente raro, fase lunar, idade do feiticeiro e afinidade com animais mágicos.

Aqui estão os critérios mágicos para cada elemento:

**Elemento Fogo:**
- Intensidade do feitiço maior ou igual a 5;
- Fase lunar durante o feitiço é crescente;
- Idade do feiticeiro é superior a 100 anos.

**Elemento Água:**
- Intensidade do feitiço maior ou igual a 7;
- Presença de componente raro;
- Fase lunar durante o feitiço é cheia;
- Idade do feiticeiro é igual ou inferior a 100 anos;
- Afinidade com animais mágicos.

**Elemento Terra:**
- Intensidade do feitiço maior ou igual a 7;
- Presença de componente raro;
- Fase lunar durante o feitiço é cheia;
- Idade do feiticeiro é igual ou inferior a 100 anos;
- Afinidade com animais mágicos.

**Elemento Ar:**
- Caso não se encaixe nos critérios anteriores.
