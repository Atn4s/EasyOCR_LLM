# 📄 Projeto OCR + Correção com Gemini

Este projeto visa extrair texto das imagens usando EasyOCR e correção do texto extraído com a inteligência do Gemini (Google AI).

Como executar o projeto:

1. Realize um git clone do projeto: 
```bash
git clone https://github.com/Atn4s/EasyOCR_LLM.git
```

2. Crie um ambiente Python isolado para ser utilizado:
```python
python3 -m venv {nome_projeto}
```

3. copie os arquivos do diretório do "EasyOCR_LLM" para o seu ambiente {nome do projeto}.
   
4. Ative o ambiente virtual:
```bash
source {nome_projeto}/bin/activate
```
5. Instale as dependências:
```python
pip install -r requirements.txt
```
6. O EasyOCR pode ser executado de 2 formas: passando a imagem direto para o programa <br>
```python
python3 EasyOCR.py /caminho/imagem.jpg
```
ou com o EasyGUI para seleção de imagem: 
```python
python3 EasyOCR.py
```
(Resultado: um arquivo chamado texto_extraido_ocr.txt será criado com todo o texto extraído.)

7. Configure a API do Gemini
Você precisará de uma chave da API Gemini. Pegue a sua aqui: Google Cloud Console (https://console.cloud.google.com/)

8. Crie um .env com o texto: GEMINI_API_KEY="insira_sua_chave_aqui"

9. Rode a correção inteligente
```python
python3 LLM_Corrector_GEMINI.py
```
(Resultado: o arquivo texto_corrigido_gemini.txt será criado, agora com as correções aplicadas.)

Resumo do Fluxo:
Imagem → OCR (EasyOCR.py) → Texto extraído → Correção (LLM_Corrector_GEMINI.py) → Texto corrigido