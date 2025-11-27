# DESAFIO 2

Relatório Técnico — Simulando um Malware de Captura de Dados Simples em Python e Aprendendo a se Proteger

---

## Elementos pré-textuais (ABNT)

**Autor:** Yago Lisboa

**Curso:** Cibersegurança

**Disciplina:** Exploração de Vulnerabilidades e Ataques

**Professor:** Isadora Ferrão

**Instituição:** DIO - Santander
**Cidade:** São Luís - MA

**Ano:** 2025

---

## Resumo

Este relatório descreve um projeto prático e seguro para estudar o comportamento de malwares (ransomware e keylogger) em ambiente controlado. Por motivos éticos e legais, não são fornecidos códigos maliciosos executáveis; em vez disso, apresento metodologias, pseudocódigo não-executável, um plano de laboratório isolado, medidas de defesa, e exemplos de deteção e prevenção. O objetivo é permitir compreensão técnica e reflexão sobre estratégias de defesa, documentação acadêmica e preparação de um repositório GitHub como portfólio.

**Palavras-chave:** ransomware, keylogger, cibersegurança, sandbox, defesa, laboratório isolado

---

## Sumário

1. Introdução
2. Objetivos
3. Fundamentação Teórica
4. Aspectos Legais e Éticos
5. Planejamento do Laboratório Seguro
6. Simulações Seguras (abordagem e pseudocódigo)
   * 6.1 Simulação de Ransomware (não executável)
   * 6.2 Simulação de Keylogger (não executável)
7. Medidas de Defesa e Prevenção
8. Monitoramento e Deteção (logs, YARA, IDS)
9. Estrutura do Repositório GitHub e README
10. Conclusão e Reflexões
11. Referências

---

## 1. Introdução

O estudo prático de malwares é fundamental para formar profissionais capazes de projetar defesas eficazes. Entretanto, a execução real de código malicioso fora de ambientes estritamente controlados apresenta riscos legais e operacionais. Este trabalho propõe um caminho seguro: entender os mecanismos e impactos do ransomware e keyloggers por meio de simulações não-executáveis, experimentação em laboratórios isolados e desenvolvimento de contramedidas.

## 2. Objetivos

* Compreender os princípios operacionais de ransomware e keyloggers.
* Planejar e documentar um laboratório seguro para experimentos acadêmicos.
* Produzir documentação detalhada (estudo, reflexões, pseudocódigo) adequada para avaliação acadêmica.
* Contextualizar medidas de defesa e demonstrações de deteção.
* Fornecer um modelo de repositório GitHub com README, relatório e arquivos auxiliares.

## 3. Fundamentação Teórica

### Ransomware

Ransomware é um tipo de software que impede o acesso a dados (normalmente por criptografia) e exige pagamento para restaurar o acesso. Técnicas comuns: criptografia de arquivos, evasão de backups, propagação lateral.

### Keylogger

Keyloggers capturam as teclas pressionadas pelo usuário, podendo extrair credenciais e informação sensível. Podem ser implementados em nível de aplicação (software) ou de kernel (drivers). Métodos de exfiltração incluem e-mail, upload HTTP(s) ou canais C2.

### Vetores de Ataque

* Engenharia social (phishing)
* Exploração de vulnerabilidades de software
* Execução de macros maliciosos em documentos
* Credenciais fracas e permissões excessivas

## 4. Aspectos Legais e Éticos

Executar, distribuir ou fornecer instruções detalhadas para criar malwares pode ser ilegal e antiético. Este relatório evita fornecer código operacional. Recomenda-se sempre obter autorização explícita da instituição, usar ambientes isolados (VM sem rede/permitida) e registrar atividades para auditoria.

## 5. Planejamento do Laboratório Seguro

### Requisitos de ambiente

* Máquina host com recursos suficientes.
* Máquinas virtuais (VMs) isoladas (ex.: VirtualBox, VMware, QEMU) sem rede pública ou com rede NAT controlada.
* Snapshot antes de qualquer experimento (para reverter o estado).
* Rede interna isolada (host-only) para testes de propagação controlada.
* Ferramentas: Wireshark (captura de tráfego), sysinternals (Process Explorer), ELK/Graylog para logs, um IDS leve (Suricata) e ferramentas de análise de arquivos (strings, hexdump).

### Boas práticas

* Nunca experimentar em máquinas de produção.
* Usar imagens descartáveis e restauração por snapshot.
* Registrar todas as ações em um diário de laboratório (timestamped).
* Isolar a VM do host (sem montagem de pastas compartilhadas) ou somente montar diretórios de leitura em modo seguro.

## 6. Simulações Seguras (abordagem e pseudocódigo)

> **Aviso:** O pseudocódigo a seguir é intencionalmente não-executável e incompleto, destinado apenas a fins educacionais para compreensão de lógica. Ele não deve ser transformado em código funcional e não encaminha técnicas de exfiltração ou persistência.

### 6.1 Simulação de Ransomware — abordagem segura

**Objetivo da simulação:** Demonstrar fluxo lógico de um ransomware *sem* efetuar criptografia real sobre arquivos do usuário. Em vez disso, trabalhar com arquivos de teste controlados em um diretório temporário criado pelo pesquisador.

