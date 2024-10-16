import customtkinter as ctk
from deep_translator import GoogleTranslator
# ---------funções-----
def traduzir():
    texto_traduzido.delete(0,'end')
    texto_para_traduzir=user_text.get()
    linguagem=var_recebe.get()
    saida=GoogleTranslator(source='auto',target=linguagem).translate(texto_para_traduzir)
    texto_traduzido.configure(state='normal')
    texto_traduzido.insert(0,saida)

# -----------------------

ctk.set_appearance_mode('dark')

janela=ctk.CTk()
janela.geometry('600x400')
janela.resizable(False,False)
janela.title('Tradutor Universal v1.0')

ctk.CTkLabel(janela,
             text='Tradutor Universal - By Gerson',
             font=('arial',25,'bold'),
             text_color='green').pack(pady=5)

user_text= ctk.CTkEntry(janela,
                        width=500,
                        height=50,
                        placeholder_text='Digite o texteto para traduzir',)
user_text.pack(pady=20)

ctk.CTkLabel(janela,
             text='Escolha o idioma para tradução',
             font=('arial',18,'bold'),
             text_color='white').pack(pady=5)

var_recebe= ctk.StringVar(value='english')

lista_indioma= GoogleTranslator().get_supported_languages()

idioma = ctk.CTkOptionMenu(janela,
                            values=lista_indioma,
                            variable=var_recebe)
idioma.set('english')
idioma.pack(pady=5)

texto_traduzido = ctk.CTkEntry(janela,
                               width=500,
                               height=100,
                               placeholder_text='Aqui vai aparecer o texto traduzido',
                               state= ctk.DISABLED)
texto_traduzido.pack(pady=3)

botao= ctk.CTkButton(janela,
                     text='Traduza',
                     font=('arial',18,'bold'),
                     command=traduzir)
botao.pack()

janela.mainloop()