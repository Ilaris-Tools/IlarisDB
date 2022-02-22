# IlarisDB
Sammelstelle für strukturierte Ilaris Daten, wie Kreaturen, NSCs, Zauber usw..

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

## Die Datenbank
Wir haben vorerst davon abgesehen eine "echte" Datenbank zu erstellen, da sich strukturierte Textdateien vorerst einfacher handhaben lassen und nicht verloren gehen falls das Projekt einschläft. Das Ziel ist hier Daten rund um das Ilaris Regelsystem strukturiert zu sammeln, sodass sie von anderen Tools genutzt werden können. Mit einfachen Scripten könnten zum Beispiel Tokens für VTTs oder Monsterboxen für das Latex-Template generiert werden. 

### Struktur
Der Kern der Informationen sind die einfach zu handhabenden yaml-Dateien im Ordner `Daten` sein. Jede Datei kann dabei als eine Art Tabelle verstanden werden, in denen Inhaltlich ähnlich aufgebaute Objekte gespeichert werden. Zum Beispiel `vorteile.yaml` oder `kreaturen.yaml`. Die Dateien sollen dabei lose verknüpft sein, das heisst, in den Vorteilen einer Kreatur beispielsweise, kann eine `id` (einzigartiges Wort ohne Sonderzeichen) hinterlegt werden über die Details zum jeweiligen voteil aus einer anderen Datei ausgelesen werden. Idee der losen Kopplung ist, dass sich jeder nur das herauspicken kann, was er/sie braucht ohne dabei auf eine aktuelle konsistente und vollständige Datenbank achten zu müssen. 

#### Schema
TODO: 


## Daten

### Kreaturen
Da Kreaturen, für Abenteuer (IlarisTex) und zum Spielen (FoundryVTT) gebraucht werden und sich die Werte aus den Bestarien und Regelwikis für DSA1-5 nicht direkt verwenden lassen, ist hier warscheinlich der Nutzen am größten. Daher wird dies der erste Teil des Projekts.

#### Erforderliche Daten

* `id:` sowohl der 'rootlevelkey' sollte die id sein, als auch ein feld der kreatur (dies ist eine der wenigen redundanzen).
* `name:` da die id oft nicht hübsch oder unleserlich ist, sollte es immer eine gut lesbare bezeichnung geben.
* `beschreibung:` Die Kreatur in einem Satz, gerade für Namen, die vielleicht weniger bekannt sind, ist dieses Feld wichtig.
* `quelle:` Für Credits und Nachvollziehbarkeit, gehört hier die id vom entsprechenden Eintrag in `quellen.yaml` rein.

#### Optionale Daten
Folgende Felder sind optional, aber typisch für die meisten Kreaturen. Für die vollständige Liste von Feldern ist ein Blick ins Schema nötig.
Einige Felder treten oft in Kombination bzw. als Gruppe auf zB alles was nur für Magisch begabte Wesen relevant ist. Diese Felder wurden auch für die Datenstruktur gruppiert.

* `info:` Ein ausführlicherer Text in dem Besonderheiten oder Anmerkungen für Spielleiterinnen zu dieser Kreatur stehen.
* `vorteile:` Allgemeine Vorteile, die gestaffelten stehen in den jeweiligen gruppen.
* `attribute:` Sollte klar sein. Aktuell hardgecoded, könnte irgendwann abstrahiert werden.
* `kampf:` Diesen Block hat warscheinlich so ziemlich jede Kreatur
* * `werte:` WS, WSE, GS, INI, MR usw. sind für Kreaturen fix und werden nicht aus Attributen errechnet.
* * `waffen:` Eine liste von waffen, die jeweils `name`, `AT`, `VT`, `TP` usw enthalten können oder auf die Waffentabelle verweisen (siehe waffen schema).
* * `vorteile:` Kampfvorteile
* `profan:` TODO: macht dieser Block sinn? oder zuviel überlapp mit allgemeinen Daten?
* * `vorteile:` Profane Vorteile
* * `fertigkeiten:` hier oder auf rootlevel?
* `magie:` Diese Gruppe ist nur für magisch Begabte
* * `asp:` Astralpunkte
* * `fertigkeiten:` Darunter sind Fertigkeiten mit entsprechenden Werten und Talenten gelistet
* * `vorteile:` Magische Vorteile..
* `karma:` Geweihte und alles was irgendwie heilig ist...
* * `kap:` Karmalpunkte
* * `fertigkeiten:` ...
* `pakt:` ...
* * `gup:` ...