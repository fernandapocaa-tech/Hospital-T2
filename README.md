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

---

## 1. El checklist por perfil

```python
DOCUMENTOS_PERFIL = {
    "administrativo": ["DUI", "Título", "Antecedentes Penal", "Solvencia PNP"],
    "medico": ["DUI", "Título", "Antecedentes Penal", "Solvencia PNP", "Colegiatura médica", "Especialidad"],
    "enfermeria": ["DUI", "Título", "Antecedentes Penal", "Solvencia PNP", "Junta de Vigilancia"]
}
```

Este diccionario guarda, para cada perfil de empleado, la lista de documentos
que le exige su checklist. Esto refleja una regla de negocio confirmada en
la ficha del reto: el checklist no es el mismo para todos, varía según si el
empleado es administrativo, médico o de enfermería.

---

## 2. La lista de empleados

```python
EMPLEADOS_DB = [
    {"nombre": "Ana", "perfil": "administrativo", "docs": ["DUI", "Título", "Antecedentes Penal", "Solvencia PNP"]},
    {"nombre": "Carlos", "perfil": "medico", "docs": ["DUI", "Título", "Antecedentes Penal", "Colegiatura médica"]},
    {"nombre": "Maria", "perfil": "enfermeria", "docs": ["DUI", "Título", "Antecedentes Penal", "Solvencia PNP", "Junta de Vigilancia"]}
]
```

Cada empleado es un diccionario con su nombre, su perfil, y la lista de
documentos que YA entregó. Esta lista (`docs`) se compara más adelante
contra el checklist de su perfil para saber qué le falta.

---

## 3. La función slug

```python
def slug(texto):
    texto = texto.lower().replace(" ", "_")
    texto = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in texto if not unicodedata.combining(c))
```

Convierte un texto a una forma simple para usarlo como nombre de parámetro
en la URL: minúsculas, sin espacios, sin acentos. Por ejemplo,
`"Colegiatura médica"` se convierte en `"colegiatura_medica"`. Esto permite
armar nombres de parámetro válidos para la URL a partir de nombres que sí
tienen espacios y acentos.

---

## 4. La ruta y la lógica de decisión

```python
@app.route('/expedientes')
def mostrar_expedientes():
    matriz_empleados = []

    for emp in EMPLEADOS_DB:
        docs_requeridos = DOCUMENTOS_PERFIL.get(emp["perfil"], [])
        estado_docs = {}

        for doc in TODOS_DOCUMENTOS:
            if doc not in docs_requeridos:
                estado_docs[doc] = "No aplica"
                continue

            entregado = doc in emp["docs"]

            parametro = slug(emp["nombre"]) + "_" + slug(doc)
            valor_url = request.args.get(parametro)
            if valor_url == "si":
                entregado = True
            elif valor_url == "no":
                entregado = False

            estado_docs[doc] = "Completo" if entregado else "Pendiente"

        matriz_empleados.append({
            "nombre": emp["nombre"],
            "perfil": emp["perfil"],
            "estados": estado_docs
        })

    return render_template('expedientes.html', empleados=matriz_empleados, documentos=TODOS_DOCUMENTOS)
```

Aquí está el corazón de la lógica de decisión, con un bucle dentro de otro
bucle:

- El **bucle de afuera** (`for emp in EMPLEADOS_DB`) recorre cada empleado.
- El **bucle de adentro** (`for doc in TODOS_DOCUMENTOS`) recorre, para ese
  empleado, cada documento posible de la tabla.

Por cada documento, la decisión es exactamente if/elif/else:

1. **Si el documento no está en el checklist de su perfil** → el estado es
   `"No aplica"`, y se pasa al siguiente documento con `continue`.
2. **Si el documento sí aplica**, se revisa si ya lo entregó (comparando
   contra su lista `docs`), y la URL puede cambiar ese valor con un
   parámetro como `?carlos_colegiatura_medica=no`.
3. Según si lo entregó o no, el estado queda en `"Completo"` o `"Pendiente"`.

---

## 5. La plantilla HTML (con Jinja)

```html
{% for emp in empleados %}
<tr>
  <td>{{ emp.nombre }}</td>
  <td><span class="badge badge-{{ emp.perfil }}">{{ emp.perfil }}</span></td>
  {% for doc in documentos %}
    {% set estado = emp.estados[doc] %}
    {% if estado == "Completo" %}
    <td class="ok">Completo</td>
    {% elif estado == "Pendiente" %}
    <td class="pendiente">Pendiente</td>
    {% else %}
    <td class="no-aplica">No aplica</td>
    {% endif %}
  {% endfor %}
</tr>
{% endfor %}
```

La plantilla recibe la matriz ya calculada desde Python (`empleados` y
`documentos`) y solo se encarga de **dibujarla**: no calcula nada, solo
decide qué clase de CSS ponerle a cada celda según el estado que ya le
llegó listo. Por eso la lógica de decisión real vive en `Hospital-T2.py`,
no aquí.

---

## 6. El CSS (static/style.css)

El CSS no calcula nada: solo le da color a las clases que la plantilla ya
puso. Por ejemplo, la clase `.ok` se pinta de verde, `.pendiente` de rojo, y
`.no-aplica` de gris:

```css
.ok { background: #e9f9ee; color: #1a7a34; font-weight: bold; }
.pendiente { background: #fdecec; color: #b3261e; font-weight: bold; }
.no-aplica { background: #f2f2f2; color: #8a8f98; font-style: italic; }
```

---

## Cómo ejecutar el proyecto

```bash
pip install flask
python Hospital-T2.py
```

El servidor corre en `http://127.0.0.1:5000/`, y la tabla se ve en:

```
http://127.0.0.1:5000/expedientes
```

## Parámetros por URL

Cada casilla se puede cambiar sin tocar el código, por ejemplo:

```
http://127.0.0.1:5000/expedientes?carlos_colegiatura_medica=no
http://127.0.0.1:5000/expedientes?ana_dui=no
```

## Checklist de documentos por perfil

| Perfil | Documentos requeridos |
|---|---|
| Administrativo | DUI, Título, Antecedentes Penal, Solvencia PNP |
| Médico | DUI, Título, Antecedentes Penal, Solvencia PNP, Colegiatura médica, Especialidad |
| Enfermería | DUI, Título, Antecedentes Penal, Solvencia PNP, Junta de Vigilancia |

## Cierre: lo que aplicamos en este proyecto

| Habilidad | Dónde se aplicó |
|---|---|
| Estructuras de decisión if/elif/else | Para decidir el estado de cada documento (Completo, Pendiente, No aplica) |
| Datos de dos dimensiones | EMPLEADOS_DB guarda varios empleados, cada uno con su propia lista de documentos |
| Bucles anidados | El bucle de afuera recorre empleados, el de adentro recorre documentos |
| Separar la lógica de la página | Hospital-T2.py calcula, expedientes.html dibuja, style.css da estilo |
| Parámetros en la URL | Cada casilla se puede cambiar desde la URL sin tocar el código |

## Capturas de pantalla

(Ver imágenes en la carpeta /capturas de este repositorio.)

(El documento con el levantamiento completo de la lógica de decisión
se entrega por separado en Word.)
