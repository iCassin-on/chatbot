import telebot

CHAVE_API = "5756900955:AAG3x6hma-V3R24QhVOE3kvsxJhtrAqylj4"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["video"])
def video(mensagem):
    bot.send_message(mensagem.chat.id, "Infelizmente todas as nossas Placas de video foram compradas por Chineses para minerar Bitcoin.clique aqui para iniciar: /iniciar ")

@bot.message_handler(commands=["cpu"])
def cpu(mensagem):
    texto = """
    Selecione a marca desejada:
    /intel Intel
    
    /amd AMD    
    """
    bot.send_message(mensagem.chat.id, texto)
    
@bot.message_handler(commands=["intel"])
def intel(mensagem):
    texto = """
    /i3 Intel i3-12100
    
    /i5 Intel i5-13600k
    
    /i7 Intel i7-13700k
    
    /i9 Intel i9-13900k
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["i3"])
def intel(mensagem):
    texto = """
    Intel i3-12100 R$999,99
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["i5"])
def intel(mensagem):
    texto = """
    Intel i5-13600k R$2.399,99
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["i7"])
def intel(mensagem):
    texto = """
    Intel i7-13700k R$3.399,99
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["i9"])
def intel(mensagem):
    texto = """
    Intel i9-13900k R$4.699,99 (TA PATRÃO HEIN)
    """
    bot.send_message(mensagem.chat.id, texto)
    
@bot.message_handler(commands=["amd"])
def amd(mensagem):
    texto = """
    /ryzen5 AMD Ryzen 5 7600X
    
    /ryzen7 AMD Ryzen 7 7700X
    
    /ryzen9 AMD Ryzen 9 7900X
    
    /ryzen95 AMD Ryzen 9 7950X
    """
    bot.send_message(mensagem.chat.id, texto)
    
@bot.message_handler(commands=["ryzen5"])
def amd(mensagem):
    texto = """
    AMD Ryzen 5 7600X R$2.079,99 
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["ryzen7"])
def amd(mensagem):
    texto = """
    AMD Ryzen 7 7700X R$2.849,99
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["ryzen9"])
def amd(mensagem):
    texto = """
    AMD Ryzen 9 7900X R$3.949,99
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["ryzen95"])
def amd(mensagem):
    texto = """
    AMD Ryzen 9 7950X R$5.499,99 (Gostaria de cotar um extintor ?)
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["ram"])
def ram(mensagem):
    texto = """
    /ddr3 RAM DDR3
    
    /ddr4 RAM DDR4
    
    /ddr5 RAM DDR5
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["ddr3"])
def ram(mensagem):
    texto = """
    Memoria Kingston, 4GB (1x4GB), DDR3L, 1600MHz
    R$245,33
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["ddr4"])
def ram(mensagem):
    texto = """
    /pny Memorias PNY
    
    /adata Memorias ADATA
    
    /corsair Memorias Corsair
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["pny"])
def pny(mensagem):
    texto = """
    Memoria PNY XLR8 Gaming, RGB, 8GB (1x8GB), DDR4, 3600MHz, CL18
    R$295,79
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["adata"])
def adata(mensagem):
    texto = """
    Memoria Adata XPG Gammix D20, 8GB (1x8GB), DDR4, 3200Mhz, C16,
    R$332,93
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["corsair"])
def corsair(mensagem):
    texto = """
    Memoria Corsair Vengeance RGB PRO, 8GB (1x8GB), DDR4, 3200MHz, C16
    R$259,99
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["ddr5"])
def ram(mensagem):
    texto = """
    Memoria PNY Performance, 8GB (1x8GB), DDR5, 4800MHz, C40,
    R$1.137,29
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que gostaria de cotar conosco? (Clique em uma opção)
    /video Placa de video
    
    /cpu Processador
    
    /ram Memória RAM
    
    /mtb Placa Mãe
    
    /fonte Fonte de Alimentação    
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
    /teclado
    
    /mouse
    
    /headset  
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["teclado"])
def intel(mensagem):
    texto = """
    /teclado1 Razer
    
    /teclado2 Corsair
    
    /teclado3 Hyperx
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    texto = """
    /kit1 Intel i5
    
    /kit2 Intel i7
    
    /kit3 AMD Ryzen 5
    
    /kit4 AMD Ryzen 7
    """
    bot.send_message(mensagem.chat.id, texto)
    
@bot.message_handler(commands=["kit1"])
def intel(mensagem):
    texto = """
    Kit upgrade, Intel i5-12600KF, Z690 DDR5, 16GB DDR5, Water Cooler X100 
    R$7.499,90
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["kit2"])
def intel(mensagem):
    texto = """
    Kit upgrade, Intel i7-12700K, Z690 DDR4, 16GB DDR4
    R$5.103,12
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["kit3"])
def intel(mensagem):
    texto = """
    Kit upgrade, AMD Ryzen 7 5700X, X570, 16GB DDR4, Water Cooler X100
    R$3.549,90
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["kit4"])
def intel(mensagem):
    texto = """
    Kit upgrade, AMD Ryzen 9 3950X, X570, 8GB DDR4, Water Cooler X100
    R$4.499,90
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao4"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Não somos Casas Bahia, por favor procure outro fornecedor. ")



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Hardware
     
     /opcao2 Periféricos
     
     /opcao3 Kit Upgrade
     
     /opcao4 Celulares
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()