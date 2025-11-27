# safe_demos.py
"""
Coleção de scripts SEGUROS para demonstração acadêmica.
Nenhum código aqui realiza criptografia real, captura de teclado,
transmissão de dados ou qualquer ação maliciosa.
Os scripts apenas simulam comportamentos para fins pedagógicos.
"""

import base64
import time
import random
from datetime import datetime

# ------------------------------------------------------------
# 1. Simulação de "criptografia" usando Base64 (didático e reversível)
# ------------------------------------------------------------

def simulate_encrypt(text: str) -> str:
    """
    Simula um processo de criptografia usando Base64.
    NÃO é criptografia real — apenas codificação.
    """
    encoded = base64.b64encode(text.encode()).decode()
    return encoded


def simulate_decrypt(encoded_text: str) -> str:
    """
    Simula um processo de descriptografia Base64.
    """
    try:
        decoded = base64.b64decode(encoded_text.encode()).decode()
        return decoded
    except Exception:
        return "[ERRO] Texto inválido para decodificação."


# ------------------------------------------------------------
# 2. Simulador de geração de "logs de teclas" (NÃO captura teclado)
# ------------------------------------------------------------

def generate_fake_keylogs(output_file="fake_keylog.txt", length=30):
    """
    Gera um arquivo contendo uma sequência aleatória de caracteres,
    simulando um log, sem capturar qualquer tecla real.
    """
    fake_keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# LOG DE TECLAS FICTÍCIO - SEM CAPTURA REAL\n")
        for _ in range(length):
            time.sleep(0.01)  # apenas simula tempo de captura
            key = random.choice(fake_keys)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] KEY: {key}\n")
    return output_file


# ------------------------------------------------------------
# 3. Simulação de envio de relatório (não envia nada)
# ------------------------------------------------------------

def simulate_email_send(log_file: str):
    """
    Simula o processo de envio, mas NÃO realiza envio real.
    Apenas imprime feedback no console.
    """
    print("Simulando envio de arquivo...")
    time.sleep(1)
    print(f"Arquivo '{log_file}' registrado para envio fictício.")
    time.sleep(1)
    print("Envio concluído (simulação).")


# ------------------------------------------------------------
# 4. Execução demonstrativa
# ------------------------------------------------------------

if __name__ == "__main__":
    print("===== SIMULADOR SEGURO DE DEMONSTRAÇÕES =====")

    # Demonstração 1: "Criptografia"
    sample_text = "Texto de teste para simulação."
    encrypted = simulate_encrypt(sample_text)
    decrypted = simulate_decrypt(encrypted)

    print("\n--- Simulação de Criptografia Base64 ---")
    print("Texto original:", sample_text)
    print("Codificado:", encrypted)
    print("Decodificado:", decrypted)

    # Demonstração 2: Keylog fictício
    print("\n--- Gerando logs fictícios ---")
    logfile = generate_fake_keylogs()
    print("Arquivo gerado:", logfile)

    # Demonstração 3: Envio simulado
    print("\n--- Envio fictício de relatório ---")
    simulate_email_send(logfile)

    print("\nTodas as simulações foram concluídas com segurança.")
