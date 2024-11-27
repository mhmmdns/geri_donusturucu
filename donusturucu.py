import discord
from discord.ext import commands

# Botu başlatmak için gerekli bilgiler
intents = discord.Intents.default() # İzinler için
intents.messages = True  # Botun mesajları görebilmesi için gerekli
intents.message_content = True # Mesaj okuma izni

# Botun Prefix'i
bot = commands.Bot(command_prefix='?', intents=intents)# Komut ön eki
        
# Bot hazır olduğunda çalışan event
@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} olarak giriş yaptı.')

# Selamlama komutu
@bot.command()
async def selam(ctx):
    await ctx.send("Merhaba! Ben geri dönüşüm botuyum. (?geri_dönüşüm_modu) komutuyla geri dönüşüm moduna geçebilirsin.")

# Geri dönüşüm modu
@bot.command()
async def geri_dönüşüm_modu(ctx):
    await ctx.send("Geri dönüşüm moduna hoş geldin! Bana mutfak artığını yaz ve geri dönüştürülebilir mi diye kontrol edeyim.")
    await ctx.send("Örnek: `yumurta kabuğu`, `karton bardak`")
    await ctx.send("Geri dönüşüm modundan çıkmak için `çıkış` yazabilirsin.")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel


    while True: #Sürekli Mesaj Bekleme
        msg = await bot.wait_for('message', check=check)  # Zaman aşımı olmadan sürekli mesaj bekliyor ve filtre uyguluyor.
        item = msg.content.lower() #Gönderilen mesaj küçük harfe çevrilerek, karşılaştırma işlemlerinde tutarlılık sağlanır.

        if item in ["plastik atıklar", "metal atıklar", "kağıt atıkları"]: # a,b ve c harfleri yerine geri dönüştürülebilen atıkları yazın.
            await ctx.send(f"'{item}' geri dönüştürülebilir! ♻️")
        elif item in ["x", "y", "z"]: # x,y ve z harfleri yerine geri dönüştürülemeyen atıkları yazın.
            await ctx.send(f"'{item}' geri dönüştürülemez! 🚫")
        elif item == "çıkış":
            await ctx.send("Geri dönüşüm modundan çıkılıyor. Görüşürüz!")
            break
        else:
            await ctx.send(f"'{item}' hakkında bilgim yok. Lütfen başka bir atık deneyin.")

# Botu başlatıyoruz
bot.run('Buraya kendi tokenınızı yazın')
