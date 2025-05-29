import openai

# Clave API de OpenAI
openai.api_key = "TU_API_KEY"

# Tema elegido
tema = "Embudo de conversión en marketing digital"

# Prompt estructurado
prompt = f"""
Actuá como un tutor personal de aprendizaje para profesionales con poco tiempo disponible.
A partir del siguiente tema, generá un entrenamiento express que incluya:
1) un resumen en lenguaje claro,
2) tres ideas clave,
3) cinco preguntas tipo quiz de opción múltiple,
4) una mini guía de aplicación práctica en el trabajo.

Tema: {tema}
Tiempo estimado de lectura: 10 minutos.
"""

# Llamado al modelo GPT
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Sos un experto en educación y aprendizaje exprés para profesionales."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=1000
)

# Mostrar la respuesta
print(response["choices"][0]["message"]["content"])
