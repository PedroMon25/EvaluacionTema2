import tkinter as tk
from tkinter import messagebox
import requests
from control_frame import ControlFrame
from RegistroTabla import RegistroTabla


class EvaluacionTema2:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Huéspedes")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)

        # Crear instancia del frame de control
        self.control_frame = ControlFrame(self.root, self)
        self.control_frame.pack(pady=10)

        # Redimensionar automaticamente la tabla
        self.table_frame = RegistroTabla(self.root)
        self.table_frame.pack(expand=True, fill='both')

        # Mostrar todos los registros al inicio
        self.mostrar_todos()

    def obtener_registros(self):
        """Obtiene los registros desde la API en formato JSON"""
        url = "https://671be4192c842d92c381a4c5.mockapi.io/RegistroHuespedes"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"No se pudo conectar a la API: {e}")
            return []

    def mostrar_todos(self):
        """Muestra todos los registros en la tabla"""
        registros = self.obtener_registros()
        registros.sort(key=lambda x: int(x["Id"]))
        self.table_frame.actualizar_tabla(registros)

    def mostrar_registro(self, numero_registro):
        """Muestra el registro específico ingresado por el usuario"""
        if not numero_registro.isdigit():
            messagebox.showwarning("Advertencia", "Por favor, ingrese un número de registro válido.")
            return None

        numero_registro = int(numero_registro)
        registros = self.obtener_registros()
        registro = next((r for r in registros if int(r['Id']) == numero_registro), None)

        if registro:
            self.table_frame.actualizar_tabla([registro])
        else:
            messagebox.showinfo("Información", "No se encontró un registro con ese número.")


if __name__ == "__main__":
    root = tk.Tk()
    app = EvaluacionTema2(root)
    root.mainloop()
