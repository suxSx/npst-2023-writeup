# DAY 2 - Rubix cube

## Description
````
Message #1:
Over natten har det vært store utfordringer knyttet til en av maskinene i verkstedet. En serie feilproduserte leker har kommet på rullende bånd. Vi prøver å finne ut hva som har skjedd. Graver du ned i det her?

- Mellomleder

📎Bilde

Bra, jeg videresender til bitBug!

- Mellomleder

Message #2:

Fra: Tastefinger
Til: Mellomleder
Emne: FW: Scrambled

Tror det var noe skitt på linsa da det forrige bildet ble tatt, så jeg har tatt et nytt et. Har lagt med som vedlegg.

- Tastefinger

📎 oedelagte_leker_fix.png
````

## Solution
It is a rubix cube. Solo solve it and you get the flag.

```
B: _ D T Ø { E U L S
G: _ S M P P L S U E 
Y: : U B ? ) K } E _
O: _ L L R E L E I L
R: O S T P E B G Y R
W: _ E D S N E O _ N 
```

### Rubix cube flat
```
                    B:_ G:_ Y::
                    O:_ R:O G:S
                    Y:U R:S G:M
                    
      O:L B:D G:P   O:R W:D R:R  W:E O:L B:{
      Y:B B:T O:L   W:S W:N Y:?  G:L G:S B:E
      W:_ W:E B:Ø   R:P O:E G:P  R:W Y:) W:O
      
                    W:_ Y:K Y:}
                    G:U O:E R:B
                    O:I R:G O:L
                    
                    B:U B:L G:E
                    B:S Y:E W:N
                    Y:_ R:Y R:R  

```

### Rubix cube flat solved 
```
            R B M
            G O Y
            P S T
            
    { L Ø   _ D E  M _ P
    S T E   N N E  U S L
    _ D U   _ S O  E S P
            
            I L L
            _ E L
            L E R
            
            _ K U
            B E ?
            : ) }  
```

### Flag
```
PST{LØSTE_DU_DENNE_SOM_PUSLESPILL_ELLER_KUBE?:)}
```