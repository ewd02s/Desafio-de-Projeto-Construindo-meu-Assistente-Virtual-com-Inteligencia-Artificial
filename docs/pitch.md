# FinanIA — Assistente de Planejamento de Economia

## 1. O problema

Muitas pessoas querem alcançar objetivos financeiros, mas não sabem exatamente quanto precisam economizar por mês para chegar até uma determinada meta.

Por exemplo:

> "Quero juntar R$ 3.000, mas não sei quanto preciso guardar por mês."

Uma informação aparentemente simples pode gerar dúvidas, principalmente para quem está começando a organizar a própria vida financeira.

---

## 2. A solução

Para resolver esse problema, desenvolvi o **FinanIA**, um assistente de planejamento de economia baseado em Inteligência Artificial.

O objetivo é simples:

**ajudar uma pessoa a transformar uma meta financeira em um plano mensal de economia.**

O usuário informa:

* quanto deseja juntar;
* em quanto tempo pretende alcançar a meta.

O sistema calcula uma simulação do valor que precisaria economizar mensalmente e explica o resultado de forma simples.

### Exemplo

Usuário:

> "Quero juntar R$ 3.000 em 6 meses."

FinanIA:

> "Para juntar R$ 3.000 em 6 meses, você precisaria economizar aproximadamente R$ 500 por mês. Essa é uma simulação simples, sem considerar juros, rendimentos ou taxas."

---

## 3. Como funciona

O projeto foi desenvolvido separando responsabilidades.

### Inteligência Artificial

A IA é responsável por:

* entender a intenção do usuário;
* identificar informações importantes;
* conversar de maneira natural;
* explicar o resultado;
* solicitar informações que estejam faltando;
* utilizar a base de conhecimento.

### Python

O Python é responsável pelos cálculos determinísticos.

Por exemplo:

**Meta ÷ quantidade de meses = economia mensal**

Assim, a IA não precisa "chutar" um resultado matemático.

---

## 4. Base de conhecimento

O FinanIA possui uma base de conhecimento estruturada em JSON.

Ela contém:

* conceitos financeiros básicos;
* perguntas frequentes;
* regras de comportamento;
* exemplos de utilização.

A base também estabelece limites para o assistente.

O FinanIA não deve inventar:

* taxas de juros;
* rendimentos;
* condições de investimentos;
* informações bancárias;
* dados que não estejam disponíveis.

Quando não possui informação suficiente, o assistente deve deixar isso claro.

---

## 5. Segurança e responsabilidade

O projeto também considera situações em que o usuário fornece informações sensíveis.

O FinanIA não deve solicitar:

* senha;
* número de cartão;
* código de segurança;
* credenciais bancárias;
* outros dados confidenciais.

Além disso, as simulações são apresentadas como **simulações**, e não como garantias de resultado financeiro.

---

## 6. Experiência do usuário

A aplicação foi pensada para ser simples.

O usuário não precisa conhecer termos técnicos ou fórmulas financeiras.

A experiência funciona como uma conversa:

**Usuário → FinanIA → entendimento da necessidade → cálculo → explicação → próximo passo**

Se faltar uma informação, o assistente pergunta.

Por exemplo:

> "Quero juntar R$ 4.000."

O FinanIA não inventa um prazo.

Ele pergunta:

> "Em quantos meses você pretende alcançar essa meta?"

---

## 7. Avaliação

Para verificar se o sistema realmente funciona, foram definidos casos de teste.

Os testes avaliam:

* entendimento da intenção;
* precisão dos cálculos;
* utilização da base de conhecimento;
* identificação de informações ausentes;
* controle de respostas inventadas;
* segurança;
* clareza;
* manutenção do contexto da conversa.

Um dos testes verifica, por exemplo:

> "Quero juntar R$ 4.000."

O comportamento esperado é solicitar o prazo.

Outro teste verifica se o sistema mantém o contexto:

> "Quero juntar R$ 4.000."

Depois:

> "Em 8 meses."

O sistema deve utilizar as duas informações para chegar à simulação de:

**R$ 500 por mês.**

---

## 8. Tecnologias

O MVP utiliza:

* Python;
* Streamlit;
* JSON;
* Inteligência Artificial generativa;
* Git;
* GitHub.

A arquitetura foi pensada para permitir evolução futura.

---

## 9. Evolução

O projeto começa pequeno, mas pode evoluir.

Uma possível evolução seria:

### MVP

Python + Streamlit + JSON + regras básicas.

↓

### Versão com IA

LLM + prompt especializado + base de conhecimento.

↓

### Versão avançada

* memória contextual;
* recuperação inteligente de informações;
* banco de dados;
* histórico de metas;
* autenticação;
* dashboards;
* análise de evolução;
* integração com APIs financeiras.

A ideia é evoluir o sistema de maneira gradual, validando cada etapa antes de adicionar novas funcionalidades.

---

## 10. Resultado esperado

O principal resultado do FinanIA não é simplesmente realizar uma divisão matemática.

É demonstrar como a Inteligência Artificial pode transformar uma necessidade cotidiana em uma experiência simples e prática.

O usuário apresenta uma dúvida.

O sistema entende.

Identifica o que está faltando.

Utiliza informações confiáveis.

Realiza o cálculo.

Explica o resultado.

E apresenta um possível próximo passo.

---

## 11. Conclusão

O FinanIA demonstra uma aplicação prática de Inteligência Artificial generativa combinada com regras determinísticas, base de conhecimento e uma interface simples.

O projeto foi desenvolvido com uma preocupação central:

**a IA deve ser útil sem inventar informações.**

Por isso, quando sabe, responde.

Quando precisa de mais informações, pergunta.

Quando não possui informação suficiente, deixa isso claro.

Esse é o princípio que orienta o desenvolvimento do FinanIA.
