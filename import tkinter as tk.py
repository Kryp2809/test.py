import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Clientes")
        self.geometry("700x500")

        # Criar frames para organizar os widgets
        self.frame_dados = ttk.Frame(self, padding=10)
        self.frame_botoes = ttk.Frame(self, padding=10)

        # Organizar os frames na janela principal
        self.frame_dados.pack(fill=tk.BOTH, expand=True)
        self.frame_botoes.pack(fill=tk.X)

        # Criar os campos de entrada
        self.name_entry = self.create_entry_field("Nome:", 0, 0)
        self.phone_entry = self.create_entry_field("Telefone:", 1, 0)
        self.city_entry = self.create_entry_field("Cidade:", 2, 0)

        # Criar o botão "Salvar"
        self.save_button = ttk.Button(self.frame_botoes, text="Salvar", command=self.save_data)
        self.save_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Criar o botão "Limpar"
        self.clear_button = ttk.Button(self.frame_botoes, text="Limpar", command=self.clear_all_fields)
        self.clear_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def create_entry_field(self, label_text, row, column):
        """Cria um campo de entrada com rótulo."""
        label = ttk.Label(self.frame_dados, text=label_text)
        label.grid(row=row, column=column, sticky=tk.W)
        entry = ttk.Entry(self.frame_dados)
        entry.grid(row=row, column=column+1, sticky=tk.EW)
        return entry

    def clear_all_fields(self):
        """Limpa todos os campos de entrada."""
        for child in self.frame_dados.winfo_children():
            if isinstance(child, ttk.Entry):
                child.delete(0, 'end')

    def save_data(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        city = self.city_entry.get()

        # Validação básica
        if not name or not phone or not city:
            messagebox.showwarning("Aviso", "Todos os campos são obrigatórios.")
            return

        if not phone.isdigit():
            messagebox.showwarning("Aviso", "O telefone deve conter apenas números.")
            return

        # Salvando os dados em um arquivo CSV (ajuste o caminho se necessário)
        try:
            with open('cadastro.csv', 'a') as file:
                file.write(f"{name},{phone},{city}\n")
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        except IOError:
            messagebox.showerror("Erro", "Não foi possível salvar os dados.")

if __name__ == "__main__":
    app = Application()
    app.mainloop()