import asyncio
import discord
import time
import pytz
import random
import pytz
from datetime import datetime
import json
import os
import youtube_dl
import requests
import base64
from discord.ext import commands

#Los requisitos te los encuentras tu solito

TOKEN = "pon tu token aqui crack"
#no se ni pa que es esto, pero borra y cagaste
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='&', intents=intents)

#Main code

API_KEY = '1df0d6827de04f7f8e7f65650d1bcf86'
@client.event
async def on_message(message):
        if message.content.startswith('&noborrar'):
                        await message.channel.send('No borrar o no funciona nada') #no borrar, es como el puto coco del TF2          
        elif message.content.startswith('&hola'):
                        await message.channel.send('Hola que tal soy un bot bien pocho, pero mas pocho eres tu que lees esto')
        elif message.content.startswith('&login'):
                        await message.channel.send('Gato bobo, aqui tienes el login para controlarme :flushed: https://portal.daki.cc/server/3fa22bc2')
                        
        elif message.content.startswith('&test'):
                        await message.channel.send("""A ver si esto salta de 
                        linea, espero que si""")
        elif message.content.startswith('&info'):
                            await message.channel.send("Buenas, soy un bot que hace literalmente nada \n Gato me creo sin usar una plantilla ni na porque es mu bobo.\n Nisiquiera se que haces leyendo esto pero bueno, en algun momento supuse que alguien lo\n utilizaria. Asi que na, supongo que tendre algunas updates hasta que el bobo de gato deje de quererme como hace con todos")
        elif message.content.startswith("&lykos"):
        # gif
                        await message.channel.send("https://media.discordapp.net/attachments/1026230169381380146/1054920418781319229/lykos.gif")
        elif message.content.startswith("&gato"):
        # cancion de judios
                        await message.channel.send("https://cdn.discordapp.com/attachments/992181444510232667/1059483800968646706/video0-3-3.mov")
        elif message.content == "&codigo":
         with open("/home/container/test/run.py") as f:
            lines = len(f.readlines())
            await message.channel.send(f"Sorprendentemente tengo {lines} líneas de código y funciono.")

        elif message.content == "&marc":
                await message.channel.send("https://tenor.com/view/nerd-emoji-nerd-meme-radar-gif-26497624")
                num = random.randint(1, 10) # Genera un número al azar entre 1 y 10
                await message.channel.send("Se han detectado Marcs! Cantidad: {}".format(num))
        
        elif message.content == "&baila":
            await message.channel.send("https://tenor.com/view/dance-jester-dmc3-devil-may-cry3-arkham-gif-27251978")
            with open("/home/container/test/baila.mp3", "rb") as f:
                await message.channel.send("", file=discord.File(f))

        elif message.content == "&sniff": #frofro
            await message.channel.send("https://media.tenor.com/_pw-gfCVzg8AAAAd/sniff.gif")

        elif message.content == "&expulsar":
            expulsar = True
        elif message.content == "&detener":
            expulsar = False

        if message.content == "&pelea":
                    # Envía el GIF al canal de Discord
                    await message.channel.send("https://tenor.com/view/simpsons-monkey-fight-monkey-gif-5219878")
                    with open("/home/container/test/banjopelea.mp3", "rb") as f:
                        await message.channel.send("", file=discord.File(f))
                        await message.channel.send("Dale al play para tener una cancioncita mientras \n Se pelean en el chat")
                        
        if "&furro" in message.content:
            mentioned_user = message.mentions[0]
            if mentioned_user.id == 341690651156676612:
                response = f"{mentioned_user.mention} Mi creador no es un Furro :moyai: ." #inmunidad kekw
            else:
                furro_percent = random.randint(1, 100)
                response = f"{mentioned_user.mention} es un {furro_percent}% furro"
            await message.channel.send(response)

        
        if message.content.startswith("&clear"):
            _, _, num_messages = message.content.partition(" ")
            if num_messages.isdigit():
                num_messages = int(num_messages)
                if message.author.guild_permissions.administrator or any(role.permissions.manage_messages for role in message.author.roles):
                    await message.channel.purge(limit=num_messages)
                    await message.channel.send(f"A chuparla {num_messages} mensajes.")
                else:
                    await message.channel.send("Tontito, que no estoy tan mal hecho, tu no puedes ejecutar ese comando, que me la lias")

            #esto ni funciona 25/11/2022 pero si lo borro no funciona nada
        if message.content.startswith("&clear"):
                    _, _, user_reason = message.content.partition(" ")
                    user, _, reason = user_reason.partition(" ")
                    user = message.mentions[0]
                    if message.author.guild_permissions.administrator or any(role.permissions.kick_members for role in message.author.roles):
                        await message.guild.kick(user, reason=reason)
                        await message.channel.send(f"{user.mention} (KICK) ha sido mandado a tomar por culo por:  {reason}")
        if message.content.startswith("&ban"):
                    _, _, user_reason = message.content.partition(" ")
                    user, _, reason = user_reason.partition(" ")
                    user = message.mentions[0]
                    if message.author.guild_permissions.administrator or any(role.permissions.ban_members for role in message.author.roles):
                        await message.guild.ban(user, reason=reason)
                        await message.channel.send(f"{user.mention} (BAN)ha sido ejecutado por el partido por : {reason}")
        
                    if message.content.startswith('&mute'): #ni funciona seguro
                        words = message.content.split()

                        if len(words) < 3 or not message.mentions:
                            await message.channel.send('Por favor especifica un usuario y un tiempo para el mute')
                        return

                    user = message.mentions[0]
                    time = words[1]
                    reason = words[2:]
        #Comando ayuda - Falta poner comandos
        if message.content == "&ayuda":
            commands = [
                {"name": "&hola", "descripcion": "Te dice hola el muy bobo."},
                {"name": "&ayuda", "descripcion": "Muestra esta ayuda."},
                {"name": "&lykos", "descripcion": "Manda la oruga azul fea esa con el tag del Lykos."},
                {"name": "&info", "descripcion": "Mi triste historia."},
                {"name": "&baila", "descripcion": "Pues me pongo a bailar, y te pongo la musica en el chat tambien."},
                {"name": "&pelea", "descripcion": "Musica para cuando se pelean en el chat."},
                {"name": "&codigo", "descripcion": "Gato: Me aburria mucho asi que hice que se contase sus propias lineas de codigo."},
                {"name": "&marc", "descripcion": "Detecta cuantos Marcs hay cerca."},
                {"name": "&login", "descripcion": "Pa cuando se me olvida donde se controla el bot."},
                {"name": "&geo", "descripcion": "Utiliza &geo IP y te da info de la ip."}
                            ]
            response = "Lista de comandos: \n"
            for command in commands:
                response += f"{command['name']}: {command['descripcion']}\n"     
        pais = None
        if message.content.startswith('&hora'):
            pais = message.content.split('&hora ')[-1]
        if pais:
            try:
                timezone = pytz.timezone(pytz.country_timezones[pais.upper()][0])
                hora_actual = datetime.now(timezone).strftime('%H:%M:%S')
                await message.channel.send(f"La hora actual en {pais} es {hora_actual}")
            except KeyError:
                await message.channel.send(f"No se pudo encontrar información de la zona horaria para {pais}")
        #
          #
                                        #  _____ _  _ _______ ___  
                                        # / ____| || |__   __/ _ \ 
                                        #| |  __| || |_ | | | | | |
                                        #| | |_ |__   _|| | | | | |
                                        #| |__| |  | |  | | | |_| |
                                        # \_____|  |_|  |_|  \___/  TO WAPO ESTO E O NO
          #
          #
          #
          #
          #
          #
          # Toca probar
        if message.content.startswith('&ping'):
            user = message.content.split(' ')[1]
            channel = random.choice(client.get_all_channels())
            await channel.send(f'{user} ¡Hola! Este es un mensaje aleatorio.')
            await asyncio.sleep(random.choice([300, 1200])) # 5 o 20 minutos
            await channel.send(f'{user} ¡Hola de nuevo! Este es otro mensaje aleatorio.')
            while True:
                stop = await client.wait_for('message')
                if stop.content == '&stop':
                    await channel.send(f'{user} Ya no te mencionaré más.')
                    break
              #
          #
          #
          #
          # https://youtu.be/dQw4w9WgXcQ
          #
          #
          #
          # tocho de separar porque me lio
          # 
          # 
          # toma doxxeo                       
        if message.content.startswith('&geo'):
            ip = message.content.split(' ')[1]
            url = f'https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={ip}'
            response = requests.get(url)
            data = json.loads(response.text)
            if 'country_name' in data:
                country = data['country_name']
                state = data['state_prov']
                city = data['city']
                isp = data['isp']
                latitude = data['latitude']
                longitude = data['longitude']

                embed = discord.Embed(title=f'Información de la dirección IP: {ip}', color=0x00ff00)
                embed.add_field(name='País', value=country, inline=True)
                embed.add_field(name='Estado/Provincia', value=state, inline=True)
                embed.add_field(name='Ciudad', value=city, inline=True)
                embed.add_field(name='Proveedor de internet', value=isp, inline=False)
                embed.add_field(name='Latitud', value=latitude, inline=True)
                embed.add_field(name='Longitud', value=longitude, inline=True)

                embed.set_footer(text='Creado por G4T0')

                await message.channel.send(embed=embed)
            else:
                await message.channel.send('No se pudo obtener información para la dirección IP proporcionada')
#ni funciona T-T
        if message.content.startswith("&restart") and message.author.id == os.environ["OWNER_ID"]:
        # Envía un mensaje al canal indicando que el bot se reiniciará
            await message.channel.send("Reiniciando el bot...")
            # Reinicia el bot
            await client.logout()

def new_func(reason):
    reason = ' '.join(reason)
    return reason

#Main code




client.run(TOKEN)
