import easyocr
import cv2
import numpy as np
import easygui
from PIL import Image, ImageDraw, ImageFont
from matplotlib import pyplot as plt

# === Abrir imagem via caixa de seleção ===
img_path = easygui.fileopenbox()

# === Inicializa o leitor EasyOCR para português ===
reader = easyocr.Reader(['pt', 'en'])
result = reader.readtext(img_path)

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
font = ImageFont.truetype(font_path, 30)  # Ajuste o tamanho da fonte conforme necessário

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
plt.imshow(cv2.cvtColor(img_final, cv2.COLOR_BGR2RGB))

plt.axis('off')
plt.title("Texto detectado")
plt.show()

print("[+] Texto extraído salvo em: texto_extraido_ocr.txt")
