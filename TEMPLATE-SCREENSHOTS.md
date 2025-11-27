# TEMPLATE DE SCREENSHOTS — Laboratório de Cibersegurança

Este documento serve como guia para padronizar **todas as capturas de tela** utilizadas no relatório acadêmico e no repositório do projeto. Seguir este template garante organização, clareza e validação adequada das evidências.

---

## 📌 Padrões Gerais para Todas as Capturas de Tela

### ✔ Resolução Recomendada

* **Mínimo:** 1280×720
* **Ideal:** 1920×1080
* Utilize o modo janela maximizada quando possível.

### ✔ Formato

* PNG preferencial
* JPG permitido

### ✔ Nome do Arquivo

Use sempre o padrão:

```
XX-nome-curto-descritivo.png
```

Onde **XX** é a ordem das imagens no relatório.

Exemplos:

```
01-criacao-diretorio-teste.png
02-lista-arquivos-simulacao.png
03-processos-monitorados.png
```

### ✔ Elementos Obrigatórios em Todas as Imagens

* Data e hora visíveis **OU** referenciadas na legenda.
* Janela principal claramente legível.
* Sem informações pessoais.
* Evitar fundo bagunçado ou múltiplas janelas abertas sem função.

---

## 📸 1. Capturas de Tela do Ambiente de Laboratório

Estas imagens comprovam que o ambiente é **isolado e seguro**.

### O que capturar:

* Configuração da máquina virtual (VirtualBox/VMware)
* Tela de snapshot antes da simulação
* Configurações de rede (NAT, Host-Only ou Sem Internet)

### Exemplos:

* `01-configuracao-vm.png`
* `02-snapshot-inicial.png`
* `03-configuracao-rede.png`

### Legenda padrão:

> *Figura XX — Configuração da máquina virtual antes do início da simulação.*

---

## 🔐 2. Capturas — Simulação de Ransomware

Estas imagens documentam **simulações seguras**, sem qualquer código malicioso real.

### O que capturar:

* Diretório de arquivos de teste criado para a simulação
* Arquivos antes e depois da renomeação/transformação fictícia
* Execução do script seguro em modo terminal
* Mensagem de “resgate” simulada gerada pelo programa

### Exemplos:

* `10-pasta-de-teste-ransom.png`
* `11-arquivos-transformados.png`
* `12-mensagem-resgate-simulada.png`

### Legenda padrão:

> *Figura XX — Transformação simulada dos arquivos de teste.*

---

## ⌨️ 3. Capturas — Simulação de Keylogger

Aqui você registrará apenas **processamento de arquivos simulados**, nunca captura real de teclado.

### O que capturar:

* Conteúdo do arquivo `input_simulado.txt`
* Execução do script seguro processando o arquivo
* Resultado em `registro_simulado.txt`
* Processo no monitor de tarefas (opcional)

### Exemplos:

* `20-arquivo-input-simulado.png`
* `21-processamento-simulado.png`
* `22-resultado-log-simulado.png`

### Legenda padrão:

> *Figura XX — Processamento simulado das entradas de teclado fictícias.*

---

## 🛡️ 4. Capturas — Segurança, Logs e Auditoria

Essas imagens comprovam que você analisou o comportamento esperado em um laboratório controlado.

### O que capturar:

* Logs de sistema (Linux: `/var/log`, Windows: Event Viewer)
* Monitoramento de processos
* Resultados de regras YARA genéricas (não específicas de malware real)
* Alertas ou comportamentos suspeitos detectados pelo IDS (quando aplicável)

### Exemplos:

* `30-processos-monitorados.png`
* `31-logs-simulacao.png`
* `32-regra-yara-exemplo.png`

### Legenda padrão:

> *Figura XX — Registro e análise de logs durante a simulação.*

---

## 📝 5. Como Inserir Screenshots no Relatório

Use o seguinte formato em Markdown:

```
![Figura XX — descrição da imagem](./screenshots/XX-nome.png)
```

Ou em ABNT:

> *Figura XX — Descrição.*
> Fonte: Elaborado pelo autor (2025).

---

## 🎯 Recomendações Finais

* A numeração deve seguir a ordem do relatório.
* Mantenha todas as imagens dentro da pasta `/screenshots/`.
* Revise cada captura antes de enviar para o GitHub.
* Não inclua informações pessoais, e-mails ou senhas.

---
