# Tarea 2 — Estructuras de decisión: Expedientes Digitales (Hospital de Diagnóstico)

**Socio Formador:** Hospital de Diagnóstico
**Integrantes:**
- Fernanda Pocasangre — usuario de GitHub: fernandapocaa-tech
- Alejandra Palma — usuario de GitHub: alepal1

## Qué hace este proyecto

Muestra, en una página web con tabla y colores, el estado de los expedientes
digitales del personal del Hospital de Diagnóstico: por cada empleado y cada
documento, dice si ese documento está Completo, Pendiente, o si No aplica a
su perfil.

## Cómo están guardados los datos

Los documentos entregados de cada empleado se guardan en un diccionario
dentro de una lista (EMPLEADOS_DB), donde cada empleado tiene su nombre, su
perfil, y la lista de documentos que ya entregó. Es la misma idea de "datos
de dos dimensiones" vista en clase (como una matriz), solo que en vez de
True/False por cada casilla, aquí se guarda directamente la lista de los
documentos que sí entregó.

## Cómo funciona la lógica de decisión

Por cada empleado, el programa recorre la lista completa de documentos
posibles (TODOS_DOCUMENTOS) y decide el estado de cada uno con if/elif/else:

1. Si el documento no está en la lista de documentos requeridos para el
   perfil de ese empleado -> el estado es "No aplica".
2. Si el documento sí aplica, se revisa si el empleado ya lo entregó
   (comparando contra su lista de documentos entregados, o contra lo que
   venga en la URL).
3. Si no lo ha entregado -> "Pendiente". Si ya lo entregó -> "Completo".

Esto es exactamente un bucle dentro de otro bucle: el de afuera recorre cada
empleado, y el de adentro recorre cada documento posible para ese empleado.

## Cómo funcionan los parámetros por URL

Igual que en el material de la semana, cada casilla de la tabla se puede
cambiar sin tocar el código, usando un parámetro con el nombre del empleado
y el documento pegados con guión bajo, por ejemplo:

- /expedientes?carlos_colegiatura_medica=no
- /expedientes?ana_dui=no

Si el nombre del parámetro no coincide con ningún empleado o documento real,
Flask simplemente lo ignora y la casilla conserva su valor original.

## Cómo está separado el proyecto

Siguiendo la separación de responsabilidades de Flask (Python calcula, HTML
dibuja, CSS da estilo), el proyecto queda dividido así:

| Archivo | Lenguaje | Su trabajo |
|---|---|---|
| Hospital-T2.py | Python | Calcula el estado de cada documento (la logica de decision) |
| templates/expedientes.html | HTML + Jinja | Dibuja la tabla con los datos ya calculados |
| static/style.css | CSS | Da el estilo y los colores a la tabla |

## Checklist de documentos por perfil

| Perfil | Documentos requeridos |
|---|---|
| Administrativo | DUI, Título, Antecedentes Penal, Solvencia PNP |
| Médico | DUI, Título, Antecedentes Penal, Solvencia PNP, Colegiatura médica, Especialidad |
| Enfermería | DUI, Título, Antecedentes Penal, Solvencia PNP, Junta de Vigilancia |

## Tecnología

- Python 3
- Flask

## Cómo ejecutar el proyecto

Instala Flask con: pip install flask

Luego ejecuta: python Hospital-T2.py

El servidor corre en http://127.0.0.1:5000/, y la tabla se ve en
http://127.0.0.1:5000/expedientes

## Cierre: lo que aplicamos en este proyecto

| Habilidad | Dónde se aplicó |
|---|---|
| Estructuras de decisión if/elif/else | Para decidir el estado de cada documento (Completo, Pendiente, No aplica) |
| Datos de dos dimensiones | EMPLEADOS_DB guarda varios empleados, cada uno con su propia lista de documentos |
| Separar la lógica de la página | Hospital-T2.py calcula, expedientes.html dibuja, style.css da estilo |
| Parámetros en la URL | Cada casilla se puede cambiar desde la URL sin tocar el código |

## Capturas de pantalla

(Ver imágenes en la carpeta /capturas de este repositorio.)

(El documento con el levantamiento de la lógica de decisión (paso previo)
se entrega por separado en Word.)
