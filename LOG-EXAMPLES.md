# LOG-EXAMPLES.md

## Exemplos de Logs para Documentação e Análise

---

## 1. Logs de Execução de Script de Criptografia (Simulado)

```
[2025-09-12 14:22:18] INFO  - Script iniciado pelo usuário "aluno_lab".
[2025-09-12 14:22:19] INFO  - Arquivo carregado para processamento: teste1.txt
[2025-09-12 14:22:19] INFO  - Arquivo carregado para processamento: teste2.txt
[2025-09-12 14:22:20] INFO  - Criptografia concluída. Arquivos movidos para /lab/encrypted/.
[2025-09-12 14:22:20] WARN  - Chave de teste gerada automaticamente (não utilizar em produção).
[2025-09-12 14:22:21] INFO  - Script finalizado com sucesso.
```

---

## 2. Logs de Captura de Eventos do Teclado (Simulação Inofensiva)

```
[2025-09-12 15:03:11] INFO  - Módulo de captura iniciado.
[2025-09-12 15:03:12] DEBUG - Tecla registrada: T
[2025-09-12 15:03:12] DEBUG - Tecla registrada: E
[2025-09-12 15:03:13] DEBUG - Tecla registrada: S
[2025-09-12 15:03:13] DEBUG - Tecla registrada: T
[2025-09-12 15:03:14] INFO  - Buffer salvo em /lab/logs/key_events.log
[2025-09-12 15:03:16] INFO  - Módulo encerrado pelo usuário.
```

---

## 3. Logs de Envio Simulado por E-mail

*(Somente demonstrativo — não envia nada)*

```
[2025-09-12 15:10:52] INFO  - Iniciando rotina de envio.
[2025-09-12 15:10:52] INFO  - Autenticando no servidor SMTP fictício.
[2025-09-12 15:10:53] INFO  - Arquivo anexado: key_events.log (4 KB)
[2025-09-12 15:10:53] INFO  - Mensagem enviada com sucesso para professor@exemplo.com
[2025-09-12 15:10:54] INFO  - Rotina concluída.
```

---

## 4. Logs de Firewall (Exemplo Educacional)

```
[2025-09-12 16:44:01] ALERT - Tentativa de conexão bloqueada: origem 192.168.0.45 destino 192.168.0.10:445
[2025-09-12 16:44:05] INFO  - Regra aplicada: BLOQUEAR SMB EM REDE LAB
[2025-09-12 16:44:10] INFO  - Tráfego HTTPS permitido para 8.8.8.8
```

---

## 5. Logs de Sandbox/VM

```
[2025-09-12 17:02:55] INFO  - Snapshot "pre_teste" restaurado.
[2025-09-12 17:03:02] INFO  - Script isolado iniciado no diretório /sandbox/safe_scripts/.
[2025-09-12 17:03:10] WARN  - Processamento elevado detectado: CPU 89%.
[2025-09-12 17:03:14] INFO  - Execução concluída. Nenhuma modificação crítica detectada.
```

---

## 6. Logs de SIEM (Modelo Didático)

```
2025-09-12T18:22:01Z EVENT: file_access
  user=aluno_lab
  path=/lab/encrypted/teste1.txt
  action=read
  result=success

2025-09-12T18:22:05Z EVENT: script_execution
  script=decrypt_demo.py
  privileges=user
  result=success
```

---
