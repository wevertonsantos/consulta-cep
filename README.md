# 🔍 Consulta de CEP com API ViaCEP

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

Um projeto simples e funcional para **consulta de endereços no Brasil via CEP**, utilizando a **API pública ViaCEP**.  
O objetivo é demonstrar habilidades práticas em **consumo de API REST** e **tratamento de dados JSON**.

## 🚀 Funcionalidades

- Consulta qualquer CEP válido do Brasil.
- Exibe informações completas: **logradouro, complemento, bairro, cidade e estado**.
- Validação de formato de CEP (8 dígitos numéricos).
- Tratamento de erros de conexão e CEP inexistente.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Biblioteca Requests** (requisições HTTP)
- **API ViaCEP** ([https://viacep.com.br/](https://viacep.com.br/))
- Manipulação de **JSON**
- **Tratamento de exceções** e fluxo interativo

## 📦 Como Executar o Projeto

1. **Clonar este repositório**
```bash
git clone https://github.com/wevertonsantos/consulta-cep.git
cd consulta-cep
```

2. **Instalar dependências**
```bash
pip install requests
```

3. **Executar**
```bash
python cep.py
```

---

## 💻 Exemplo de Uso

```
Digite o CEP (apenas números) : 01001000

📍 Resultado da consulta:
Rua: Praça da Sé
Complemento: lado ímpar
Bairro: Sé
Cidade: São Paulo - SP
```

## 📚 Aprendizados

Durante o desenvolvimento, foram aplicados conceitos como:
- Consumo de **API REST** usando Python.
- Manipulação e leitura de **JSON**.
- Estruturação de código com funções.
- Boas práticas de tratamento de erros.
- Validação de dados de entrada do usuário.

## 📫 Contato
Se quiser falar comigo sobre o projeto ou oportunidades:
- 💼 [LinkedIn](https://linkedin.com/in/wevertonsantoss)
- 📧 wevercanal@gmail.com