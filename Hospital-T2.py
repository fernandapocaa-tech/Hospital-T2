#Hospital-T2
from flask import Flask, render_template, request
import unicodedata

app = Flask(__name__)

DOCUMENTOS_PERFIL = {
    "administrativo": ["DUI", "Título", "Antecedentes Penal", "Solvencia PNP"],
    "medico": ["DUI", "Título", "Antecedentes Penal", "Solvencia PNP", "Colegiatura médica", "Especialidad"],
    "enfermeria": ["DUI", "Título", "Antecedentes Penal", "Solvencia PNP", "Junta de Vigilancia"]
}

TODOS_DOCUMENTOS = ["DUI", "Título", "Antecedentes Penal", "Solvencia PNP", "Colegiatura médica", "Especialidad", "Junta de Vigilancia"]

EMPLEADOS_DB = [
    {"nombre": "Ana", "perfil": "administrativo", "docs": ["DUI", "Título", "Antecedentes Penal", "Solvencia PNP"]},
    {"nombre": "Carlos", "perfil": "medico", "docs": ["DUI", "Título", "Antecedentes Penal", "Colegiatura médica"]},
    {"nombre": "Maria", "perfil": "enfermeria", "docs": ["DUI", "Título", "Antecedentes Penal", "Solvencia PNP", "Junta de Vigilancia"]}
]


def slug(texto):
    texto = texto.lower().replace(" ", "_")
    texto = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in texto if not unicodedata.combining(c))
    
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


  if __name__ == '__main__':
    app.run(debug=True)
