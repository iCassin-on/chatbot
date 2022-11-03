import telebot
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('AUTH_TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["video"])
def video(mensagem):
    bot.send_message(mensagem.chat.id,
    "Infelizmente todas as nossas Placas de video foram compradas por Chineses para minerar Bitcoin. Clique aqui para iniciar: /opcao1 ")


@bot.message_handler(commands=["cpu"])
def cpu(mensagem):
    texto = """
    Selecione a marca desejada:
    
    /intelp Intel

    /amdp AMD    
    
    /opcao1 Voltar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["intelp"])
def intelp(mensagem):
    texto = """
    /i3 Intel i3-12100

    /i5 Intel i5-13600k

    /i7 Intel i7-13700k

    /i9 Intel i9-13900k
    
    /cpu Voltar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["i3"])
def intelp(mensagem):
    texto = """
    Intel i3-12100 R$999,99
    Clique aqui para voltar aos processarodes: /intelp ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["i5"])
def intelp(mensagem):
    texto = """
    Intel i5-13600k R$2.399,99
    Clique aqui para voltar aos processarodes: /intelp ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["i7"])
def intelp(mensagem):
    texto = """
    Intel i7-13700k R$3.399,99
    Clique aqui para voltar aos processarodes: /intelp ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["i9"])
def intelp(mensagem):
    texto = """
    Intel i9-13900k R$4.699,99 (TA PATRÃO HEIN)
    Clique aqui para voltar aos processarodes: /intelp ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["amdp"])
def amdp(mensagem):
    texto = """
    /ryzen5 AMD Ryzen 5 7600X

    /ryzen7 AMD Ryzen 7 7700X

    /ryzen9 AMD Ryzen 9 7900X

    /ryzen95 AMD Ryzen 9 7950X
    
    /cpu Voltar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["ryzen5"])
def amdp(mensagem):
    texto = """
    AMD Ryzen 5 7600X R$2.079,99 
    Clique aqui para voltar aos processarodes: /amdp ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["ryzen7"])
def amdp(mensagem):
    texto = """
    AMD Ryzen 7 7700X R$2.849,99
    Clique aqui para voltar aos processarodes: /amdp ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["ryzen9"])
def amdp(mensagem):
    texto = """
    AMD Ryzen 9 7900X R$3.949,99
    Clique aqui para voltar aos processarodes: /amdp ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["ryzen95"])
def amdp(mensagem):
    texto = """
    AMD Ryzen 9 7950X R$5.499,99 (Gostaria de cotar um extintor ?)
    Clique aqui para voltar aos processarodes: /amdp ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["ram"])
def ram(mensagem):
    texto = """
    /ddr3 RAM DDR3

    /ddr4 RAM DDR4

    /ddr5 RAM DDR5
    
    /opcao1 Voltar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["ddr3"])
def ram(mensagem):
    texto = """
    Memoria Kingston, 4GB (1x4GB), DDR3L, 1600MHz
    R$245,33
    Clique aqui para voltar as Memórias: /ram ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["ddr4"])
def ram(mensagem):
    texto = """
    /pny Memorias PNY

    /adata Memorias ADATA

    /corsair Memorias Corsair
    
    /ram Voltar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["pny"])
def pny(mensagem):
    texto = """
    Memoria PNY XLR8 Gaming, RGB, 8GB (1x8GB), DDR4, 3600MHz, CL18
    R$295,79
    Clique aqui para voltar as Memórias: /ram ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["adata"])
def adata(mensagem):
    texto = """
    Memoria Adata XPG Gammix D20, 8GB (1x8GB), DDR4, 3200Mhz, C16,
    R$332,93
    Clique aqui para voltar as Memórias: /ram ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["corsair"])
def corsair(mensagem):
    texto = """
    Memoria Corsair Vengeance RGB PRO, 8GB (1x8GB), DDR4, 3200MHz, C16
    R$259,99
    Clique aqui para voltar as Memórias: /ram ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["ddr5"])
def ram(mensagem):
    texto = """
    Memoria PNY Performance, 8GB (1x8GB), DDR5, 4800MHz, C40,
    R$1.137,29
    Clique aqui para voltar as Memórias: /ram ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["mtb"])
def mtb(mensagem):
    texto = """
    /intel Socket Intel LGA1700
    
    /amd Socket AMD AM5
    
    /opcao1 Voltar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["intel"])
def mtb(mensagem):
    texto = """
    /biostar Placa Mãe Asus
    
    /gigabyte Placa Mãe Gigabyte
    
    /mtb Voltar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["biostar"])
def biostar(mensagem):
    texto = """
    PLACA MAE BIOSTAR Z690GTA, DDR4, SOCKET LGA1700, ATX
    R$2.699,90
    Clique aqui para voltar: /intel ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["gigabyte"])
def gigabyte(mensagem):
    texto = """
    PLACA MAE GIGABYTE Z690 AORUS MASTER, DDR5, SOCKET 1700, ATX
    R$4.599,90
    Clique aqui para voltar: /intel ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["amd"])
def mtb(mensagem):
    texto = """
    PLACA MAE ASROCK X670E PG LIGHTNING, DDR5, ATX
    R$2.899,90
    Clique aqui para voltar as Placas Mãe: /mtb ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["fonte"])
def fonte(mensagem):
    texto = """
    /f650 Fonte 650W

    /f850 Fonte 850W

    /f1050 Fonte 1050W

    /opcao1 Voltar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["f650"])
