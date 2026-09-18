import os
import tkinter as tk
from tkinter import filedialog, messagebox
from docx2pdf import convert
import threading

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(
        title="Selecciona el archivo Word",
        filetypes=[("Documentos Word", "*.docx")]
    )
    if archivo:
        ruta_word.set(archivo)
        label_archivo.config(text=f"📄 Archivo seleccionado:\n{archivo}")

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory(title="Selecciona carpeta de destino")
    if carpeta:
        ruta_destino.set(carpeta)
        label_carpeta.config(text=f"📁 Carpeta seleccionada:\n{carpeta}")

def proceso_conversion(archivo, ruta_pdf):
    try:
        convert(archivo, ruta_pdf)
        messagebox.showinfo("Éxito", f"✅ PDF generado exitosamente:\n{ruta_pdf}")
    except Exception as e:
        messagebox.showerror("Error", f"⚠️ Error durante la conversión:\n{e}")

def convertir():
    archivo = ruta_word.get()
    carpeta = ruta_destino.get()

    if not archivo or not carpeta:
        messagebox.showerror("Error", "Debes seleccionar el archivo y la carpeta de destino.")
        return

    nombre_pdf = os.path.splitext(os.path.basename(archivo))[0] + ".pdf"
    ruta_pdf = os.path.join(carpeta, nombre_pdf)

    hilo = threading.Thread(target=proceso_conversion, args=(archivo, ruta_pdf))
    hilo.start()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Convertidor Word a PDF")
ventana.geometry("500x300")
ventana.resizable(False, False)

# Variables para rutas
ruta_word = tk.StringVar()
ruta_destino = tk.StringVar()

# Etiquetas y botones
tk.Label(ventana, text="📝 Conversor de Word a PDF", font=("Arial", 16, "bold")).pack(pady=10)

tk.Button(ventana, text="Seleccionar archivo Word", command=seleccionar_archivo).pack(pady=5)
label_archivo = tk.Label(ventana, text="📄 Ningún archivo seleccionado", wraplength=480)
label_archivo.pack()

tk.Button(ventana, text="Seleccionar carpeta de destino", command=seleccionar_carpeta).pack(pady=5)
label_carpeta = tk.Label(ventana, text="📁 Ninguna carpeta seleccionada", wraplength=480)
label_carpeta.pack()

tk.Button(ventana, text="Convertir a PDF", command=convertir, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=20)

# Ejecutar ventana
ventana.mainloop()