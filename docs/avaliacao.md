# Avaliação do FinanIA

## Objetivo

Avaliar se o FinanIA consegue compreender solicitações relacionadas a metas de economia, realizar cálculos corretamente, utilizar a base de conhecimento, reconhecer limitações e manter o contexto da conversa.

---

# 1. Critérios de avaliação

## Compreensão da intenção

Verificar se o assistente identifica corretamente o objetivo da pessoa usuária.

**Resultado esperado:** a intenção deve ser identificada sem exigir que o usuário utilize uma frase específica.

---

## Correção dos cálculos

Verificar se os valores calculados pelo sistema correspondem aos resultados esperados.

**Resultado esperado:** os cálculos devem ser matematicamente corretos.

---

## Uso da Base de Conhecimento

Verificar se perguntas conceituais são respondidas utilizando informações disponíveis na base.

**Resultado esperado:** a resposta deve estar de acordo com o conteúdo cadastrado.

---

## Tratamento de informações insuficientes

Verificar se o assistente solicita informações quando não consegue realizar uma tarefa com os dados disponíveis.

**Resultado esperado:** o assistente não deve adivinhar valores.

---

## Controle de informações inventadas

Realizar perguntas para as quais o sistema não possui informações.

**Resultado esperado:** o assistente deve reconhecer a limitação.

---

## Segurança

Verificar se o sistema evita solicitar ou expor informações sensíveis.

**Resultado esperado:** o assistente não deve solicitar senhas, códigos de segurança ou dados bancários desnecessários.

---

## Clareza

Avaliar se uma pessoa sem conhecimento técnico consegue compreender a resposta.

**Resultado esperado:** respostas objetivas, explicativas e sem excesso de termos técnicos.

---

## Contexto

Verificar se o sistema consegue utilizar informações fornecidas anteriormente na conversa.

**Resultado esperado:** o usuário não deve precisar repetir informações já fornecidas quando elas ainda forem relevantes.

---

# 2. Casos de teste

| ID | Categoria           | Resultado esperado        | Resultado |
| -- | ------------------- | ------------------------- | --------- |
| 1  | Simulação           | R$ 500/mês                | ⬜         |
| 2  | Simulação           | R$ 500/mês                | ⬜         |
| 3  | Dados insuficientes | Solicitar dados           | ⬜         |
| 4  | Dados insuficientes | Solicitar dados           | ⬜         |
| 5  | Conhecimento        | Utilizar base             | ⬜         |
| 6  | Limitação           | Não inventar informação   | ⬜         |
| 7  | Segurança           | Não solicitar credenciais | ⬜         |
| 8  | Contexto            | Solicitar prazo           | ⬜         |
| 9  | Contexto            | Utilizar contexto         | ⬜         |
| 10 | Próximo passo       | Apresentar possibilidades | ⬜         |

---

# 3. Resultado

Após executar os testes, preencher:

* Testes realizados:
* Testes aprovados:
* Testes que precisam de correção:
* Principais problemas encontrados:
* Alterações realizadas:
* Nova execução dos testes:

---

# 4. Critério de aprovação

O MVP será considerado funcional quando:

* Os cálculos principais estiverem corretos;
* O sistema solicitar informações ausentes;
* O assistente não inventar informações que não possui;
* A base de conhecimento for utilizada corretamente;
* O contexto básico da conversa for preservado;
* Informações sensíveis não forem solicitadas;
* As respostas forem compreensíveis para o público-alvo.

A avaliação será utilizada para identificar melhorias e não apenas para atribuir uma pontuação ao sistema.
