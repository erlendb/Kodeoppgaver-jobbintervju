# Kodeoppgaver i forbindelse med jobbintervju

Til glede for dem som lurer på hva i alle dager man egentlig gjør på en "teknisk test".

## Ardoq

> Before we move into interviews we have a couple of technical tasks we'd like you to look at. The first task is mandatory, but you can choose either one of 2 or 3. I hope you find it an interesting and fun challenge and get back to me with your answers soon.
>
>1: Create a function that, given a list of integers, returns the highest product between three of those numbers. For example, given the list [1, 10, 2, 6, 5, 3] the highest product would be 10 * 6 * 5 = 300
>
>2: Oslo city bikes has an open API showing real-time data on location and state of the bike stations.
>Your task is to create a small application that utilizes this api to show the stations and the amount of available bikes and free spots a station currently has. You’re free to choose which language and libraries you use. How you show the stations and status is also up to you.
>The api can be found at  [https://oslobysykkel.no/apne-d…](https://oslobysykkel.no/apne-data/sanntid) 
>
>3: Oslo city bikes have an open API with historical data.
>Your task is to create a project and use this data and provide some interesting findings. This can be anything from data preprocessing, data analysis, data visualizations, or applying machine learning in any way you see fit. The most important is that you have a story to tell with the data.
>The API can be found at  [https://oslobysykkel.no/apne-d…](https://oslobysykkel.no/apne-data/historisk) 
>
>We prefer if you deliver the task as an open GitHub repo and just send us the link.
>
> &mdash; Ardoq

Løsningen jeg leverte ligger [her](ardoq).

En av oppgavene var å finne det største mulige produktet man kan få av å gange sammen tre tall, gitt en liste med tall.

> Supert. Hvis jeg sier at det er noen mangler ved algoritmen din, har du noen tanker om hva det kan være? &mdash; Ardoq

Eeeeh, nei? Hallo, jeg har jo gjort det riktig? Etter sju e-poster fram og tilbake med Ardoq innså jeg at jeg hadde forenklet litt vel mye. I min verden var det åpenbart at man fant det største produktet av tre tall ved å gange sammen de tre største tallene i lista. I etterkant viste det seg at produktet av to negative tall blir positivt. For eksempel illustrerer denne lista problemet: `[1, 2, -3, 4, 5, -7]`.

> Hei,
>
> Vi setter stor pris på interessen din for Ardoq og tiden du har investert for å søknaden.
>
> Vi har kommet frem til at vi dessverre ikke tar deg videre i prosessen nå. Du har masse engasjement og driv og leverte en bra oppgave, men vi har fått inn veldig mange søkere og konkurransen ble stor.
>
> Jeg ønsker deg lykke til videre og håper vi snakkes igjen ved en senere anledning
>
> &mdash; Ardoq

## Capra
Den tekniske testen hos Capra foregikk på intervjuet. Intervjuet foregikk over Teams. Det var først litt vanlig intervjubabling, og så en halvtimes tid med kodeoppgaver. Jeg fikk beskjed om å tenke høyt og dele skjerm, sånn at de kunne se hvordan jeg løste oppgaven (og hva jeg googlet underveis heheh). Jeg fikk 8 minutter på å løse hver oppgave, og rett etter hver oppgave diskuterte vi litt hva, hvorfor, hvordan og andre måter det kunne vært løst på.

[Lenke til løysinga](capra).

>Hei, Erlend!
>
>(...)
>
>Du gjorde et godt inntrykk under kodekataen. I tillegg til å løse oppgavene med gode resultater, kom du med fine refleksjoner rundt alternative løsninger underveis. Vi håper at du tar med prestasjonen som erfaring til lignende situasjoner senere i utviklerkarrieren.
>
>Lykke til videre i jakten på sommerjobb!
>
> &mdash; Capra

## Knowit
>Vi ønsker at du gjennomfører en hjemmeoppgave i grunnleggende Java-programmering, som vil ta 1,5 time. Svar på denne eposten og oppgi en dato og et klokkeslett som passer for deg, så sender vi deg oppgaven på det tidspunktet.
>
>Du løser oppgaven i Java, og etter halvannen time sender du oss besvarelse i form av kildekode for løsning og tester. Vi retter oppgaven og gir deg tilbakemelding på koden, og resultatet går inn i evalueringsgrunnlaget vårt. Det kan også hende vi sender deg noen oppfølgingsspørsmål (uten tidsfrist) etter at vi har fått besvarelsen.

>Oppgaven er en liten kravspesifikasjon du skal implementere - den krever kun bruk av Java og språkets standardbiblioteker. Du kan bruke et bibliotek for enhetstesting (f.eks. JUnit) dersom du ønsker det. Andre 3.-parts biblioteker/rammeverk skal ikke benyttes. Det blir IKKE nødvendig å skrive noen form for brukerinteraksjon eller lagring til disk.
>
>Vi anbefaler at du setter opp utviklingsmiljø på forhånd, et IDE som intellij eller eclipse bør være tilstrekkelig. Vi anbefaler også at du sørger for å ha arbeidsro under oppgaveperioden.

>Her er oppgaven vi ønsker at du utfører. Lever ved å sende oss kildekodefilene på epost (svar gjerne på denne meldingen), senest om 1,5 timer.
>
>Det er fullt mulig å få godkjent oppgaven selv om du ikke rekker alt, så ikke stress! ;-) Hvis du går tom for tid, lever det du har. Ikke gå over fristen.
>
>Oppgaven skal løses i Java. Koden du lager bør være testet, enten med et testrammeverk som f.eks. JUnit eller ved at du skriver et lite program som tester koden din. Du har antagelig ikke tid til å teste alt, men vi krever at i hvertfall noe av funksjonaliteten er testet. Testene skal også leveres.
>
>OBS: Det er ikke meningen at du skal lage noe brukergrensesnitt i denne oppgaven. Trenger du data i testene dine, så hardkod disse dataene i testene. Det er heller ikke meningen at du skal persistere data til disk eller database - hold dataene i standard Java-datastrukturer.
>
>Oppgaven:
>
>Du skal lage kjernen i et system som skal holde styr på alle faggruppene til Knowit og deres planlagte arrangementer. Andre utviklere skal lage brukergrensesnittet, som skal brukes av Knowits ansatte for å registrere nye grupper og legge til planlagte arrangementer.
>
>For hver faggruppe skal programmet kunne lagre ID, navn, type og en liste over alle planlagte arrangementer. En faggruppe kan være av typen Chapter (holder foredrag) Guild (holder workshops/kodekvelder) eller Playground (lavterskel gruppe uten krav om å holde arrangementer).
>For hvert arrangement skal programmet kunne lagre beskrivelse, dato og maks antall personer som kan delta.
>Funksjonalitetskrav 1: Registrering og uthenting
>
>Lag en metode som registrerer en faggruppe i systemet. Ta navn og type som parametere. Faggruppens ID bør genereres av systemet.
>Lag en metode for å registrere et nytt arrangement for en faggruppe. Ta faggruppens id samt arrangementets beskrivelse, dato og maks antall personer som parametere.
>Lag en metode som henter ut alle registrerte arrangementer for en faggruppe. Bruk faggruppens ID som parameter.
>Funksjonalitetskrav 2: Beregning
>
>Lag en metode som henter ut alle faggrupper av typen Playground.
>Lag en metode som regner ut hvor mange faggrupper som har hatt, eller skal ha, minst ett arrangement hvor det var plass til minst 10 deltagere.
>Lag en metode som henter ut en sortert liste av alle kommende arrangementer for en faggruppe. Listen skal sorteres på dato, fra førstkommende arrangement og til den siste. Bruk faggruppens ID som parameter.
>Funksjonalitetskrav 3: Feilhåndtering
>Når det oppstår problemer i systemet, f.eks. hvis det forsøkes å opprette et arrangement med en dato i fortiden eller om det blir prøvd å opprette et arrangement til en faggruppe som ikke finnes, så skal dette behandles fornuftig.
>
> &mdash; Knowit

Jeg kan ikke Java, så jeg tok sjansen på å implementere [løsningen min](knowit) i Python.

>Det ser ut som om du har levert en grei besvarelse i Python. Dessverre er ikke Python blant språkene vi bruker i utstrakt nok grad til at vi godtar besvarelser i det i jobbsøkerprosessen, og jeg må derfor gi deg avslag på søknaden din. 
>
>For evaluering til sommerjobb godtar vi kun besvarelser i Java. For fastjobb vil vi også kunne vurdere Kotlin, Scala, Python, C#, JavaScript, TypeScript og Swift. Begrensningen til Java for sommerjobb-søknader er fordi Java er det språket vi nærmest kan garantere relevant prosjektplass for - og når man bare er noen få uker hos oss er det best at mest mulig forkunnskaper er på plass før man begynner, det er nok annet å sette seg inn i. (Det betyr ikke at alle våre sommerstudenter faktisk koder Java - om noen også har kompetanse på andre teknologier og det viser seg at det er behov for det når sommeren kommer, kan man få oppgaver i andre språk. Men det klarer vi ikke forutse på nåværende tidspunkt.) At Python heller ikke er interessant med tanke på fastjobb kommer av at det kun benyttes i relativt enkle scripteoppgaver hos våre kunder, og vi ønsker at våre faste konsulenter demonstrerer dybdekunnskap om språkene de faktisk skal jobbe med.
>
>Hvis du i fremtiden opparbeider deg kompetanse på Java (mtp sommerjobb) eller et av de andre språkene vi ønsker oss (mtp fast stilling) oppfordrer vi deg til å søke jobb hos oss på nytt på det tidspunktet.  
>
>Vi takker for interesse og innsats, og ønsker deg lykke til videre med sommerjobbsøknaden for neste år!
>
> &mdash; Knowit

## Progit

>Sender som avtalt over oppgaveteksten, denne finnes her:
>https://github.com/progitas/neste-sommer-2021
>
>Oppgaven kan løses i de fleste programmeringsspråk, dersom språket du velger ikke har mulighet til å hente data fra et API, hardkod responsen fra API-et inn i en variabel som brukes for å løse oppgaven.
>
>Minner om at en zippet fil med koden må sendes til oss innen 2 timer etter at mailen er mottatt. Gjør så mye du klarer og hvis du går tom for tid kan det være greit å inkludere en kort forklaring på hva du ville gjort med det som eventuelt gjenstår. Det er også fint om du legger ved et lite skjermbilde av resultatet du kommer fram til.
>
> &mdash; Progit

[Her](progit) ligger løsningen min.

>Basert på søknaden og besvarelsen din vil vi gjerne invitere til en prat den kommende uken. &mdash; Progit

Og så var jeg på intervju. Og så sluttet de å svare. Ukult.

## Vipps

> (...)
>
>Se hjemmeoppgave nedenfor. Vi tror ikke du bruker mer enn rundt 20min på å løse oppgaven i forkant av intervjuet - husk å sende den til oss senest kl 12 dagen før intervjuet. Under intervjuet diskuterer hvordan du har valgt å løse oppgaven og begrunnelse for det.
>
>Home assignment:
>
>Submit this before 12:00 the day before the interview.
>
>Part 1: Backend
>Using an HTTP GET method, retrieve information from Wikipedia using a given topic. Query https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=[topic] to get the topic Wikipedia article.
>Print the total number of times that the string [topic] appears in the article's text field.
>
>Part 2: Frontend
>Expose your backend code as an API and write a frontend that calls that API. The frontend can be very simple- just an input field and some way to submit and display the results. Feel free to be creative.
>
> &mdash; Vipps

"Vi tror ikke du bruker mer enn rundt 20min". Veeel, brukte en del mer tid enn det.

[Her](vipps) er ei lenke som fører deg til besvarelsen min.

> "Eeeeh, når jeg kjører api/api.py sånn som det står i readme så får jeg noe sånn derre 'Error: module requests not found', hva betyr det?" &mdash; Vipps

Poenget hans var at Readme-en manglet en oversikt over "requirements" og en forklaring på hvordan man installerer nødvendige pakker.

> "Hei, har du lyst på jobb hos oss?" &mdash; Vipps