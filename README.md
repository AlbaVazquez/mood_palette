HE USADO bart-large-mnli, UN MODELO PLN DE FACEBOOK QUE SE DESTACA EN LA CLASIFICACIÓN DE TEXTO DE "zero-shot".

La dinámica de la aplicación es extraer las emociones detectadas en un texto introducido. Las mostrará con su respectivo color y repartidas en porcentajes que reflejan qué tanto predomina dicha emoción.

**_NO FUNCIONA CON LIVE SERVER_**

**Levantar la app:**
Para crear el entorno virtual: **python3 -m venv env**

Para entrar al entorno virtual: **source env/bin/activate**

Para descargar los requisitos (solo en caso de no contar con ellos): **pip install -r requirements.txt**

Utilizar el siguiente comando en la terminal para levantar la app: **uvicorn main:app --reload**

Una vez activa, busca en tu navegador: **http://127.0.0.1:8000/**