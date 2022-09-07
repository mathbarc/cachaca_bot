#!/usr/local/bin/python
# coding: utf8

import telebot
import random
import time
import os

class Session:    
    def __init__(self):
        self.all_doses = 0
        self.bebidas = []
        self.doses = {}

class ShotDrinks:

    def __init__(self) -> None:
        token = os.environ["BOT_TOKEN"]
        self.bot = telebot.TeleBot(token, threaded=False)
        self.sessions = {}
        
        
    def run(self):
        @self.bot.message_handler(commands="start")
        def start(message):
            self.sessions[message.chat.id] = Session()
            self.bot.send_message(chat_id=message.chat.id, text=f"Começando cedo meu consagrado!")
            time.sleep(1)
            self.bot.send_message(chat_id=message.chat.id, text=f"Se precisar de algo é so chamar:\n/tras monta o cardápio\n/desce vem umas doses la da cozinha\n/conta encerra os pedidos")

        @self.bot.message_handler(commands="desce")
        def desce(message):
            
            if len(self.sessions[message.chat.id].bebidas) == 0:
                self.bot.send_message(chat_id=message.chat.id, text=f"Tamo sem estoque mestre, manda trazer umas bebida ae")
                return    

            choose = random.randint(0, len(self.sessions[message.chat.id].bebidas)-1)
            doses = random.randint(1, 2)
            bebida = self.sessions[message.chat.id].bebidas[choose]
            self.sessions[message.chat.id].doses[bebida] += doses
            self.sessions[message.chat.id].all_doses+=doses
            self.bot.send_message(chat_id=message.chat.id, text=f"{doses} doses de {bebida}")
            time.sleep(1)
            
            
            dosesText = ""
            for k in self.sessions[message.chat.id].doses.keys():
                if self.sessions[message.chat.id].doses[k] > 0:
                    dosesText = dosesText + f"{self.sessions[message.chat.id].doses[k]} doses de {k}\n"    

            if(len(dosesText) > 0):
                dosesText = dosesText + f"num total de {self.sessions[message.chat.id].all_doses} doses"
                self.bot.send_message(chat_id=message.chat.id, text=f"Esses cornos já beberam: \n{dosesText}")

        @self.bot.message_handler(commands="tras")
        def tras(message):
            print(message.text)
            self.sessions[message.chat.id].bebidas = message.text.split(" ")
            self.sessions[message.chat.id].bebidas.pop(0)
            print(self.sessions[message.chat.id].bebidas)
            if(len(self.sessions[message.chat.id].bebidas) <= 0):
                self.bot.send_message(chat_id=message.chat.id, text=f"Tras o que filho de kenga?")
                return

            self.sessions[message.chat.id].doses.clear()

            for k in self.sessions[message.chat.id].bebidas:
                self.sessions[message.chat.id].doses[k] = 0
            self.sessions[message.chat.id].all_doses = 0

            self.bot.send_message(chat_id=message.chat.id, text=f"Abastecido, que comecem os trabalhos.")
            
        
        @self.bot.message_handler(commands="conta")
        def conta(message):
            for k in self.sessions[message.chat.id].bebidas:
                self.sessions[message.chat.id].doses[k] = 0
            self.sessions[message.chat.id].all_doses = 0

            self.bot.send_message(chat_id=message.chat.id, text=f"Mas já? Cs tão muito fraco.")

        self.bot.infinity_polling()


if __name__=="__main__":
    bot = ShotDrinks()
    bot.run() 
