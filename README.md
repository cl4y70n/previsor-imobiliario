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

