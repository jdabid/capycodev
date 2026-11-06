"""
auto_accounting.py
Automatización de facturas en PDF a hojas contables en Excel con Python.
Por Capycodev (@capycodev) - Episodio 07.

¿Por qué usar este script en vez de Claude o ChatGPT web?
- En la web tienes que subir facturas de una en una y esperar tokens.
- Este script procesa 100 facturas en 1 segundo directamente en tu computadora.
- 100% privado, sin enviar datos confidenciales a la nube y sin costo de API.
"""

import os
import re
import sys
from pathlib import Path

# Intentar importar librerías profesionales
try:
    import pdfplumber
    import pandas as pd
    LIBRERIAS_DISPONIBLES = True
except ImportError:
    LIBRERIAS_DISPONIBLES = False

CARPETA_FACTURAS = Path("./facturas")
ARCHIVO_SALIDA = Path("./contabilidad_automatica.xlsx")

def crear_facturas_de_prueba():
    """Genera datos de facturas simuladas para que el script corra de inmediato."""
    CARPETA_FACTURAS.mkdir(parents=True, exist_ok=True)
    
    facturas_demo = [
        {"archivo": "factura_001_servidor_cloud.txt", "texto": "PROVEEDOR: Cloud Services Inc.\nFECHA: 2026-11-01\nNIT: 900.123.456-7\nSUBTOTAL: $1,250.00\nIVA (19%): $237.50\nTOTAL: $1,487.50"},
        {"archivo": "factura_002_cafe_estudio.txt", "texto": "PROVEEDOR: Cafeina Dev Bar\nFECHA: 2026-11-02\nNIT: 800.987.654-3\nSUBTOTAL: $180.00\nIVA (19%): $34.20\nTOTAL: $214.20"},
        {"archivo": "factura_003_teclado_mecanico.txt", "texto": "PROVEEDOR: Hardware Tech Store\nFECHA: 2026-11-03\nNIT: 901.456.789-0\nSUBTOTAL: $450.00\nIVA (19%): $85.50\nTOTAL: $535.50"}
    ]
    
    for f in facturas_demo:
        ruta = CARPETA_FACTURAS / f["archivo"]
        if not ruta.exists():
            ruta.write_text(f["texto"], encoding="utf-8")

def procesar_factura_texto(contenido: str, nombre_archivo: str) -> dict:
    """Extrae los campos contables clave mediante expresiones regulares."""
    patron_total = re.search(r"TOTAL:?\s*\$?([\d.,]+)", contenido, re.IGNORECASE)
    patron_iva = re.search(r"IVA.*?:?\s*\$?([\d.,]+)", contenido, re.IGNORECASE)
    patron_fecha = re.search(r"FECHA:?\s*([\d\-\/]+)", contenido, re.IGNORECASE)
    patron_nit = re.search(r"NIT:?\s*([\d.\-]+)", contenido, re.IGNORECASE)
    patron_proveedor = re.search(r"PROVEEDOR:?\s*(.+)", contenido, re.IGNORECASE)

    return {
        "Archivo": nombre_archivo,
        "Proveedor": patron_proveedor.group(1).strip() if patron_proveedor else "No identificado",
        "Fecha": patron_fecha.group(1).strip() if patron_fecha else "2026-11-04",
        "NIT": patron_nit.group(1).strip() if patron_nit else "S/N",
        "IVA": float(patron_iva.group(1).replace(",", "").replace("$", "")) if patron_iva else 0.0,
        "Total": float(patron_total.group(1).replace(",", "").replace("$", "")) if patron_total else 0.0,
        "Estado": "Procesado con Éxito"
    }

def ejecutar_automatizacion():
    print("=" * 70)
    print("⚡ CAPYCODEV AUTO-ACCOUNTING: EL SUPERPODER DE PYTHON")
    print("=" * 70)

    crear_facturas_de_prueba()
    archivos = list(CARPETA_FACTURAS.iterdir())
    print(f"📁 Analizando carpeta: '{CARPETA_FACTURAS}' ({len(archivos)} documentos encontrados)...")

    registros = []

    for archivo in archivos:
        if archivo.name.startswith("."):
            continue

        texto = ""
        # 1. Si es PDF y pdfplumber está disponible
        if archivo.suffix.lower() == ".pdf" and LIBRERIAS_DISPONIBLES:
            with pdfplumber.open(archivo) as pdf:
                texto = "".join([p.extract_text() or "" for p in pdf.pages])
        else:
            # Soporte nativo para texto/txt/simulaciones
            try:
                texto = archivo.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

        if texto:
            datos = procesar_factura_texto(texto, archivo.name)
            registros.append(datos)
            print(f"  ✅ [PROCESADO] {archivo.name} -> Total: ${datos['Total']:,.2f} | IVA: ${datos['IVA']:,.2f}")

    print("\n📊 RESUMEN CONTABLE CONSOLIDADO:")
    total_acumulado = sum(r["Total"] for r in registros)
    total_iva = sum(r["IVA"] for r in registros)
    print(f"   💰 Gasto Total: ${total_acumulado:,.2f}")
    print(f"   🧾 IVA Deducible Total: ${total_iva:,.2f}")

    # Exportar a Excel si pandas está disponible, o a CSV con la librería estándar
    if LIBRERIAS_DISPONIBLES:
        df = pd.DataFrame(registros)
        df.to_excel(ARCHIVO_SALIDA, index=False)
        print(f"\n🎉 ¡Libro contable de Excel generado exitosamente en: '{ARCHIVO_SALIDA}'!")
    else:
        # Fallback estándar a CSV para que corra en cualquier máquina sin pip install
        archivo_csv = Path("./contabilidad_automatica.csv")
        with open(archivo_csv, "w", encoding="utf-8") as f:
            f.write("Archivo,Proveedor,Fecha,NIT,IVA,Total,Estado\n")
            for r in registros:
                f.write(f"{r['Archivo']},{r['Proveedor']},{r['Fecha']},{r['NIT']},{r['IVA']},{r['Total']},{r['Estado']}\n")
        print(f"\n🎉 ¡Archivo contable CSV generado en: '{archivo_csv}'!")
        print("💡 Tip: Ejecuta 'pip install -r requirements.txt' para exportar directamente a formato .xlsx")

    print("=" * 70)

if __name__ == "__main__":
    ejecutar_automatizacion()

