# 📄 Projeto OCR + Correção com Gemini

Este projeto visa extrair texto das imagens usando EasyOCR e correção do texto extraído com a inteligência do Gemini (Google AI).

Como executar o projeto:
1. Crie um ambiente Python isolado
```python
python3 -m venv {nome_projeto}
```
2. Rode o git clone 
```bash
git clone https://github.com/Atn4s/EasyOCR_LLM.git
```
3. copie os arquivos de dentro do "EasyOCR_LLM" para o seu ambiente {nome do projeto}
   
4. Ative o ambiente virtual
```bash
source {nome_projeto}/bin/activate
```
5. Instale as dependências
```python
pip install -r requirements.txt
```
6. Rode o OCR
```python
python3 EasyOCR.py
```
(Resultado: um arquivo chamado texto_extraido_ocr.txt será criado com todo o texto extraído.)

7. Configure a API do Gemini
Você precisará de uma chave da API Gemini. Pegue a sua aqui: Google Cloud Console (https://console.cloud.google.com/)

Depois, abra o arquivo LLM_Corrector_GEMINI.py e insira a chave da API neste trecho:
genai.configure(api_key="insira_sua_chave_aqui")

8. Rode a correção inteligente
```python
python3 LLM_Corrector_GEMINI.py
```
(Resultado: o arquivo texto_corrigido_gemini.txt será criado, agora com as correções aplicadas.)

Resumo do Fluxo:
Imagem → OCR (EasyOCR.py) → Texto extraído → Correção (LLM_Corrector_GEMINI.py) → Texto corrigido
