# 📝 Melhorias Visuais - Study Manager

## Data: 19/08/2026

Este arquivo documenta as melhorias visuais aplicadas ao projeto Study Manager, mantendo a essência original.

---

## 1. CSS Base (`templates/base.html`)

### Paleta de Cores
- Adicionadas variáveis CSS (`:root`) para padronização de cores
- Cores: `--primary: #1a1a2e`, `--accent: #0f3460`, `--accent-light: #533483`
- Background suave: `--bg: #f0f2f5`

### Navbar
- Gradiente suave no background da navbar
- Sombras sutis (`box-shadow`)
- Links com transição hover e borda arredondada

### Tipografia
- Fonte trocada para `Segoe UI` (mais moderna)
- Headers com cor `--primary` padronizada

### Cards
- Border-radius aumentado para `16px` (mais arredondado)
- Sombras suaves com `box-shadow`
- Efeito hover com `translateY(-2px)` e sombra maior

### Botões
- Gradiente suave nos botões `btn-dark`
- Efeito hover com sombra e transição
- Bordas arredondadas `rounded-pill` mantidas

### List Items (Task List)
- Border-radius `12px` com sombra suave
- Efeito hover com `translateX(4px)` (desliza para direita)

### Formulários
- Inputs com bordas arredondadas `10px`
- Focus state com cor `--accent` e sombra sutil
- Labels com font-weight `600` e cor `--primary`

### Progress Bar
- Gradiente verde no preenchimento
- Animação de transição suave

---

## 2. Dashboard (`templates/tasks/dashboard.html`)

- Cards com classes CSS específicas: `.total`, `.completed`, `.pending`, `.late`
- Cada card com borda esquerda colorida (azul, verde, amarelo, vermelho)
- Ícones emoji em cada card: 📋, ✅, ⏳, 🔴
- Título com emoji: 📊 Dashboard
- Seção de progresso melhorada com label "Progresso Geral"

---

## 3. Homepage (`templates/core/home.html`)

- Título maior com `display-4` e ícone 📚
- Espaçamento vertical maior (`margin-top: 80px`)
- Subtítulo centralizado com largura máxima
- Botões maiores (`btn-lg`)
- Seção de funcionalidades em grid de 4 colunas
- Cada funcionalidade em card com ícone emoji
- Cards de funcionalidade: 📝, 📚, 📅, 📊

---

## 4. Login (`templates/registration/login.html`)

- Ícone de boas-vindas: 👋
- Título mais acolhedor: "Bem-vindo de volta!"

---

## 5. Signup (`templates/registration/signup.html`)

- Ícone de criação: ✨
- Header com ícone e título centralizado

---

## 6. Lista de Subjects (`templates/subjects/subject_list.html`)

- Título com ícone: 📚 Subjects
- Botão de criar com ícone: ➕ Novo Subject

---

## 7. Lista de Tasks (`templates/tasks/task_list.html`)

- Título com ícone: 📋 Lista de Tasks
- Botão de criar com ícone: ➕ Nova Task

---

## 8. Formulário de Tasks (`templates/tasks/task_form.html`)

- Botão de criar subject com ícone: ➕ Criar novo Subject

---

## Resumo das Melhorias

| Aspecto | Antes | Depois |
|---------|-------|--------|
| Fonte | Arial | Segoe UI |
| Cores | Padrão Bootstrap | Paleta customizada com CSS vars |
| Cards | Bordas simples | Sombras + hover effects |
| Navbar | Background sólido | Gradiente suave |
| Botões | Bootstrap padrão | Gradiente + hover animado |
| Dashboard | Cards genéricos | Cards coloridos com ícones |
| Home | Lista simples | Grid de cards com ícones |
| Formulários | Padrão | Bordas arredondadas + focus states |
| Listas | Itens simples | Hover effects sutis |

---

## Nota

Todas as melhorias são **visuais apenas**. A lógica do Django, models, views e URLs não foram alteradas.
