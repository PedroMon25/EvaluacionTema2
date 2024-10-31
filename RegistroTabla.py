import tkinter as tk
from tkinter import ttk

class RegistroTabla(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        scrollbar = tk.Scrollbar(self, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.tree = ttk.Treeview(self,
                                 columns=("Id", "Cliente", "Habitacion", "Email", "Telefono", "CuentaDePago", "Ingreso"),
                                 show='headings',
                                 yscrollcommand=scrollbar.set)
        self.tree.pack(expand=True, fill='both')

        scrollbar.config(command=self.tree.yview)

        column_names = ["Id", "Cliente", "Habitacion", "Email", "Telefono", "CuentaDePago", "Ingreso"]
        for col in column_names:
            self.tree.heading(col, text=col)

        self.tree.column("Id", width=50)
        self.tree.column("Habitacion", width=80)
        self.tree.column("CuentaDePago", width=100)

    def actualizar_tabla(self, registros):
        """Actualiza la tabla con los registros dados"""
        for row in self.tree.get_children():
            self.tree.delete(row)

        for registro in registros:
            self.tree.insert("", "end", values=(
                registro["Id"],
                registro["Cliente"],
                registro["Habitacion"],
                registro["Email"],
                registro["Telefono"],
                registro["CuentaDePago"],
                registro["Ingreso"]
            ))
