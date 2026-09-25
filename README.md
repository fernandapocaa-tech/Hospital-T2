# Tarea 2 — Estructuras de decisión: Expedientes Digitales (Hospital de Diagnóstico)

**Socio Formador:** Hospital de Diagnóstico
**Integrantes:**
- [Fernanda Pocasangre] — usuario de GitHub: fernandapocaa-tech
- [Alejandra Palma] — usuario de GitHub: alepal1

## Objetivo

Traducir la lógica de decisión diseñada en la Semana 6 (pseudocódigo) a código
real usando sentencias `if/elif/else`, aplicada al reto de Expedientes
Digitales del Hospital de Diagnóstico: evaluar el estado de un expediente
según el checklist de documentos correspondiente al perfil del empleado.

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

```
GET /expediente/<nombreEmpleado>/<documentosSubidos>
GET /expediente/<nombreEmpleado>/<documentosSubidos>/<perfil>
```

El checklist de documentos requeridos varía según el perfil del empleado
(administrativo, médico, enfermería), según lo indicado en la ficha del reto.
Si no se especifica un perfil, se usa un checklist por defecto.

## Ejemplos de prueba

- `/expediente/Ana/0` → estado "sin iniciar"
- `/expediente/Carlos/3/medico` → estado "incompleto"
- `/expediente/Maria/4/administrativo` → estado "completo"

*(El documento de requerimientos con el levantamiento de la lógica de decisión
y las capturas de las pruebas se entregan por separado en Word.)*
