import tkinter as tk
from tkinter import messagebox
import ast

class Calculadora:
    def __init__(self, root):
        self.root = root #root é o painel principal, nessa linha torna esse painel como global para ter acesso em todo programa
        self.root.title("Calculadora") #declara o texto na barra superior do programa
        self.root.geometry("300x450")
        self.root.configure(bg="#E0E0E0")

        # Variável para armazenar a expressão atual
        self.expressao = ""

        # Título
        tk.Label(root, text="CALCULATOR", bg="#E0E0E0", font=("Arial", 10)).pack(pady=(10, 0))

        # Display (usando Entry para facilitar a inserção de texto, state = "readonly" seta somente como leitura, nem o próprio programa pode editar, porem na "def atualizar_display" ele é alterado para state="normal", onde pode ser editado, recebe os dados e fecha logo em seguida, impedindo a entrada do usuário)
        self.display = tk.Entry(root, font=("Arial", 24), bd=2, relief="sunken", justify="right",state="readonly")
        self.display.pack(padx=10, pady=10, fill="x")

        # Frame para os botões
        frame_botoes = tk.Frame(root, bg="#E0E0E0")
        frame_botoes.pack(padx=10, pady=10, fill="both", expand=True)

        # Layout dos botões
        botoes = [
            ['C', '²', '√', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['D', '0', '.', '=']
        ]

        for r, linha in enumerate(botoes):
            for c, texto in enumerate(linha):
                # Usamos uma função lambda para passar o texto do botão para o processador
                comando = lambda t=texto: self.ao_clicar(t)
                
                btn = tk.Button(
                    frame_botoes, text=texto, font=("Arial", 12, "bold"),
                    bg="#F0F0F0", relief="raised", bd=1,
                    command=comando
                )
                btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

        # Configurar expansão das colunas/linhas
        for i in range(4): frame_botoes.grid_columnconfigure(i, weight=1)
        for i in range(5): frame_botoes.grid_rowconfigure(i, weight=1)

    def calcular(self, expressao_matematica):
        try:
            # Substituímos operadores visuais para o padrão Python se necessário
            expr = expressao_matematica.replace('^', '**',)#aqui ele segue a ordem da matriz feita, no caso botoes
            
            # O parse analisa o código sem executá-lo. 
            # Se não for uma expressão matemática simples, ele falha aqui.
            teste_calcular = ast.parse(expr, mode='eval')
            
            # Agora que sabemos que é uma expressão segura, compilamos e executamos
            return str(eval(compile(teste_calcular, '<string>', 'eval')))
        except Exception:
            return "Erro, expressão inválida"


    def ao_clicar(self, tecla):
        if tecla == "C":
            self.expressao = ""
        elif tecla == "D":
            self.expressao = self.expressao[:-1]
        elif tecla == "=":
            self.expressao = self.calcular(self.expressao)
        elif tecla == "²":
            self.expressao = self.calcular(f"({self.expressao})**2")
        elif tecla == "√":
            self.expressao = self.calcular(f"({self.expressao})**0.5")
        else:
            self.expressao += str(tecla)

        self.atualizar_display()

        # Atualiza o display visualmente
        self.atualizar_display()

    def atualizar_display(self):
        # 1. Muda para normal para permitir que o código altere o conteúdo
        self.display.configure(state="normal")
        
        # 2. Limpa e insere o novo valor
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expressao)
        
        # 3. Bloqueia novamente para o usuário
        self.display.configure(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    Calculadora(root)
    root.mainloop()