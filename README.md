# Hospital-T2
# Tarea 2 — Estructuras de decisión: Expedientes Digitales (Hospital de Diagnóstico)

**Socio Formador:** Hospital de Diagnóstico
**Integrantes:**
- [Tu nombre] — usuario de GitHub: fernandapocaa-tech
- [Nombre de tu compañera] — usuario de GitHub: [su usuario]

## Objetivo

Traducir la lógica de decisión diseñada en la Semana 6 (pseudocódigo) a código real usando sentencias `if/elif/else`, aplicada al reto de Expedientes Digitales del Hospital de Diagnóstico: evaluar el estado de un expediente según el checklist de documentos correspondiente al perfil del empleado.

## Paso previo: Levantamiento de requerimientos de la lógica de decisión

**1. ¿Cuáles son los estados posibles reales del dato que vamos a evaluar?**
- Sin iniciar
- Incompleto
- Completo

**2. ¿Qué valor o condición de la ficha define cada estado?**
El número de documentos subidos por el empleado, comparado contra el total de documentos requeridos por el checklist (5 documentos).
- 0 documentos subidos → *sin iniciar*
- Más de 0 pero menos de 5 → *incompleto*
- 5 o más → *completo*

**3. ¿Hay reglas de negocio confirmadas en la ficha que aún no estén reflejadas en la lógica de la Semana 6?**
[Completa aquí si tu ficha menciona algo adicional, o escribe "No, el checklist es el mismo para todos los perfiles."]

**4. ¿Qué pasa si el dato no encaja en ningún estado esperado? (caso por defecto)**
Si la cantidad de documentos subidos es un número negativo, el sistema retorna el estado *"dato inválido"*.

## Tecnología
- Python 3
- Flask

## Cómo ejecutar el proyecto

```bash
pip install flask
python Hospital-T2.py
```

El servidor corre en `http://127.0.0.1:5000/`.

## Endpoint
