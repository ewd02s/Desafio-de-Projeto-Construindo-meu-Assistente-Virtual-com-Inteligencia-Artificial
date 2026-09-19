# 🤖 FinanIA — Assistente de Planejamento Financeiro

## 📌 Sobre o projeto

O **FinanIA** é um assistente financeiro baseado em Inteligência Artificial Generativa, desenvolvido para ajudar pessoas a transformar uma **meta financeira em um plano simples de economia**.

O assistente utiliza linguagem natural para compreender a necessidade da pessoa usuária, consultar uma base de conhecimento, realizar simulações financeiras demonstrativas e apresentar os resultados de forma simples e contextualizada.

O projeto combina conceitos de **Inteligência Artificial, Python, dados e UX (Experiência do Usuário)** em uma aplicação prática.

---

## 🎯 Problema

Muitas pessoas possuem objetivos financeiros, mas têm dificuldade para transformar esses objetivos em um plano.

Por exemplo:

> "Quero comprar um notebook de R$ 3.000, mas não sei quanto preciso guardar por mês."

Para responder a esse tipo de necessidade, o usuário precisa descobrir:

* Quanto precisa economizar;
* Em quanto tempo pode alcançar a meta;
* Se o valor mensal necessário cabe em seu planejamento;
* O que pode fazer caso o valor calculado seja muito alto.

O FinanIA foi pensado para simplificar esse processo.

---

## 💡 Solução

O FinanIA permite que a pessoa converse com o assistente utilizando linguagem natural.

A partir das informações fornecidas, o sistema pode:

1. Identificar a meta financeira;
2. Identificar o valor necessário;
3. Identificar o prazo disponível;
4. Solicitar informações que estejam faltando;
5. Realizar uma simulação;
6. Explicar o resultado;
7. Consultar informações da base de conhecimento;
8. Informar quando não possui dados suficientes;
9. Apresentar possíveis próximos passos.

### Exemplo

**Usuário:**

> Quero juntar R$ 3.000 em 6 meses.

**FinanIA:**

> Para alcançar uma meta de R$ 3.000 em 6 meses, você precisaria guardar aproximadamente R$ 500 por mês, considerando uma divisão simples do valor pelo número de meses e sem considerar juros, taxas ou rendimentos.
>
> Se R$ 500 por mês não for compatível com seu orçamento, podemos simular um prazo diferente.

---

# 👥 Público-alvo

O FinanIA foi pensado principalmente para:

* Pessoas que estão começando a organizar sua vida financeira;
* Pessoas que possuem uma meta de curto ou médio prazo;
* Usuários com pouca familiaridade com cálculos financeiros;
* Pessoas que desejam compreender melhor uma situação financeira antes de tomar uma decisão.

O projeto prioriza **linguagem simples**, evitando termos técnicos desnecessários.

---

# 🎯 Objetivo do assistente

O principal objetivo do FinanIA é ajudar a pessoa usuária a responder:

> **"Quanto preciso guardar por mês para alcançar minha meta financeira?"**

A partir dessa tarefa principal, o assistente também pode explicar conceitos relacionados ao planejamento de economia e ajudar a pessoa a avaliar possíveis cenários.

---

# 🧠 Como o FinanIA deve se comportar

O assistente deve:

* Compreender perguntas escritas em linguagem natural;
* Identificar informações importantes presentes na mensagem;
* Solicitar informações quando houver dados insuficientes;
* Utilizar a base de conhecimento para responder dúvidas;
* Realizar cálculos de forma consistente;
* Explicar como chegou ao resultado;
* Utilizar linguagem simples e objetiva;
* Manter o contexto da conversa quando necessário;
* Diferenciar cálculos e simulações de informações financeiras reais;
* Informar claramente suas limitações;
* Ajudar a pessoa a identificar um próximo passo.

---

# 🚫 O que o FinanIA não deve fazer

Para reduzir o risco de respostas incorretas ou inventadas, o assistente não deve:

* Inventar taxas de juros;
* Inventar rendimentos;
* Criar informações que não estejam disponíveis;
* Apresentar uma simulação como garantia de resultado;
* Fingir possuir acesso à conta bancária da pessoa;
* Solicitar senhas;
* Solicitar número de cartão;
* Solicitar códigos de segurança;
* Inventar produtos ou condições financeiras;
* Apresentar informações insuficientes como se fossem certezas.

Quando não possuir informação suficiente, o FinanIA deve **informar a limitação e solicitar os dados necessários**, quando apropriado.

---

# 🔐 Segurança e privacidade

O projeto foi pensado para funcionar sem necessidade de acesso a informações bancárias reais.

O FinanIA não deve solicitar:

* Senhas;
* Número completo de cartão;
* Código de segurança;
* Dados de autenticação;
* Informações bancárias desnecessárias.

As simulações devem utilizar apenas os dados necessários para realizar o cálculo.

---

# ⚠️ Limitações

O FinanIA é um **projeto educacional e demonstrativo**.

