# DAY 3 - Santa's Ransomware

## Description
````
Det er krise! Filene på alvemaskinene har blitt kryptert, og vi har ingen backups tilgjengelig!

På nissens skrivebord fant vi det vedlagte brevet, sammen med en kryptert fil.

Det er ubeskrivelig viktig at vi får åpnet denne filen igjen umiddelbart, da Jule NISSEN ikke klarer å huske innholdet!

- Mellomleder

📎 Mitt utpressingsbrev.docx
📎 huskeliste.txt.enc
````

## Solution

Open the DOC and get the encryption key: ``dda2846b010a6185b5e76aca4144069f88dc7a6ba49bf128``

The key has 48 hexadecimal characters. Thus, the size of the key in bits is
48
×
4
=
192
48×4=192 bits, not 24 bits. This size suggests that the encryption algorithm used is likely AES-192, a variant of the Advanced Encryption Standard (AES) that uses a 192-bit key.

AES is a widely used symmetric encryption standard and supports three key sizes: 128, 192, and 256 bits. Since your key fits the 192-bit size, it's a strong indication that AES-192 may have been used. AES is commonly used in various applications due to its balance of speed and security.

You also find the IV: UtgangsVektor123
In the image you can see there is something there to the left. So if you right click and use crop,
you can see that the image have been cropped. And you are able to get more information by dragging that out.

It tells you that the encryption is AES-CTR and the IV also is ROT13 encrypted.
So using the new IV: HgtnatfIrxgbe123 you get this text.

The decryption was done using CyberChef:

### CyberChef
````
https://gchq.github.io/CyberChef/#recipe=AES_Decrypt(%7B'option':'Hex','string':'dda2846b010a6185b5e76aca4144069f88dc7a6ba49bf128'%7D,%7B'option':'UTF8','string':'HgtnatfIrxgbe123'%7D,'CTR','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=qlRpqmM%2ByENV/QMGV1OEnBGZf1Uezculf6vNDdxITIN/jbQ4qJn0RXmkrcxhELGStNunjs6Vl%2By94XIN8n4k/URJy/rIPTbSx81NoubCFPOxOh/woMEli4spXmu2If4e4Gy2VsV9iJ2UgPhb0nMpLlsnYgzAtWeeIqceWwbBVONGMhV%2BWECs2EeYwKxDnyxz6cJ1OEY1Ts%2B6wgrDLvoPtjuYdAhh/BT7TLu3q9L6ZCxwN2Zb%2BIpqefQz552AjTYgDHzSML2jSno4PW4LGBREDYjClO4lJtY2wMx/1BxNrD89XmiZFqxh0/13jw41X0arjHCm5xKE0vgoS1fP3uj9zuXm4KkVCOUrpjAL0GZ2hl3wfJPOsvY8d2MQzA
````

### Text
```
Nissing 101:

Snille barn: Morosaker, spenstigheter og snurrepiperier
Slemme barn: Ukomprimerte diamanter
Nissebetjenter: Flagg

Forslag til morosaker, spenstigheter og snurrepiperier:
Dukker
Lekebiler
Sokker

Forslag til flagg:
Norsk
Nordpolsk
KRIPOS{Husk å se etter spor i snøen!}
```



### Flag
```
KRIPOS{Husk å se etter spor i snøen!}
```