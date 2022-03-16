---
permalink: /docs/datenbank/
layout: default
---

## Die Datenbank
### Daten

Bisher gibt es lediglich eine Tabelle zu Kreaturen, an der noch gearbeitet wird. 

[Mehr Infos zur Kreaturen DB](/docs/db/kreaturen)

[Vorschau der Einträge](/db/kreaturen)

> TODO: links mit jekyll generieren


### Struktur
Der Kern der Informationen sind die einfach zu handhabenden yaml-Dateien im Ordner `Daten` sein. Jede Datei kann dabei als eine Art Tabelle verstanden werden, in denen Inhaltlich ähnlich aufgebaute Objekte gespeichert werden. Zum Beispiel `vorteile.yaml` oder `kreaturen.yaml`. Die Dateien sollen dabei lose verknüpft sein, das heisst, in den Vorteilen einer Kreatur beispielsweise, kann eine `id` (einzigartiges Wort ohne Sonderzeichen) hinterlegt werden über die Details zum jeweiligen voteil aus einer anderen Datei ausgelesen werden. Idee der losen Kopplung ist, dass sich jeder nur das herauspicken kann, was er/sie braucht ohne dabei auf eine aktuelle konsistente und vollständige Datenbank achten zu müssen. 


#### Schemata
Zu jeder Tabelle bzw. jeder Klasse liegt ein Schema im Ordner `schemata` vor. Diese Dateien definieren die Struktur der jeweiligen Klasse und können benutzt werden um die Daten nach neuen Einträgen oder Änderungen zu überprüfen. 


## Begriffe und Abkürzungen
Ich habe ein paar zusätzliche Abkürzungen und Felder verwendet um besimte Dinge feiner aufzusplitten, bzw. eindeutige Datentypen zuweisen zu können (zB. TP `2W6+4` teilt sich auf in TPW: `2` und TPP: `4`). Hier ist eine Liste die ich versuche aktuell zu halten:

* `GSF` Geschwindigkeit (fliegend)
* `GSR` Geschwindigkeit (reitend)
* `GSS` Geschwindigkeit (schwimmend)
* `RWM` Minimale Reichweite, wenn ein Bereich als RW angegeben ist
* `TPP` TP Plus.. der Wert der zum Würfel addiert wird.
* `TPW` Die Anzahl W6 für TP Wurf
* `TPW20` Anzahl W20 (nicht kombinierbar mit `TPW`)
* `WSE` Effektive Wundsschwelle (WS*)
* `WSS` Spezielle Wundschwelle als Text (in kombination mit WS=-1)