As simulações apresentadas não constituem recomendação financeira, oferta de crédito, recomendação de investimento ou garantia de resultado.

Os resultados dependem das informações fornecidas pela pessoa usuária e das premissas utilizadas no cálculo.

---

# 🧩 Escopo do MVP

A primeira versão do projeto será deliberadamente simples.

### Funcionalidades do MVP

* [ ] Conversação com o usuário;
* [ ] Identificação de meta financeira;
* [ ] Identificação do valor da meta;
* [ ] Identificação do prazo;
* [ ] Validação dos dados;
* [ ] Cálculo do valor mensal necessário;
* [ ] Base de conhecimento;
* [ ] Respostas baseadas na base de conhecimento;
* [ ] Tratamento de perguntas sem informação suficiente;
* [ ] Histórico/contexto básico da conversa;
* [ ] Interface simples para demonstração.

---

# 🛠️ Tecnologias previstas

| Tecnologia    | Utilização                           |
| ------------- | ------------------------------------ |
| Python        | Lógica da aplicação e cálculos       |
| IA Generativa | Interpretação e geração de respostas |
| JSON          | Base de conhecimento inicial         |
| Streamlit     | Interface da aplicação               |
| Git           | Controle de versão                   |
| GitHub        | Hospedagem do projeto                |

---

# 📂 Estrutura prevista

```text
finanIA/
│
├── README.md
├── app.py
├── calculadora.py
├── base_conhecimento.json
├── prompt.txt
├── avaliacao.md
├── pitch.md
│
└── testes/
    └── casos_teste.json
```

---

# 🔄 Fluxo básico

```text
Usuário
   ↓
Envia uma dúvida ou objetivo
   ↓
FinanIA interpreta a solicitação
   ↓
Existem informações suficientes?
   │
   ├── Não → Solicita informações
   │
   └── Sim
        ↓
Consulta a base de conhecimento
        ↓
Executa cálculo quando necessário
        ↓
Gera resposta contextualizada
        ↓
Explica o resultado
        ↓
Apresenta próximo passo possível
```

---

# 🧪 Exemplo de casos de uso

### Caso 1 — Simulação

**Usuário:**

> Quero juntar R$ 2.400 em 12 meses.

**Sistema:**

Calcula:

```text
R$ 2.400 ÷ 12 = R$ 200
```

E apresenta uma explicação simples.

---

### Caso 2 — Informação insuficiente

**Usuário:**

> Quero juntar dinheiro para comprar um celular.

**FinanIA:**

Solicita informações necessárias, como:

> Qual é o valor aproximado do celular e em quanto tempo você gostaria de alcançar essa meta?

---

### Caso 3 — Meta incompatível com o valor informado

**Usuário:**

> Quero juntar R$ 5.000 em 5 meses e consigo guardar R$ 500 por mês.

O assistente pode mostrar:

```text
Meta: R$ 5.000
Prazo: 5 meses
Necessário: R$ 1.000/mês
Disponível: R$ 500/mês
```

E explicar que existe uma diferença de R$ 500 por mês entre o valor necessário e o valor informado.

A partir disso, pode ajudar a pessoa a explorar alternativas, como alterar o prazo ou revisar o valor da meta.

---

# 📊 Critérios de sucesso

O MVP será considerado funcional quando conseguir:

1. Compreender uma solicitação relacionada à meta de economia;
2. Identificar os dados necessários;
3. Solicitar informações ausentes;
4. Realizar o cálculo corretamente;
5. Explicar o resultado;
6. Evitar informações inventadas;
7. Reconhecer quando não possui dados suficientes;
8. Manter o contexto básico da conversa;
9. Apresentar uma próxima ação possível.

---

# 🚀 Evolução futura

Depois do MVP, o projeto poderá evoluir para incluir:

* Categorias de metas;
* Simulação com juros compostos;
* Controle de orçamento;
* Registro de metas;
* Dashboard financeiro;
* Histórico de simulações;
* Personalização da experiência;
* Banco de dados;
* Autenticação;
* Integração com APIs financeiras em um ambiente apropriado;
* Avaliação automatizada das respostas.

Essas funcionalidades não fazem parte do escopo inicial.

---

# 📚 Objetivo educacional

O principal objetivo deste projeto é demonstrar, de forma prática, como a Inteligência Artificial pode apoiar uma pessoa em uma tarefa real.

Durante o desenvolvimento serão aplicados conhecimentos de:

* Inteligência Artificial Generativa;
* Engenharia de Prompts;
* Python;
* Manipulação de dados;
* Base de conhecimento;
* UX;
* Validação;
* Testes;
* Avaliação de respostas;
* Documentação de projetos.

---

# 👨‍💻 Autor

**Eder William**

Projeto desenvolvido como parte de um desafio prático de Inteligência Artificial.

---

## 📌 Status

**Em desenvolvimento 🚧**

O projeto será desenvolvido de forma incremental, começando pelo MVP e evoluindo conforme os resultados dos testes.
