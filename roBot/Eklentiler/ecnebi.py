# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, filters
from googletrans import Translator

cevirici = Translator()

from roBot._edevat import logYolla

@Client.on_message(filters.command(['ingilizce'], ['!','.','/']) & filters.me)
async def ingilizce(client, message):
    # < Başlangıç    
    cevaplanan_mesaj    = message.reply_to_message
    if cevaplanan_mesaj is None:
        yanitlanacak_mesaj  = message.message_id
    else:
        yanitlanacak_mesaj = cevaplanan_mesaj.message_id
    
    ilk_mesaj = await message.edit("__Bekleyin..__",
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    girilen_yazi = message.text
    if not cevaplanan_mesaj and len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("__Çeviri yapabilmem için bişeyler söyleyin ya da mesaj yanıtlayın..__")
        return

    if not cevaplanan_mesaj:
        girdi = girilen_yazi.split(" ", 1)[1]
    
    elif cevaplanan_mesaj and cevaplanan_mesaj.document:
        gelen_dosya = await cevaplanan_mesaj.download()
        
        veri_listesi = None
        with open(gelen_dosya, "rb") as oku:
            veri_listesi = oku.readlines()
        
        inen_veri = ""
        for veri in veri_listesi:
            inen_veri += veri.decode("UTF-8")
        
        girdi = inen_veri

        os.remove(gelen_dosya)
    
    elif cevaplanan_mesaj.text:
        girdi = cevaplanan_mesaj.text
    else:
        await ilk_mesaj.edit("__güldük__")
        return
    
    await ilk_mesaj.edit("Çevriliyor...")

    if cevirici.detect(girdi).lang != 'en':
        await ilk_mesaj.edit("ingilizce konuş davar.!")
        return
    
    cevrilmis_mesaj = cevirici.translate(girdi, dest='tr').text

    await ilk_mesaj.edit(f'__{cevrilmis_mesaj}__')
    await logYolla(client, message)

@Client.on_message(filters.command(['türkçe'], ['!','.','/']) & filters.me)
async def türkçe(client, message):
    # < Başlangıç    
    cevaplanan_mesaj    = message.reply_to_message
    if cevaplanan_mesaj is None:
        yanitlanacak_mesaj  = message.message_id
    else:
        yanitlanacak_mesaj = cevaplanan_mesaj.message_id
    
    ilk_mesaj = await message.edit("__Bekleyin..__",
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    girilen_yazi = message.text
    if not cevaplanan_mesaj and len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("__Çeviri yapabilmem için bişeyler söyleyin ya da mesaj yanıtlayın..__")
        return

    if not cevaplanan_mesaj:
        girdi = girilen_yazi.split(" ", 1)[1]
    
    elif cevaplanan_mesaj and cevaplanan_mesaj.document:
        gelen_dosya = await cevaplanan_mesaj.download()
        
        veri_listesi = None
        with open(gelen_dosya, "rb") as oku:
            veri_listesi = oku.readlines()
        
        inen_veri = ""
        for veri in veri_listesi:
            inen_veri += veri.decode("UTF-8")
        
        girdi = inen_veri

        os.remove(gelen_dosya)
    
    elif cevaplanan_mesaj.text:
        girdi = cevaplanan_mesaj.text
    else:
        await ilk_mesaj.edit("__güldük__")
        return

    if cevirici.detect(girdi).lang != 'tr':
        await ilk_mesaj.edit("türkçe konuş davar.!")
        return
    
    cevrilmis_mesaj = cevirici.translate(girdi, dest='en').text

    await ilk_mesaj.edit(f'__{cevrilmis_mesaj}__')
    await logYolla(client, message)


from roBot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "komut"        : "ingilizce/türkçe",
        "aciklama"     : "Türkçe/İngilizce veya İngilizce/Türkçe çeviri yapmanıza olanak tanır.",
        "parametreler" : [
            "Yanıtlanan Mesaj",
            "Yanıtlanan Dosya",
            "Metin"
            ],
        "ornekler"     : [
            None
            ]
    }
})