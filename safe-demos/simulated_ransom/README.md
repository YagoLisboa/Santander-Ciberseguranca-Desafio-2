# simulated_ransom/README.md

## 🛡️ Simulação Segura de Ransomware (Didática e Inofensiva)

Este diretório contém materiais **100% seguros**, usados apenas para fins acadêmicos e demonstrativos.
Não há qualquer código malicioso, nem criptografia real, nem risco para o sistema.
Tudo aqui serve **exclusivamente para estudo**, mostrando a *lógica conceitual* de um ransomware.

---

## 📘 Objetivo do Diretório

Este módulo demonstra:

* Como um ransomware **seria organizado conceitualmente**;
* Como arquivos podem ser **codificados de forma reversível** usando Base64;
* Como registrar logs e gerar artefatos para análise;
* Como **documentar com segurança** um experimento de cibersegurança em laboratório.

---

## 📂 Conteúdo da Pasta

```
simulated_ransom/
├── README.md               ← Este documento
├── files/                  ← Arquivos de teste (txt) usados como "vítimas"
└── exemplo_processo.txt    ← Descrição passo a passo da demonstração
```

### Sobre a pasta `files/`

Aqui ficam arquivos de texto simples, como:

```
files/
├── documento1.txt
├── trabalho_final.txt
├── dados_ficticios.txt
```

Eles são usados apenas para simular um processo de "codificação" e "decodificação".

---

## 🔒 Como funciona a simulação

A demonstração utiliza o script **safe_demos.py** (na pasta raiz `safe-demos/`).
Ele contém funções como:

* `simulate_encrypt(text)` → codifica string em Base64;
* `simulate_decrypt(text)` → reverte a codificação;
* Registros de log e prints explicativos.

⚠️ **Nada aqui criptografa arquivos reais do sistema.**
Tudo ocorre em memória ou em arquivos de teste dentro da pasta `files/`.

---

## ▶️ Passo a Passo da Demonstração

1. Copie alguns arquivos para a pasta `files/`.
2. Edite o script `safe_demos.py` se quiser alterar textos ou arquivos de exemplo.
3. Execute:

```
python3 safe_demos.py
```

4. Observe:

   * Texto original sendo exibido no console;
   * Texto codificado em Base64;
   * Texto decodificado de volta ao original;
   * Logs fictícios representando ações típicas de um ransomware.

---

## 📌 Observação Importante

Este material **não representa malware real**.
É uma simulação segura voltada a estudantes, professores e análises acadêmicas.
