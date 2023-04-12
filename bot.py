import nextcord
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import requests
from bs4 import BeautifulSoup
import datetime
import random


intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

TOKEN="YOUR_TOKEN"

def timeget():
    global date
    date = str(datetime.datetime.now())

version = "0.1c"

@bot.event
async def on_ready():
    timeget()
    await bot.change_presence(activity=nextcord.Game(name="détruire le capitalisme"))
    print("Started at : "+ date)

@bot.slash_command(name="version", description="Affiche la version actuelle de Karl.py")
async def version_cmd(interaction: Interaction):
    version_embed = nextcord.Embed(title="**Ma version**", description="je suis actuellemnt en version "+"__**"+version+"**__", color=0x00a4ff)
    await interaction.response.send_message(embed=version_embed)

@bot.slash_command(name="help", description="Affiche toutes les commandes possibles")
async def help(interaction: Interaction):
    help_embed = nextcord.Embed(title="__**Liste des commandes :**__", color=0x00dd02,description=
                                "**`/version`** : montre la version actuelle de Karl.py\n" +
                                "**`/quote`** : montre une citation aléatoire de Karl\n" + 
                                "**`/links`** : Affiche les liens sociaux\n" +
                                "C'est tout pour l'instant, plus de contenu est à venir."
                                )
    await interaction.response.send_message(embed=help_embed)

@bot.slash_command(name="quote", description="Affiche une citation de Karl")
async def quote(interaction: Interaction):
    url = "https://fr.wikiquote.org/wiki/Karl_Marx"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    quotes_list = list(soup.find_all("div", class_="citation"))
    del quotes_list[48:61]
    elem = quotes_list[random.randint(0, 47)]
    quote = elem.get_text()
    
    quote_embed = nextcord.Embed(title="**Voilà ma citation !**",description=quote,color=0xff0000)
    quote_embed.set_image(url="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjg1NjU0Mzk0MmEwNjRiYzk1Y2MyYWRlMDA3NGE2MTA0NzJkMjI4OCZjdD1n/mFw51RR5HkD4gYUbIx/giphy.gif")
    await interaction.response.send_message(embed=quote_embed)

@bot.slash_command(name="links", description="Afiche les différents liens sociaux")
async def links(interaction: Interaction):
    links_embed = nextcord.Embed(title="__**Liens de Darkpepito**__", color=0x0071ff, description=
                                 "__Steam:__ https://vu.fr/JIrz\n"+
                                 "__Musique (pas ouf):__ https://vu.fr/Dtdc\n"+
                                 "__Github:__ https://vu.fr/ORNM\n"+
                                 "\n(Les liens sont raccourcis, ne vous inquiétez pas de leur tronche)"
                                 )
    await interaction.response.send_message(embed=links_embed)

bot.run(TOKEN)