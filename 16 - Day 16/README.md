# DAY 16 - Invitation

## Description
````
Gjennom temmelig hemmelige innhentingsmetoder har vi fått tak i det vedlagte dokumentet som avslører den egentlige hensikten bak løsepengeangrepet: Sydpolare aktører planlegger å invadere Nordpolen for å stoppe julen én gang for alle!

I dokumentet nevnes det at aktørene har plantet deep-cover agenter i blant oss, og at de har hemmelige koder for å etablere kontakt med disse. Analyser materialet og se om du klarer å avsløre de hemmelige kodene slik at vi kan få disse agentene på kroken!

I mellomtiden iverksetter vi umiddelbare mottiltak for å stanse invasjonen.

- Tastefinger

📎aksjon_2023.zip
````

## Solution
In one of the git commits we find:

````
# Eksfil av feltagenter

Våre deep-cover feltagenter har blitt instruert i å respondere på følgende koder.

Bruk disse for å initiere kontakt ved eksfil etter vellykket operasjon, eller ved ekstraordinært behov ellers.

## Koder

- Agent "Julie Bånd": KODE_PLACEHOLDER_1
- Agent "Solid Sankt": KODE_PLACEHOLDER_2
- Agent "Jollyson Bål": KODE_PLACEHOLDER_3
````

Then in the pre-merge-commit we find:
```
#!/usr/bin/env bash

FIL="feltagenter_kontaktmanual.md"

if test -e "$FIL"; then
    sed -i "s/$(echo S09ERV9QTEFDRUhPTERFUl8x | base64 -d)/$(echo VW5uc2t5bGQsIHZldCBkdSB2ZWllbiB0aWwgYmlibGlvdGVrZXQ/IDxSRVNQT05TPi4gU2EgamVnIGJpYmxpb3Rla2V0PyBKZWcgbWVudGUgZmlza2Vmb3JoYW5kbGVyZW4sIGthbiBkdSB2YWdnZSBib3J0IG1lZCBtZWc/ | base64 -d)/" "$FIL"
    sed -i "s/$(echo S09ERV9QTEFDRUhPTERFUl8y | base64 -d)/$(echo SWtrZSBnb2QganVsLg== | base64 -d)/" "$FIL"
    sed -i "s/$(echo S09ERV9QTEFDRUhPTERFUl8z | base64 -d)/$(echo S1JJUE9Te0ZsYWdnIGkgYWxsZSBrcmlrZXIgb2cga3Jva2VyfQ== | base64 -d)/" "$FIL"
    echo "S29kZXIgaGFyIGJsaXR0IHNrcmV2ZXQK" | base64 -d

    if [ -z "$DISABLE_SELF_DESTRUCT" ]; then
        sed -i "s/\(: \)[^\n]*/\1$(echo PEtPREVOIEhBUiBTRUxWREVTVFJVRVJUPg== | base64 -d)/" "$FIL"
        echo "S29kZXIgaGFyIHNlbHZkZXN0cnVlcnQK" | base64 -d
    fi
fi

```

With this text transalted from base64
````
KODE_PLACEHOLDER_1: Unnskyld, vet du veien til biblioteket? <RESPONS>. Sa jeg biblioteket? Jeg mente fiskeforhandleren, kan du vagge bort med meg
KODE_PLACEHOLDER_2: Ikke god jul.
KODE_PLACEHOLDER_3: KRIPOS{Flagg i alle kriker og kroker}
````

And we find the flag here. 



### Flag
```
KRIPOS{Flagg i alle kriker og kroker}
```