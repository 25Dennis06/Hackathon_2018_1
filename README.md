# Hackathon_2018_1

Anbei findest du unser sehr einfaches Python-Skript.
Wir haben uns dabei stark an foglendes Youtube-Tutorial gehalten (Teile 1-3)
https://www.youtube.com/watch?v=DFiCsMcipr4&t=636s

Der prinzipielle Aufbau ist dabei so, dass man über der Alexa-Entwicklerseite sogenannte "Intents" definiert. Diese Intents sind Sätze oder Satzbauteile und deren Synonyme, die man definiert. Also man kann z.B. den Intent "ThanksIntent" definieren und dazu die Synonyme
Vielen Dank
Danke
Dankeschön
Danke Alexa
Vielen lieben Dank
...

Findet Alexa dann einen von diesen Satzteilen, wird der entsprechende Response ausgegeben. Dieser wird in unserem Fall über Python geregelt. In unserem Fall gibt Alexa als Rückmeldung "Bitteschön" (als Frage/Question, damit weitere eingaben erfolgen können. Würde man es als statement zurückgeben, würde Alexa nicht weiter zuhören (so habe ich es zumindest verstanden)).

Ansonsten kann man in den Intents noch diverse Platzhalter (ich glaube sie hießen "Slots"?) einfügen. Wir haben dies z.B. bei der Suchanfrage gemacht. So war die Suchanfrage z.B. definiert über "Suche mir ein {Filter} {Produkt}."
Die Werte für die Platzhalter müssen aber ebenfalls vorher definiert werden. Also z.B. für {Filter} "Blau, Rot, Grün, ..." und für {Produkt} "Schuhe, Anzug, Hose, Kamm, ...". Man kann diese sicherlich auch irgendwie über Python direkt einstellen, wir haben diese aber wie oben bereits erwähnt direkt in die Alexa-Website eingebunden. 
