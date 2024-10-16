# Gerson,Luis,JoâoPaulo
import customtkinter as ctk

def calculu():
    a= float(ch.get())
    b= float(faltas_por_dias.get())
    
    conversao_dias = a/4
    faltas_max = b*0.25
    feijao = (a/b)*100
    converter_horas = feijao*4
    
    if b>faltas_max:
        resultado.configure(text=('você foi reprovado'))
    else:
        dias_restantes = faltas_max-b
        resultado.configure(text=(f'você tem  {feijao:.0f}% você pode ainda ter {dias_restantes:.0f} dias para faltar'))

ctk.set_appearance_mode('dark')

janela = ctk.CTk()

janela.geometry('500x500')

ctk.CTkLabel(janela,
             text='Gerenciado de Faltas',
             font=('arial',20,'bold'),
             text_color='white',
             ).pack(pady=10)

ch= ctk.CTkEntry(janela,
                 placeholder_text='Digite a Carga Horaria',
                 width=450,
                 height=50)
ch.pack(pady=10)

faltas_por_dias= ctk.CTkEntry(janela,
                 placeholder_text='Faltas por Dias ',
                 width=450,
                 height=50)
faltas_por_dias.pack(pady=10)

calcular=ctk.CTkButton(janela,
                       text='calcular',
                       font=('arial',20,'bold'),
                       fg_color='blue',command= calculu)
calcular.pack(pady=10)

resultado=ctk.CTkLabel(janela,
                       text='',
                       font=('arial',18))
resultado.pack(pady=5)




janela.mainloop()