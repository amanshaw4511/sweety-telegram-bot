from flask import Flask, request, jsonify, abort
import requests
import re
from os import environ

from telebot import TelegramBot
from getweather import getData


app = Flask(__name__)



@app.route('/')
def index():
    return "telebot homepage"

@app.route('/fqKVUFNFBJdS2NbGWKHq5TtRYdcgq1XL', methods=['POST'])
def telebot():
    if request.headers.get('Content-Type') == 'application/json' :
        update = request.json
        try:
            # extract text message, user name and chat id
            text = update['message']['text']
            message_id = str(update['message']['message_id'])
            chat_id = str(update['message']['chat']['id'])
            chat_type = update['message']['chat']['type']
            user_id = str(update['message']['from']['id'])
            


            bot_token = environ['TELEGRAM_BOT_TOKEN'] 
            telebot = TelegramBot(bot_token)
            
            if text.startswith('!weather'):
                city_name = text[8:].strip()
                print(city_name)
                matched_cities = getCity(city_name)
                if len(matched_cities) == 0:
                    otext = f"No City found with the name : {city_name}"
                    telebot.sendMessage(chat_id,otext)
                elif len(matched_cities) > 1 :
                    otext =f"please select the city from the given list\n"
                    i=0
                    for ocity in matched_cities:
                        otext += ocity[1] + "\n"
                        if i>10 :
                            otext += "and more ....."
                            break
                        i+=1
                    telebot.sendMessage(chat_id,otext)

                else :
                    data = getData(matched_cities[0][0])
                    otext = '\t Today Update\n'
                    for name,value in data['today'].items():
                        otext += name
                        otext += ' : {}\n'.format(value)
                    telebot.sendMessage(chat_id,otext)

                    otext = '\t Forcasts \n'
                    otext += 'date\tmin-temp\tmax-temp\t status\n'
                    for value in data['next7days'].values():
                        for each in value:
                            otext += '{}\t'.format(each)
                        otext += '\n'
                    telebot.sendMessage(chat_id, otext)
                return jsonify(True)



            # echo back message
            if chat_type != 'private' :
                telebot.sendMessage(chat_id, text, message_id)
            else :
                telebot.sendMessage(chat_id,text)

        except Exception as e:
            print(str(e))
        finally :
            return jsonify(True)
    return abort(403) 


def getCity(name):
    matched_cities = []
    with open('cityname.dat') as f :
        for line in f:
            cityid,city = line.split('|')
            c = re.compile(re.escape(name.upper()))
            if c.search(city.upper()): 
                matched_cities.append([cityid,city])

    return matched_cities

