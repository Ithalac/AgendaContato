# 📒 Agenda de Contatos

Este projeto é uma aplicação de terminal feita em Python para gerenciar contatos pessoais e profissionais. O sistema permite adicionar, listar, editar e remover contatos, armazenando os dados localmente de forma persistente.

---

## 📌 Definição do Problema

Manter o controle de contatos pessoais e profissionais pode ser difícil sem uma ferramenta centralizada. Este projeto resolve esse problema ao oferecer uma agenda digital simples, funcional e organizada, com interface em linha de comando, onde é possível cadastrar e editar facilmente dados como nome, telefone, data de nascimento ou empresa.

---

## ✅ Casos de Uso

### 1. Criar Contato
- O usuário escolhe se deseja cadastrar um contato pessoal ou profissional.
- Para **contato pessoal**, são solicitados: nome, telefone, data de nascimento (formato DDMMAAAA).
- Para **contato profissional**, são solicitados: nome, telefone, empresa.

### 2. Ver Contatos
- Mostra todos os contatos cadastrados com seus dados.
- Exibe o índice numérico de cada contato (usado para editar ou remover).

### 3. Editar Contato
- O usuário informa o número do contato que deseja editar.
- Os campos existentes são exibidos e o usuário pode alterá-los ou pressionar Enter para manter os atuais.
- Para contatos pessoais, a data de nascimento digitada como `DDMMAAAA` é automaticamente formatada como `DD/MM/AAAA`.

### 4. Remover Contato
- O usuário informa o número do contato que deseja remover.
- O contato é excluído da agenda e a alteração é salva.

### 5. Armazenamento Local
- Todos os contatos são salvos automaticamente em um arquivo local (`contatos.pkl`) usando serialização com `pickle`.
- Os dados são carregados automaticamente ao iniciar a agenda.

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Paradigma Orientado a Objetos
- Serialização com Pickle


