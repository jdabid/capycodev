"""
bug_demo_manual_copy_paste.py
Demostración pedagógica del 'Bug Catastrófico' de novato.

¿POR QUÉ FALLA ESTE CÓDIGO?
Muchos programadores novatos intentan extraer datos de facturas usando string.split()
asumiendo que todas las empresas formatean sus facturas de forma idéntica.
Apenas una factura usa espacios distintos, minúsculas o renglones vacíos,
el script se rompe con el clásico 'IndexError: list index out of range'.
"""

import sys
import time

def demo_bug_split_ingenuo():
    print("\n--- INICIANDO DEMO: EL ERROR DE PARSEO DE FACTURAS (Capycodev) ---")
    print("Intentando extraer el total de 3 facturas con string.split() ingenuo...\n")

    factura_normal = "Factura Nro 001\nTotal: $1,200.00"
    factura_con_formato_raro = "Factura Electrónica Nro 002\nTOTAL A PAGAR (IVA INCLUIDO) ---> 350.50"
    factura_sin_espacios = "Factura Nro 003\nTOTAL:$890.00"

    facturas = [
        ("Factura 1", factura_normal),
        ("Factura 2", factura_con_formato_raro),
        ("Factura 3", factura_sin_espacios)
    ]

    for nombre, texto in facturas:
        time.sleep(0.5)
        print(f"📄 Procesando {nombre}...")
        try:
            # ERROR DE NOVATO: asumir que siempre hay un "Total: " exacto y hacer split()[1]
            lineas = texto.split("\n")
            linea_total = [l for l in lineas if "Total:" in l][0] # ¡PUM! IndexError si dice 'TOTAL A PAGAR'
            monto = linea_total.split("Total: ")[1]
            print(f"   ✅ Extraído con éxito: {monto}")
        except IndexError as e:
            print(f"   ❌ ¡ERROR CRÍTICO! IndexError: list index out of range")
            print(f"   💥 El script se detuvo porque la factura 2 no tiene 'Total: ' exacto.")
            print(f"   💡 Solución: Usar expresiones regulares (re) y la librería pdfplumber.\n")
            break

if __name__ == "__main__":
    demo_bug_split_ingenuo()

