import tkinter as tk

class ControlFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        tk.Label(self, text="Número de registro:").pack(side=tk.LEFT, padx=5)
        self.entry_numero_registro = tk.Entry(self, width=10)
        self.entry_numero_registro.pack(side=tk.LEFT, padx=5)

        self.btn_mostrar_registro = tk.Button(self, text="Mostrar Registro", command=self.mostrar_registro)
        self.btn_mostrar_registro.pack(side=tk.LEFT, padx=5)

        self.btn_mostrar_todos = tk.Button(self, text="Mostrar Todos", command=self.app.mostrar_todos)
        self.btn_mostrar_todos.pack(side=tk.LEFT, padx=5)

        self.btn_refresh = tk.Button(self, text="Refrescar", command=self.app.mostrar_todos)
        self.btn_refresh.pack(side=tk.LEFT, padx=5)

    def mostrar_registro(self):
        """Llama a la función de la app para mostrar un registro específico"""
        numero_registro = self.entry_numero_registro.get().strip()
        self.app.mostrar_registro(numero_registro)
