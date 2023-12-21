# DAY 10 - Sorting

## Description
````
De strenge alvene har skrevet ned et julekodeord, men i den ivrige 
sorteringen av pakker har det skjedd en horribel feil og alt er blitt rot! 
Ordet har blitt borte i det som ser ut som et virrvarr av tilfeldig tekst! 
Nå trenger de hjelp til å gjenfinne ordet. De har null peiling på hvor langt ordet er. 
Kan du å gjenfinne ordet?

- Mellomleder
````

## Solution
When you open the document it is very messy. My first task was to search for somthing with the flag.
I search for PST, {, }, KRIPOS and NSM. I found that { and } was first in place in the strings.

I then dived each line by null byte. And then though maybe since it is sorting, we have something
to do with the length of strings. So I added this to the program and print.
I found out that there where over 10000 lines. But } had max chars of 80 and { had max chars of 20.
So I though maybe then we do not need the strings that have more than 20 chars.

So I printed out only the ones. And it wasent to much. Then I though how about we sort this by length.
And then I found the flag.


### Flag
```
PST{julenisseStreng0Alv}
```