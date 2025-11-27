# simulated_keylogger/README.md

## ⌨️ Simulação Segura de Keylogger (Didática e Inofensiva)

Este diretório contém arquivos usados para **simular** o funcionamento conceitual de um keylogger, **sem capturar teclas reais**.
A simulação é completamente segura, controlada e adequada para fins acadêmicos.

---

## 🎯 Objetivo do Diretório

Demonstrar, de forma segura e sem risco, como seria o fluxo de:

* Registro de eventos;
* Geração de logs;
* Armazenamento de dados simulados;
* Uso do script `safe_demos.py` para gerar logs fictícios.

**Nenhum método aqui captura teclado do usuário.**
Apenas gera caracteres artificiais para estudo.

---

## 📂 Conteúdo da Pasta

```
simulated_keylogger/
├── README.md               ← Este documento
├── input_simulado.txt      ← Conteúdo textual simulado, como se fosse digitado
└── registro_simulado.txt   ← Logs fictícios gerados artificialmente
```

### Exemplos de conteúdo

`input_simulado.txt`:

```
TESTE DE ENTRADA DE TEXTO FICTÍCIO
```

`registro_simulado.txt`:

```
[2025-09-10 13:45:22] KEY: T
[2025-09-10 13:45:22] KEY: E
[2025-09-10 13:45:23] KEY: S
...
```

Esses arquivos servem para ilustrar como um keylogger **real** estruturaria seus dados — mas de forma completamente inofensiva.

---

## 🛡️ Como a simulação funciona

O script `safe_demos.py` (pasta `/safe-demos/`) possui uma função:

```
generate_fake_keylogs()
```

que:

* Cria um log com caracteres aleatórios;
* Não captura teclado real;
* Simula timestamps e comportamento;
* Gera um arquivo `.txt` com o conteúdo fictício.

Essa abordagem respeita boas práticas de segurança e evita qualquer comportamento malicioso.

---

## ▶️ Como Executar a Demonstração

1. Abra a pasta `safe-demos/`.
2. Execute o script:

```
python3 safe_demos.py
```

3. O script criará um arquivo como:

```
fake_keylog.txt
```

4. Compare esse arquivo com `registro_simulado.txt` para análise.

Isso permite explicar **conceitos de keyloggers reais**, sem realizar captura alguma.

---