def f650(mensagem):
    texto = """
    FONTE CORSAIR RMX SERIES RM650X, 650W, FULL MODULAR, 80 PLUS GOLD
    R$669,00
    Clique aqui para voltar: /fonte ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["f850"])
def f850(mensagem):
    texto = """
    FONTE CORSAIR RMX SERIES RM850X, 850W, FULL MODULAR, 80 PLUS GOLD
    R$1.264,65
    Clique aqui para voltar: /fonte ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["f1050"])
def f850(mensagem):
    texto = """
    FONTE COUGAR POLAR 1050, 1050W, FULL MODULAR, 80 PLUS PLATINUM
    R$1.999,90
    Clique aqui para voltar: /fonte ou inicio: /iniciar
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
    
    /iniciar Voltar 
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["teclado"])
def teclado(mensagem):
    texto = """
    /teclado1 Razer

    /teclado2 Corsair

    /teclado3 Hyperx

    /opcao2 Voltar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=['teclado1'])
def teclado1(mensagem):
    texto = """
    TECLADO GAMER RAZER HUNTSMAN V2 ANALOG CHROMA
    R$2.199,90
    Clique aqui para voltar: /teclado ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=['teclado2'])
def teclado2(mensagem):
    texto = """
    TECLADO MECANICO CORSAIR K95 RGB PLATINUM XT SWITCH CHERRY MX SPEED US
    R$1.199,99
    Clique aqui para voltar: /teclado ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=['teclado3'])
def teclado3(mensagem):
    texto = """
    TECLADO MECANICO GAMER HYPERX ALLOY ORIGINS, RGB, ABNT2
    R$529,90
    Clique aqui para voltar: /teclado ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["mouse"])
def mouse(mensagem):
    texto = """
    /mouse1 Razer

    /mouse2 Corsair

    /mouse3 Hyperx

    /opcao2 Voltar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=['mouse1'])
def mouse1(mensagem):
    texto = """
    MOUSE RAZER DEATHADDER V2 CHROMA 20000 DPI
    R$259,90
    Clique aqui para voltar: /mouse ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=['mouse2'])
def mouse2(mensagem):
    texto = """
    MOUSE GAMER CORSAIR SABRE RGB PRO CHAMPION SERIES, 18000 DPI
    R$349,99
    Clique aqui para voltar: /mouse ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=['mouse3'])
def mouse1(mensagem):
    texto = """
    MOUSE GAMER HYPERX PULSEFIRE SURGE, RGB, 16000DPI
    R$349,90
    Clique aqui para voltar: /mouse ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["headset"])
def headset(mensagem):
    texto = """
    /headset1 Razer

    /headset2 Corsair

    /headset3 Hyperx

    /opcao2 Voltar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=['headset1'])
def headset1(mensagem):
    texto = """
    HEADSET GAMER RAZER BLACKSHARK V2 PRO MULTIPLATAFORMA PRETO
    R$1.399,90
    Clique aqui para voltar: /headset ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=['headset2'])
def headset2(mensagem):
    texto = """
    HEADSET GAMER CORSAIR VIRTUOSO RGB WIRELESS XT, DRIVERS 50MM
    R$2.442,63
    Clique aqui para voltar: /headset ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=['headset3'])
def headset3(mensagem):
    texto = """
    HEADSET GAMER HYPERX CLOUD MIX, DRIVERS 40MM
    R$1.049,90
    Clique aqui para voltar: /headset ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
    /teclado  Teclado Gamer

    /mouse Mouse Gamer

    /headset Headset Gamer
    
    /iniciar Voltar
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    texto = """
    /kit1 Intel i5

    /kit2 Intel i7

    /kit3 AMD Ryzen 5

    /kit4 AMD Ryzen 7
    
    /iniciar Voltar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["kit1"])
def intel(mensagem):
    texto = """
    Kit upgrade, Intel i5-12600KF, Z690 DDR5, 16GB DDR5, Water Cooler X100 
    R$7.499,90
    Clique aqui para voltar os Kits: /opcao3 ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["kit2"])
def intel(mensagem):
    texto = """
    Kit upgrade, Intel i7-12700K, Z690 DDR4, 16GB DDR4
    R$5.103,12
    Clique aqui para voltar os Kits: /opcao3 ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["kit3"])
def intel(mensagem):
    texto = """
    Kit upgrade, AMD Ryzen 7 5700X, X570, 16GB DDR4, Water Cooler X100
    R$3.549,90
    Clique aqui para voltar os Kits: /opcao3 ou inicio: /iniciar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["kit4"])
def intel(mensagem):
    texto = """
    Kit upgrade, AMD Ryzen 9 3950X, X570, 8GB DDR4, Water Cooler X100
    R$4.499,90
    Clique aqui para voltar os Kits: /opcao3 ou inicio: /iniciar
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
    Seja bem-vindo(a) ao chat de cotação do grupo Delay. Destinado a gamers e entusiastas.
    Escolha uma opção para continuar (Clique no item):
    
     /opcao1 Hardware

     /opcao2 Periféricos

     /opcao3 Kit Upgrade

     /opcao4 Celulares
     
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)


bot.polling()