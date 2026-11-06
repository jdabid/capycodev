# ⚡ Capy Auto-Accounting: Facturas PDF a Excel en Python

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![pdfplumber](https://img.shields.io/badge/pdfplumber-0.10%2B-green.svg)](https://github.com/jsvine/pdfplumber)
[![pandas](https://img.shields.io/badge/pandas-2.0%2B-orange.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![YouTube](https://img.shields.io/badge/YouTube-Capycodev-red.svg)](https://www.youtube.com/@Capycodev)

> *"Los gurús de internet te dicen que subas facturas una por una a Claude o ChatGPT... pero con este script en Python de 15 líneas procesas 100 facturas en 1 segundo directamente en tu computadora."* — **Capycodev**

---

## 📖 Acerca del Proyecto

Este repositorio contiene el código fuente oficial del **Episodio 07 de Capycodev**. Es una solución ligera y 100% local para automatizar la extracción de datos contables (NIT, Fecha, Proveedor, IVA y Total) desde archivos PDF hacia una hoja de cálculo consolidada en Excel.

### 🚀 Ventajas sobre Claude / ChatGPT Web:
1. **Cero Límites de Subida:** Procesa carpetas masivas de 50, 100 o 500 facturas de golpe.
2. **100% Privado y Seguro:** Los datos financieros de tu empresa o clientes nunca viajan a servidores de terceros en la nube.
3. **Cero Costo de API:** Funciona con librerías de código abierto sin pagar suscripciones mensuales.

---

## 🏛️ Flujo de Procesamiento

```text
📁 CARPETA FACTURAS (PDFs)
            │
            ▼
┌───────────────────────────────┐
│     EXTRACCIÓN (pdfplumber)   │  ---> Lee texto y tablas de alta fidelidad
└───────────────────────────────┘
            │
            ▼
┌───────────────────────────────┐
│   NORMALIZACIÓN REGEX (`re`)  │  ---> Detecta NIT, IVA y Totales variables
└───────────────────────────────┘
            │
            ▼
┌───────────────────────────────┐
│     CONSOLIDACIÓN (pandas)    │  ---> Exporta a `contabilidad_automatica.xlsx`
└───────────────────────────────┘
```

---

## ⚡ Instalación y Uso Rápido

### 1. Clonar el repositorio
```bash
git clone https://github.com/capycodev/capy-auto-accounting.git
cd capy-auto-accounting
```

### 2. Instalar dependencias
```bash
python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Ejecutar el Script Principal
```bash
python auto_accounting.py
```
*(Si no tienes facturas reales, el script genera automáticamente facturas de prueba para demostrar el funcionamiento).*

### 4. Probar la Demo del Error de Novato
Para ver por qué el parseo manual con `.split()` falla en facturas con formatos variables:
```bash
python bug_demo_manual_copy_paste.py
```

---

## 📺 Video Tutorial

Puedes ver la explicación cómica, la analogía del superpoder de las librerías y la demostración en vivo en el canal de YouTube:  
👉 **[Ver en YouTube: @Capycodev](https://www.youtube.com/@Capycodev)**

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Úsalo libremente para automatizar la contabilidad de tu trabajo, tus finanzas personales o tus proyectos de software.

