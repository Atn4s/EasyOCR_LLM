import os
import sys
import easyocr
import cv2
import numpy as np
import easygui
from PIL import Image, ImageDraw, ImageFont
from matplotlib import pyplot as plt

# === Caminho para iniciar o EasyGUI ===
load_path = "/home/joao/Downloads/IMAGENS_OCR"

# === Abrir imagem via caixa de seleção ou linha de comando ===
try:
    img_path = sys.argv[1] if len(sys.argv) > 1 else easygui.fileopenbox(default=f"{load_path}/*")
except:
    print("Erro ao abrir a imagem. Verifique se o caminho está correto ou selecione uma imagem via caixa de diálogo.")
    exit()

# === Nome base do arquivo ===
img_name = os.path.basename(img_path)

# === Inicializa o leitor EasyOCR para português ===
try:
    reader = easyocr.Reader(['pt', 'en'])
    result = reader.readtext(img_path)
except Exception as e:
    print(f"Erro ao inicializar o EasyOCR: {e}")
    exit()

# === Lê a imagem com OpenCV ===
img = cv2.imread(img_path)

# === Junta todos os textos detectados ===
texto_bruto = "\n".join([detection[1] for detection in result])

# === Salvar o texto bruto (OCR) ===
with open('texto_extraido_ocr.txt', 'w', encoding='utf-8') as file:
    file.write(texto_bruto)

# === Converte a imagem OpenCV (BGR) para Pillow (RGB) ===
img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# === Carrega a fonte ABNT-2 ===
font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' # Substitua pelo caminho correto para a fonte ABNT-2
font = ImageFont.truetype(font_path, 20)  # Ajuste o tamanho da fonte conforme necessário

# === Cria um objeto de desenho para adicionar o texto ===
draw = ImageDraw.Draw(img_pil)

# === Redesenha na imagem original com a fonte ABNT-2 ===
for detection in result:
    top_left = tuple(map(int, detection[0][0]))
    text = detection[1]
    
    # Desenha um retângulo para destacar o texto
    cv2.rectangle(img, top_left, tuple(map(int, detection[0][2])), (0, 255, 0), 2)  
    
    # Usa o Pillow para adicionar o texto com a fonte personalizada
    draw.text((top_left[0], top_left[1] - 30), text, font=font, fill=(255, 0, 0))

# === Converte novamente para formato OpenCV (BGR) para exibição ===
img_final = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

# === Mostra a imagem com as detecções ===
plt.figure(figsize=(12, 16))  # Tamanho maior para melhor visualização  
plt.imshow(cv2.cvtColor(img_final, cv2.COLOR_BGR2RGB))
plt.title(f"OCR: {img_name}")
plt.axis('off')
plt.show()

print("[+] Texto extraído salvo em: texto_extraido_ocr.txt")
print(texto_bruto)