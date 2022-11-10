from PIL import Image, ImageFont, ImageDraw

afbeelding = Image.open("meme_background.jpg")
lettertype = ImageFont.truetype("impact.ttf", 40)

# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(afbeelding)

# Tekst schrijven
tekst = "Lekkkahhh!"
tekengebied.multiline_text((60,130), tekst, font=lettertype, fill=(0,0,0))

# En opslaan onder een andere naam
afbeelding.save("meme_met_tekst.jpg")

# Het resultaat tonen
afbeelding.show()