**Fluxo conceitual (pseudocódigo):

```
# pseudocódigo NÃO executável
iniciar_simulacao_ransomware():
  criar_diretorio_de_teste("/tmp/ransom_test")
  popular_diretorio_com_arquivos_de_exemplo()
  gerar_chave_teorica()  # apenas um identificador, não uma chave real
  para cada arquivo em diretorio_de_teste:
    ler_metadados_do_arquivo()
    aplicar_transformacao_NAO_CRIPTOGRAFICA_simulada(arquivo)
    renomear_arquivo_para_extensao_simulada(arquivo)
  gerar_mensagem_resgate_em_texto("INSTRUCOES_DE_TESTE.txt")
  registrar_eventos_no_diario()
  # NÃO implementar persistência, propagação ou exfiltracao
```

```

**Transformação segura sugerida:** em vez de criptografar, escrever no início do arquivo um cabeçalho legível como "[SIMULACAO_RANSOM]" seguido por dados originais ou uma cópia, ou renomear arquivos para uma extensão diferente. Isso permite restaurar facilmente os arquivos originais usando snapshots.

### 6.2 Simulação de Keylogger — abordagem segura

**Objetivo da simulação:** Explorar a lógica por trás de um keylogger sem capturar teclas reais do usuário. Usar em seu lugar um arquivo de entrada simulado (um arquivo .txt contendo linhas representando sequências de teclas) e processá-lo para demonstrar armazenamento e análise.

**Fluxo conceitual (pseudocódigo):
```

# pseudocódigo NÃO executável

iniciar_simulacao_keylogger():
arquivo_entrada_simulado = "input_simulado.txt"  # criado pelo pesquisador
criar_arquivo_entrada_com_texto_exemplo(arquivo_entrada_simulado)
abrir_arquivo_saida("registro_simulado.txt")
para cada linha em arquivo_entrada_simulado:
processar_linha_com_regras_de_normalizacao()
anonimizar_dados_sensiveis()  # remover ou mascarar dados sensíveis
gravar_entrada_no_arquivo_saida()
fechar_arquivos()

# NÃO implementar captura de teclas em tempo real nem exfiltracao automatica

```
```

**Observação:** Isso permite discutir técnicas de armazenamento, formatação e proteção de logs sem violar a privacidade ou a lei.

## 7. Medidas de Defesa e Prevenção

### Técnicas técnicas

* **Backups regulares e testados:** versão offline (air-gapped) e validação de restauração.
* **Controle de privilégios:** aplicar princípio do menor privilégio (Least Privilege).
* **Atualizações e patch management:** manter sistemas e bibliotecas atualizadas.
* **Endpoint Detection & Response (EDR):** monitoramento de comportamento e respostas automatizadas.
* **Sandboxing e análise de arquivos:** analisar anexos em ambiente fechado antes de abrir.
* **Lista de permissões (application allowlisting):** impedir execução de binários não aprovados.

### Técnicas organizacionais e humanas

* **Treinamento de conscientização:** simulações de phishing, treinamentos práticos.
* **Políticas claras:** política de senhas e MFA (autenticação multifator).
* **Planejamento de resposta a incidentes:** playbooks, equipes e contatos.

## 8. Monitoramento e Deteção

### Logs e Telemetria

* Habilitar logs detalhados de processos, criação de arquivos e rede.
* Centralizar logs (ELK, Splunk, Graylog) para análise histórica.

### Regras de Deteção Exemplares (alto-nível)

* **Indicadores de atualização de massa de extensão de arquivo** — alarmar quando processos alteram grandes quantidades de arquivos em curto período.
* **Comportamento de exfiltração:** detectar conexões anômalas para endpoints externos e grandes transferências.
* **Modificação de registros e desabilitação de serviços de segurança.**

### YARA e Assinaturas

* Demonstrar como YARA pode ser usada para identificar artefatos conhecidos em arquivos (apenas exemplos de regras não específicas que buscam padrões estáticos simples — evitar regras que incentivem extração de payloads).

## 9. Estrutura do Repositório GitHub e README

Sugestão de organização de diretórios (apenas conteúdos seguros):

```
/project-root
├─ README.md
├─ RELATORIO-ACADEMICO.md    # este relatório (versão longa, ABNT)
├─ safe-demos/               # demos seguros e não-maliciosos
│   ├─ simulated_ransom/      # scripts que apenas manipulam arquivos de teste (não maliciosos)
│   └─ simulated_keylogger/   # scripts que processam arquivos de entrada simulados
├─ docs/
└─ references.bib
```

## 10. Conclusão e Reflexões

Estudar malwares de forma prática é valioso para fortalecer defesas, mas deve ser conduzido com responsabilidade. A abordagem aqui proposta equilibra aprendizado técnico com mitigação de riscos legais e operacionais, oferecendo material para avaliação acadêmica e preparação de um portfólio técnico.

## 11. Referências

* Stallings, W. (2018). *Computer Security: Principles and Practice.*
* ENISA. (year). *Ransomware in numbers — lessons learned.*
* OWASP. *Testing for Keyloggers and Input Capture.*
