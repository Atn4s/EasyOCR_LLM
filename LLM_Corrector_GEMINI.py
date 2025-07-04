import google.generativeai as genai
import os
from dotenv import load_dotenv

# === CONFIGURAR A CHAVE DA API DO GEMINI === 
# Para funcionar com o código abaixo, crie um arquivo .env com a variável: GEMINI_API_KEY="sua_chave_aqui"
load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# === Função para corrigir texto com Gemini ===
def corrigir_texto(texto_original):
    model = genai.GenerativeModel('models/gemini-2.0-flash')
    prompt = (
        f"Corrija ortografia e gramática do seguinte texto em português:\n\n\"{texto_original}\""
    )
    resposta = model.generate_content(prompt)
    return resposta.text

# === Ler arquivo OCR ===
with open('texto_extraido_ocr.txt', 'r', encoding='utf-8') as file:
    texto_original = file.read()

# === Corrigir o texto com Gemini ===
texto_corrigido = corrigir_texto(texto_original)

# === Salvar o texto corrigido ===
with open('texto_corrigido_gemini.txt', 'w', encoding='utf-8') as file:
    file.write(texto_corrigido)

# === Mostra o texto corrigido no console ===
print("\n--- Texto Corrigido via API - Gemini 2.0 - Flash ---\n")
print(texto_corrigido)
