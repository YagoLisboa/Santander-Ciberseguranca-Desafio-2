# Santander-Ciberseguranca-Desafio-2
Neste desafio eu vou simular um malware de captura de dados simples em Python e aprender a me proteger.

# Simulação Segura de Malware — Projeto Acadêmico

Este repositório contém um conjunto de **simulações seguras**, **documentação acadêmica** e **estudos** sobre o funcionamento de ransomware e keyloggers em ambientes controlados, seguindo princípios éticos e legais. **Nenhum código malicioso ou executável prejudicial está incluído.**

O objetivo deste projeto é permitir entendimento técnico sem riscos, auxiliar no desenvolvimento de portfólio e atender aos requisitos acadêmicos da disciplina de Cibersegurança.

---

## 📌 Objetivos do Projeto

* Compreender o funcionamento lógico de ransomware e keyloggers.
* Simular seus comportamentos de forma **não maliciosa** e **não executável**.
* Documentar aprendizados, reflexões e processos de defesa.
* Criar um repositório GitHub organizado e profissional.
* Demonstrar boas práticas de laboratório seguro.

---

## 📁 Estrutura do Repositório

```
/project-root
├─ README.md                       # Este arquivo
├─ RELATORIO-ACADEMICO.md          # Versão detalhada em formato ABNT
├─ TEMPLATE-SCREENSHOTS.md         # Guia para capturas de tela do laboratório
├─ safe-demos/                      # Simulações seguras e não maliciosas
│   ├─ simulated_ransom/            # Demonstrações de "criptografia" fictícia
│   └─ simulated_keylogger/         # Processamento de entradas simuladas
├─ docs/                            # Material complementar
└─ references.bib                   # Referências em BibTeX (opcional)
```

---

## 🧪 Ambiente Seguro Recomendado

Para evitar riscos e seguir boas práticas, todas as simulações devem ser executadas em **máquina virtual isolada**.

**Requisitos sugeridos:**

* VirtualBox ou VMware
* VM Linux ou Windows isolada (sem acesso à rede pública)
* Snapshots antes de cada experimento
* Pasta de trabalho dedicada (sem acessar documentos pessoais)

**Ferramentas úteis:**

* Wireshark (captura de tráfego)
* Process Explorer / Sysinternals
* ELK, Graylog ou Wazuh (logs e análise)
* Suricata (IDS)

---

## 🧩 Conteúdo Técnico (Seguro)

As simulações deste repositório **não** executam comportamentos maliciosos reais. Em vez disso, usam:

### 🔐 Ransomware Simulado

* Manipulação de arquivos de teste criados pelo usuário.
* Renomeação ou alteração fictícia do conteúdo (sem criptografia real).
* Geração de "mensagem de resgate" meramente ilustrativa.
* Pseudocódigo explicativo totalmente inofensivo.

### ⌨️ Keylogger Simulado

* Processamento de um arquivo **input_simulado.txt** contendo teclas fictícias.
* Registro em **registro_simulado.txt**.
* Anonimização e normalização de dados.
* Nenhuma captura real de teclado.

Esses procedimentos permitem compreender lógica, sem qualquer risco técnico ou ético.

---

## 🛡️ Estratégias de Defesa Documentadas

O relatório inclui discussões sobre:

* Antivírus e EDR
* Firewall e filtragem de tráfego
* Sandboxing
* Hardening do sistema
* Backups e políticas de recuperação
* Conscientização do usuário
* Monitoramento e detecção (YARA, logs, IOC comportamental)

---

## 📚 Documentação Acadêmica

Todo o material teórico e reflexivo está no arquivo:

* **RELATORIO-ACADEMICO.md**

Esse arquivo segue padrão **ABNT**, incluindo:

* Elementos pré-textuais
* Fundamentação teórica
* Aspectos éticos e legais
* Planejamento do laboratório seguro
* Reflexões sobre defesa
* Referências

---

## 📸 Capturas de Tela

As instruções oficiais estão em:

* **TEMPLATE-SCREENSHOTS.md**

Você encontrará:

* O que capturar no laboratório
* Como anotar cada imagem
* Padrões de resolução
* Dicas de organização

---

## ⚠️ Aviso Legal

Este repositório tem **exclusivamente fins educacionais e acadêmicos**.
Nenhuma parte deve ser usada para criação, distribuição ou execução de softwares maliciosos.
Todas as simulações foram projetadas para serem **100% seguras e éticas**.
