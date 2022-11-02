from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


şablon1="""<?xml version="1.0" encoding="utf-8"?>
<base xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" type="string">
  <tags>
    <tag language="English" />
  </tags>
  <strings>
"""

şablon2=""

şablon3="""  </strings>
</base>
"""

with open("sta_strings.xml","r",encoding="utf-8") as file:
    reading=file.read()
    bs=BeautifulSoup(reading,"html.parser")
    for i in bs.find_all("string"):
        try:
            kardiz=GoogleTranslator(source="auto", target="tr").translate(i["text"])
            liste=[]
            kardiz.lower()
            for kelime in kardiz.split():
                if kelime.startswith("i"):
                    kelime = "İ" + kelime[1:]
                kelime = kelime.title()
                liste.append(kelime.title())
            i["text"]=" ".join(liste)
            şablon2+=f"    {i}\n"
            print(i)
        except:
            continue

with open("sablon.txt","a",encoding="utf-8") as file:
    file.write(şablon1)
    file.write(şablon2)
    file.write(şablon3)

print("\n\nİşlem Bitti.")

