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
    
