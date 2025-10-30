# Previsor Imobiliário Inteligente 🏠💻

## Visão Geral

O **Previsor Imobiliário Inteligente** é um sistema de previsão de preços de imóveis usando Machine Learning, com foco em praticidade, precisão e deploy rápido.  
Ele utiliza o algoritmo **XGBoost** para regressão, integrado com pipelines do **scikit-learn**, e inclui monitoramento de métricas via **MLflow**.  
O projeto conta com um aplicativo de interface web em **Gradio**, que pode ser facilmente adaptado para **Hugging Face Spaces**.

---

## Funcionalidades

- Carregamento de dataset público de imóveis (tabular).  
- Pré-processamento completo: imputação, encoding de variáveis categóricas e scaling de features.  
- Engenharia de features: por exemplo, idade do imóvel e densidade por área.  
- Treinamento com **XGBoost**, incluindo early stopping.  
- Monitoramento de métricas no **MLflow**: RMSE, MAE, R².  
- Salvamento do modelo: `joblib` e formato nativo XGBoost (`.xgb`).  
- Gráfico de importância das features e comparação de previsões vs valores reais.  
- Interface Gradio para inferência em tempo real.  

---

## Estrutura do Projeto

```

previsor-imobiliario/
│
├── app.py                     # Interface Gradio
├── requirements.txt           # Dependências do projeto
├── model/
│   ├── preprocessor.joblib    # Pipeline de pré-processamento
│   └── xgb_model.joblib       # Modelo XGBoost treinado
├── mlruns/                    # Experimentos e logs do MLflow
├── feature_importance.png     # Artefato gerado pelo MLflow
├── predicoes_vs_reais.png     # Artefato gerado pelo MLflow
└── sample_data/               # Arquivos de exemplo para teste

````

---

## Instalação e Execução no Colab

1. Clone este repositório:

```bash
!git clone https://github.com/cl4y70n/previsor-imobiliario.git
%cd previsor-imobiliario
````

2. Instale dependências:

```bash
!pip install -r requirements.txt
```

3. Execute o notebook ou scripts de treino:

```bash
# Exemplo: iniciar notebook
%run colab_previsor_imoveis.ipynb
```

4. Após o treino, você terá os modelos salvos em `model/` e gráficos de monitoramento em `feature_importance.png` e `predicoes_vs_reais.png`.

---

## MLflow UI no Colab

Para visualizar os logs do MLflow localmente:

```bash
from pyngrok import ngrok
!mlflow ui --port 5000 &

url = ngrok.connect(5000)
print(f"MLflow UI disponível em: {url}")
```

> ⚠️ Lembre-se: é necessário um token ngrok se estiver expondo para fora do Colab.

---

## Deploy no Hugging Face Spaces

1. Crie um Space em [https://huggingface.co/spaces/](https://huggingface.co/spaces/)

   * Escolha **Gradio** como SDK.
2. Faça upload do projeto ou use Git:

```bash
git remote add hf https://huggingface.co/spaces/Ad0N41/previsor-imobiliario
git push hf main
```

3. Certifique-se que `app.py` está na raiz e `model/` contém os arquivos `.joblib`.
4. O Space carregará a interface Gradio automaticamente.

---

## Configuração de AWS S3 (Opcional)

Para salvar modelos e artefatos no S3:

```python
import boto3
import os

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    s3.upload_file("model/xgb_model.joblib", S3_BUCKET_NAME, "xgb_model.joblib")
```

---

## GitHub Commit & Push

```bash
git add .
git commit -m "Primeiro commit completo do projeto"
git branch -M main
git push -u origin main
```

---

## Tecnologias

* Python 3.10+
* XGBoost
* scikit-learn
* pandas / numpy
* MLflow
* Gradio
* Matplotlib / Seaborn
* Hugging Face Spaces (opcional)
* Boto3 (AWS S3, opcional)

---

## Contato

**Clayton Ramos**
Email: [claytonramos334@gmail.com](mailto:claytonramos334@gmail.com)

---
