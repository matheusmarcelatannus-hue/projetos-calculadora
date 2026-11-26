
import tkinter as tk

ent1 = 0
ent2 = ""
ent3 = 0

def calcular(operacao):
    global ent1, ent2, ent3

    try:
        ent1 = int(numero1.get())
        ent3 = int(numero2.get())
        ent2 = operacao

        if ent2 == "+":
            opA = ent1 + ent3
            resultado.config(text=f"Resultado: {opA}")

        elif ent2 == "-":
            opB = ent1 - ent3
            resultado.config(text=f"Resultado: {opB}")

        elif ent2 == "*":
            opC = ent1 * ent3
            resultado.config(text=f"Resultado: {opC}")

        elif ent2 == "/":
            opD = ent1 / ent3
            resultado.config(text=f"Resultado: {opD}")

        elif ent2 == "**":
            opE = ent1 ** ent3
            resultado.config(text=f"Resultado: {opE}")

        else:
            resultado.config(text="Isso nem é operação, boboca!")

    except ValueError:
        resultado.config(text="Digite números válidos!")

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x600")
janela.configure(bg="#171717")
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="CALCULADORA",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#171717"
)
titulo.pack(pady=20)

numero1 = tk.Entry(
    janela,
    font=("Arial", 18),
    justify="center",
    bg="#303030",
    fg="white",
    insertbackground="white"
)
numero1.pack(pady=10, padx=30, fill="x")

numero1.insert(0, "Número 1")

numero2 = tk.Entry(
    janela,
    font=("Arial", 18),
    justify="center",
    bg="#303030",
    fg="white",
    insertbackground="white"
)
numero2.pack(pady=10, padx=30, fill="x")

numero2.insert(0, "Número 2")

texto = tk.Label(
    janela,
    text="Escolha uma operação:",
    font=("Arial", 14),
    fg="white",
    bg="#171717"
)
texto.pack(pady=15)

frame = tk.Frame(janela, bg="#171717")
frame.pack()

operacoes = [
    ("+", "+"),
    ("-", "-"),
    ("×", "*"),
    ("÷", "/"),
    ("x²", "**")
]

for i, (visual, op) in enumerate(operacoes):
    botao = tk.Button(
        frame,
        text=visual,
        font=("Arial", 18, "bold"),
        width=5,
        height=2,
        bg="#ff9500",
        fg="white",
        activebackground="#ffaa33",
        command=lambda x=op: calcular(x)
    )
    botao.grid(row=i // 3, column=i % 3, padx=6, pady=6)

resultado = tk.Label(
    janela,
    text="Resultado: ",
    font=("Arial", 18, "bold"),
    fg="#00ff99",
    bg="#171717"
)
resultado.pack(pady=25)

janela.mainloop()
