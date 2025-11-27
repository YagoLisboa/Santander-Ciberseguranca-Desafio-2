# PLAYBOOK DE RESPOSTA A INCIDENTES — CIBERSEGURANÇA

Este playbook apresenta procedimentos padronizados para **Resposta a Incidentes (RI)** em ambiente corporativo ou acadêmico. Ele deve ser utilizado como guia para documentar, reagir e mitigar ameaças de maneira coordenada e eficiente.

> **Este documento é seguro:** contém apenas práticas de defesa, não possui código malicioso nem instruções que comprometam sistemas.

---

## 📌 1. Preparação (ANTES DO INCIDENTE)

Objetivo: garantir que a organização possua ferramentas, processos e pessoal treinado.

### Atividades

* Manter inventário atualizado de ativos (hardware, software, versões).
* Criar snapshots e backups regulares — e **testar restaurações**.
* Implantar antivírus/EDR com monitoramento em tempo real.
* Configurar logs centralizados (SIEM, ELK, Wazuh, Graylog).
* Estabelecer papéis da equipe:

  * **Líder de RI:** coordena ações.
  * **Analista Técnico:** coleta evidências.
  * **Gestor de Comunicação:** faz comunicações internas.
* Definir canais de comunicação:

  * E-mail interno da equipe
  * Grupo seguro (Signal, Teams, Slack privado)
* Treinar equipes com simulações periódicas (tabletop exercises).

### Evidências coletáveis

* Checklist de configuração do ambiente.
* Logs de funcionamento do SIEM.
* Políticas de backup e restauração.

---

## 🚨 2. Identificação (DETECÇÃO DO INCIDENTE)

Objetivo: confirmar se um evento é realmente um incidente.

### Sinais de alerta

* Alterações massivas de arquivo (possível ransomware).
* Processos desconhecidos ou consumo anormal de CPU/RAM.
* Tentativas repetidas de login (brute-force).
* Conexões suspeitas com IPs externos incomuns.
* Mensagens de extorsão ou comportamento inesperado do sistema.

### Ações recomendadas

1. Registrar data e hora da detecção.
2. Documentar o alerta no SIEM/EDR.
3. Capturar logs imediatamente.
4. Salvar estado atual da máquina (snapshot ou imagem forense, se possível).

### Evidências coletáveis

* Logs de sistema, rede e autenticação.
* Capturas de tela do comportamento suspeito.
* Hashes dos arquivos suspeitos (quando aplicável).

---

## 🧯 3. Contenção (CURTO PRAZO)

Objetivo: impedir que o incidente se espalhe.

### Ações de contenção imediata

* Isolar a máquina da rede (desativar Wi-Fi, remover cabo, VLAN isolada).
* Bloquear processos suspeitos no EDR.
* Revogar credenciais comprometidas.
* Bloquear portas de rede suspeitas no firewall.

### Contenção de longo prazo

* Criar nova política temporária bloqueando execução de arquivos desconhecidos.
* Restringir acesso administrativo.
* Aumentar nível de logs temporariamente.

### Evidências coletáveis

* Registro de bloqueios no EDR.
* Logs de ações de firewall.
* Estado do host isolado.

---

## 🧹 4. Erradicação

Objetivo: remover completamente a ameaça do ambiente.

### Ações recomendadas

* Identificar o vetor de ataque (phishing, vulnerabilidade, credencial exposta).
* Remover arquivos maliciosos ou suspeitos.
* Aplicar patches e atualizações pendentes.
* Restaurar arquivos modificados com base em backups ou snapshots.
* Fazer varredura completa no sistema com antivírus/EDR.

### Evidências coletáveis

* Relatórios de antivírus.
* Lista de arquivos removidos.
* Logs de atualização e patching.

---

## 🔄 5. Recuperação

Objetivo: retornar ao funcionamento normal de forma segura.

### Ações recomendadas

* Restaurar sistema a partir de backup íntegro.
* Monitorar continuamente o host restaurado.
* Revalidar credenciais e políticas de senha.
* Acompanhar tráfego de rede nos dias seguintes.

### Evidências coletáveis

* Logs pós-restauração.
* Relatório de integridade do sistema.

---

## 📚 6. Lições Aprendidas

Objetivo: fortalecer a segurança futura.

### Reunião pós-incidente

* O que funcionou bem?
* O que falhou?
* Como melhorar o processo?
* Que nova política deve ser implementada?

### Documentos gerados

* Relatório final do incidente.
* Atualização das políticas de segurança.
* Inclusão do incidente nos treinamentos futuros.

---

## 📝 Modelos de Comunicação

### Comunicação Interna

> "Identificamos um incidente de segurança em investigação. A máquina afetada foi isolada e não há impacto confirmado nas operações. Atualizaremos assim que possível."

### Comunicação Externa (somente quando necessário)

* Deve ser aprovada pela gestão.
* Seguir políticas legais e de compliance.

---

## 🗂️ Checklist Resumido

```
[ ] Receber alerta ou suspeita
[ ] Registrar data/hora
[ ] Coletar logs imediatos
[ ] Criar snapshot da máquina
[ ] Isolar o host afetado
[ ] Bloquear processos suspeitos
[ ] Revogar credenciais comprometidas
[ ] Identificar vetor de ataque
[ ] Remover artefatos maliciosos
[ ] Atualizar sistema e aplicar patches
[ ] Restaurar backups seguros
[ ] Monitorar pós-incidente
[ ] Registrar relatório final
```

---
