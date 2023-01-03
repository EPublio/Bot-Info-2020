import discord
from get_tarefas import get_tarefas
from get_aulas import get_aulas
import login

client = discord.Client()

@client.event
async def on_ready():    
    print("bot on")
    
@client.event
async def on_message(message):
    
    if message.author == client.user :
        return
    cmd = ["-help","-ajuda"]
    if message.content.lower() in cmd:
        aaa = discord.Embed(title="**Comandos**", url="", description="")
        aaa.add_field(name="Aulas",value="-aulas")
        aaa.add_field(name="Tarefas",value="-tarefas")
        aaa.add_field(name="Ajuda",value="-help")
        await message.channel.send(embed=aaa)

    if message.content.lower() == ("-aulas"):
        mensagem = await message.channel.send(":gear: **Recarregando aulas...**")
        aulas_list = get_aulas()
        def dia(x):
            msg = ""
            for i in range(len(aulas_list[x])):
                if i == 0:
                    msg = msg + aulas_list[x][i+1] +"\n"
                elif i > 1:
                    msg = msg + aulas_list[x][i] +"\n"
            return msg
        
        embed=discord.Embed(title="Calendário dos guri", url=login.link_calendario, description="") 
        embed.add_field(name=aulas_list[0][0], value=dia(0),inline=False)
        embed.add_field(name=aulas_list[1][0], value=dia(1),inline=False)
        embed.add_field(name=aulas_list[2][0], value=dia(2),inline=False)
        embed.add_field(name=aulas_list[3][0], value=dia(3),inline=False)
        embed.add_field(name=aulas_list[4][0], value=dia(4),inline=False)
        embed.add_field(name=aulas_list[5][0], value=dia(5),inline=False)
        embed.add_field(name=aulas_list[6][0], value=dia(6),inline=False)
        
        embed.set_footer(text="")
        await mensagem.delete()
        await message.channel.send(embed=embed)

    if message.content.lower() == ("-tarefas"):
        mensagem = await message.channel.send(":gear: **Recarregando tarefas...**")
        tarefas_list = get_tarefas()
        
        embed=discord.Embed(title="**Tarefas dos guri**", url="", description="")
        
        for x in tarefas_list:
            splited = x.split(" - ")
            embed.add_field(name=splited[0], value=splited[1], inline=False)
        
        await mensagem.delete()
        await message.channel.send(embed=embed)



client.run('TOKEN DO BOT')