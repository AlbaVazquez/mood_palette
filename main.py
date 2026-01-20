from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

#Usaré el modelo Zero-Shot, un modelo capaz de realizar tareas o reconocer
#categorías sin haber sido entrenado específicamente para ellas.
#Lo cuál lo hace perfecto como clasificador.
clasificador_ia = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

#Lista de emociones y diccionario que le asigna un color a cada emoción
LISTA_EMOCIONES = [
    "alegría", "tristeza", "ira", "miedo", "amor", "sorpresa", 
    "nostalgia", "misterio", "esperanza", "confusión", "euforia", "calma"
]

COLORES = {
    "alegría": "#FFD700", "tristeza": "#4682B4", "ira": "#FF4500",
    "miedo": "#483D8B", "amor": "#FF69B4", "sorpresa": "#00CED1",
    "nostalgia": "#D8BFD8", "misterio": "#2F4F4F", "esperanza": "#90EE90",
    "confusión": "#BC8F8F", "euforia": "#FF00FF", "calma": "#E0FFFF"
}

class Entrada(BaseModel):
    texto:str

#Petición GET 
@app.get("/")
def home():
    return FileResponse('static/index.html')

#Petición POST
@app.post("/analizar")
def analizar(entrada: Entrada):
    #Aquí es donde la IA analiza el texto pasado como entrada
    resultado = clasificador_ia(entrada.texto, candidate_labels=LISTA_EMOCIONES, multi_label=False)
    
    #Filtrará solo las emociones que tengan más de un 15% de probabilidad
    emociones_detectadas = []
    for i in range(len(resultado['labels'])):
        score = resultado['scores'][i]
        label = resultado['labels'][i]
        
        if score > 0.05:
            emociones_detectadas.append({
                "nombre": label,
                "color": COLORES.get(label, "#D3D3D3"),
                "fuerza": f'{int(score * 100)}%'
            })

    return emociones_detectadas[:6]

app.mount("/static", StaticFiles(directory="static"), name="static")
