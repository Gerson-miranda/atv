import customtkinter as ctk

# formula imc =peso/(altura*altura)
# condições:
# se imc<18.5:magreza
# se imc>=18.5 e imc<25:peso ideal
# se imc>=25 imc <30;sobrepeso
# se imc>=30:obesidade

def calculu(event):
    p=int(altura.get()) 
    a=float(peso.get())
    soma=p/(a*a)
    if(soma<18.5):
        resultado.configure(text=(f'seu imc é de {soma:.1f} você é magro'))  
    if(soma>=18.5 and soma<25):
        resultado.configure(text=(f'seu imc é de {soma:.1f} você esta no peso ideal'))  
    if(soma>=25 and soma<30):
        resultado.configure(text=(f'seu imc é de {soma:.1f} você esta com sobrepeso'))  
    else:
        resultado.configure(text=(f'seu imc é de {soma:.1f} você esta com obsidade'))  

def limpar():
    nome.delete(0,'end')
    altura.delete(0,'end')
    peso.delete(0,'end')
    resultado.configure(text='')

ctk.set_appearance_mode('dark')

janela = ctk.CTk()

janela.geometry('500x500')

ctk.CTkLabel(janela,
             text='aplicativo Saúde ',
             font=('arial',20,'bold'),
             text_color='white',
             ).pack(pady=10)

nome= ctk.CTkEntry(janela,
                   placeholder_text='digite seu nome',
                   width=400,
                   height=40)
nome.pack(pady=10)

altura= ctk.CTkEntry(janela,
                   placeholder_text='digite a sua altura',
                   width=400,
                   height=40)
altura.pack(pady=10)

peso= ctk.CTkEntry(janela,
                   placeholder_text='digite seu peso',
                   width=400,
                   height=40)
peso.pack(pady=10)

calcular=ctk.CTkButton(janela,
                       text='calcular',
                       font=('arial',20,'bold'),
                       fg_color='blue',
                       command=calculu)
calcular.place(x=40,y=250)

limpar=ctk.CTkButton(janela,
                       text='limpar',
                       font=('arial',20,'bold'),
                       fg_color='blue',command=limpar)
limpar.place(x=240,y=250)

resultado=ctk.CTkLabel(janela,
                       text='',
                       font=('arial',18))
resultado.pack(pady=78)

janela.bind('<Return>',calculu)
janela.mainloop()