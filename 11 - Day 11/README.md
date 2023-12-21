# DAY 11 - Description

## Description
### Message #1 (NPST):
````
Heisann alle sammen!

Det kom et bud innom med en pakke som vi ikke klarer å finne ut av. Budet la igjen en post-it lapp med 61d42b52b5334fe4f513c24c6da2a4251b069def05ae7c96a4152038c4b1f712 på og pakken er vedlagt i meldingen.

- 📞 Sentralbordet 
📎npst.zip
````

### Message #2:
````
NISSENS verksted har mottatt en mystisk melding og litt kode for å dekryptere meldingen. Noen alver i førstelinjen har sett på det, og blir ikke helt kloke. De mistenker at kun denne ene hemmeligheten ikke er nok. Kanskje er det andre som sitter på mer info?

- Mellomleder

📎 filer.zip
````

## Solution
Start by extracting your own secret, the zip file is password encrypted, so use the password from the post-it note.

Me as an NPST player got

```
Hemmelighet #1
980daad49738f76b80c8fafb0673ff1b
```

To complete this challange you need to find the other two secrets. And it has been sendt to other players. 
In the other departements KRIPOS and NSM. So you need to contact them and get the other two secrets.

```
hex_str1 = "a3c5a5a81ebc62c6144a9dc1ae5cce11"
hex_str2 = "980daad49738f76b80c8fafb0673ff1b"
hex_str3 = "fc78e6fee2138b798e1e51ed15e0a109"
```

After getting them all, we need to create a AES key. The key must be of a specific length, 
typically 16 bytes (128 bits), 24 bytes (192 bits), or 32 bytes (256 bits). 

The strings you appear to be hexadecimal representations, where each character represents 4 bits. They all
has 32 hexadecimal characters, which means it's 16 bytes long (128 bits).

The most common way to get a new key is to XOR it. So we XOR the three strings together.

```
# Function to XOR two hexadecimal strings
def xor_hex_strings(str1, str2):
    # Convert the hex strings to integers, XOR them, and then convert back to hex, padded with zeros if necessary
    xor_result = hex(int(str1, 16) ^ int(str2, 16))[2:].zfill(max(len(str1), len(str2)))
    return xor_result
```

### Flag
```
NSM{9c7cac722d55da1dbfa13025d85efeed45e9ddea2796c0e5ea2fda81ea4de17d}
```