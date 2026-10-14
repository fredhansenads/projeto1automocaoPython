# Automação de Sistemas e Processos com Python
# Todos os dias, o nosso sistema atualiza as vendas do dia anterior. O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior

import pyautogui
import time
import pandas
import openpyxl
import pyperclip

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
link = "https://drive.google.com/drive/u/0/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=1779, y=479)
time.sleep(1)
pyautogui.click(x=1418, y=509)
time.sleep(5)

caminho = r"C:\Users\PC-01\Downloads\Vendas - Dez.xlsx"
tabela = pandas.read_excel(caminho)
print(tabela)
faturamento = tabela["Valor Final"].sum()
qtde_produtos = tabela["Quantidade"].sum()
print(faturamento)
print(qtde_produtos)

pyautogui.hotkey("ctrl", "t")
pyautogui.write("http://mail.google.com/")
pyautogui.press("enter")
time.sleep(8)
pyautogui.click(x=93, y=278)
time.sleep(6)
pyautogui.write("fredhansenads@gmail.com")
pyautogui.press("tab") # seleciona o email
pyautogui.press("tab") # passar para o campo do assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
texto = f"""
Prezados,

Segue o relatório de vendas de hoje.

Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {qtde_produtos:,}

Qualquer dúvida estou à disposição.
Abs,
Lira Python
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.click(x=1192, y=945)


