# Introduksjon til tokens (Norsk)

## Token
Det er tre typer token:
* Access token / tilgangstoken
* Refresh token
* ID token

**Access token / tilgangstoken**
Gir applikasjonen tilgang til å agere på vegne av brukeren

**Refresh token**
Brukes for å fornye access tokens. I praksis en erstatning for brukerens brukernavn og passord

**ID token**
Grunnleggende informasjon om brukeren

## Hvordan dette fungerer i praksis
Et access token kan ha kort levetid (f.eks. 5 min) og er det som sier om en bruker er logget inn eller ikke. Når levetiden til et access token har utløpt, må applikasjonen / klienten spørre identitetsløsningen om å få et nytt. 

For at brukeren skal slippe å skrive brukernavn/passord hvert 5. min, brukes et refresh token i stedet. Denne utvekslingen skjer hele tiden uten at brukeren merker stort til det. 

I teorien kan denne fornyingen av access token skje et uendelig antall ganger. 

I praksis er det satt en absolutt maksimal levetid på et refresh token, som gjør at brukeren må autentiseres på nytt når den absolutte levetiden er nådd. 

I tillegg er det begrensninger på refresh tokens, slik at hver gang en applikasjon / klient ber om et nytt access token, så utstedes det også et nytt refresh token (rotering av refresh token). Et refresh token erstatter brukernavn og passord for brukeren, og det er kritisk viktig at dette holdes skjult og godt sikret av applikasjonen / klienten. 

Det å utstede nytt access token skjer, som nevnt, uten at brukeren merker noe til det gitt at refresh tokenet fremdeles er gyldig. Dersom refresh tokenet blir ugyldig eller utstedingen feiler, vil brukeren bli sendt til  login.coop.no. Hvis brukeren har en gyldig cookie fra login.coop.no, vil identitetsløsningen utstede et nytt access og refresh token uten at brukeren må skrive inn brukernavn og passord på nytt. 
