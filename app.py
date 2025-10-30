
<# app.py
import gradio as gr
import joblib
import numpy as np

# Carregar modelos salvos
preprocessor = joblib.load("model/preprocessor.joblib")
model = joblib.load("model/xgb_model.joblib")

# Função de previsão
def predict_price(area, quartos, banheiros, idade, localizacao):
    # Criar array de entrada
    X = np.array([[area, quartos, banheiros, idade, localizacao]])
    # Aplicar pré-processamento
    X_trans = preprocessor.transform(X)
    # Previsão
    pred = model.predict(X_trans)[0]
    return round(pred, 2)

# Interface Gradio
demo = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Área (m²)"),
        gr.Number(label="Quartos"),
        gr.Number(label="Banheiros"),
        gr.Number(label="Idade do imóvel (anos)"),
        gr.Number(label="Localização (código ou bairro)")  # Se tiver categórica, usar encoding numérico
    ],
    outputs=gr.Number(label="Preço Previsto (R$)"),
    title="Previsor de Preço de Imóveis",
    description="Informe os dados do imóvel e obtenha o preço estimado."
)

if __name__ == "__main__":
    demo.launch()
>
