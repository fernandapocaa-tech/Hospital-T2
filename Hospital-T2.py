#Hospital-T2.py

from flask import Flask, jsonify

app = Flask(__name__)

# Documentos requeridos segun el checklist del perfil del empleado.
# Ajusta estos numeros si tu ficha indica que el checklist varia por perfil
# (por ejemplo: medico=6, administrativo=4). Si es un numero fijo para todos,
# puedes dejar solo DOCUMENTOS_REQUERIDOS y quitar el diccionario.
# Checklist confirmado con RRHH del Hospital de Diagnostico segun ficha del reto
Baja hasta el final de la página, en el mensaje del commit escribe algo como "Agrego comentario de validacion del checklist"
DOCUMENTOS_REQUERIDOS = 5


@app.route("/expediente/<nombreEmpleado>/<int:documentosSubidos>")
def evaluarExpediente(nombreEmpleado, documentosSubidos):
    """
    Recibe un expediente por la ruta (nombre del empleado y cantidad de
    documentos subidos) y retorna su estado segun el checklist.
    """
    # Caso por defecto: dato invalido (no deberia haber documentos negativos)
    if documentosSubidos < 0:
        estado = "dato invalido"
    elif documentosSubidos == 0:
        estado = "sin iniciar"
    elif documentosSubidos < DOCUMENTOS_REQUERIDOS:
        estado = "incompleto"
    else: 
        estado = "completo"

    return jsonify({
        "empleado": nombreEmpleado,
        "documentosSubidos": documentosSubidos,
        "documentosRequeridos": DOCUMENTOS_REQUERIDOS,
        "estado": estado
    })


if __name__ == "__main__":
    app.run(debug=True)
