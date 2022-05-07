---
permalink: /docs/db/kreaturen/
layout: default
---

## Kreaturen

Die Kreaturentabelle ist die erste Tabelle in der Datenbank. Da Kreaturen, für Abenteuer (IlarisTex) und zum Spielen (FoundryVTT) gebraucht werden und sich die Werte aus den Bestarien und Regelwikis für DSA1-5 nicht direkt verwenden lassen, ist hier warscheinlich der Bedarf am größten. Ihre Struktur soll die Einträge aus dem Bestarium des Ilaris Regelbuchs möglichst vollständig abbilden können, aber trotzdem algemein und erweiterbar bleiben. Viele Daten werden sehr kleinteilig zerlegt und reine Werte von möglichen Bemerkungen und Spezialfällen getrennt, damit sie automatisiert verarbeitet werden können (zB `tp.anzahl:4`, `tp.W: 6`, `tp.plus: 3` statt `tp: 4W6+3`). Dies erlaubt/erleichtert beispielsweise das Sortieren oder Filtern der Kreaturen nach konkreten Eigenschaften oder das exportieren zu Tokens für verschiedene Virtual Table Tops (VTT).


### Unterschiede zu Charakteren

Kreaturen unterliegen nicht den selben Regeln der Generierung und weichen daher auch in den Angaben ihrer Werte von generierten (N)SCs ab. Im wesentlichen bedeutet dies, das nur die PW für die wichtigsten Attribute und Talente angegeben werden. Sie werden nicht dynamisch aus Grundwerten berechnet und können daher auch nicht nach den Generierungsregeln gesteigert werden. Humanoide NSCs mit Persönlichkeit mögen hier in den Übergangsbereich fallen und je nach SL lieber als Kreatur oder Charakter geführt werden. Eine automatische Konvertierung von Charakteren zu Kreaturen ist für die Zukunft denkbar. Die folgende Liste zeigt einige konzeptionelle Unterschiede, die bei der Erstellung der Datenbank berücksichtigt wurden:

* PW für Talente (profane fertigkeiten werden teilweise übergangen)
* Kampfwerte (GS, WS, TP, AT, INI, ...) festgelegt und nicht berechnet
* Besonderheiten nach Kreaturenklassen: Daimonid, Dämon, Elementar, Feenwesen, Humanoid, Mythenwesen, Tier, Untoter
*  Eigenschaften statt Vorteilen: Kreaturen können neben alg. Vorteilen auch bestimmte Nachteile und Anfälligkeiten (zB gegen Feuer) oder besondere Fähigkeiten (zB Fliegen) haben.
* Varianten: Viele Kreaturen unterscheiden sich nur in Kleinigkeiten oder lassen sich in einer allgemeineren Gruppe zusammenfassen, oft sind 'kleinere' verträter als `variantevon` gekennzeichnet.
* Info: Kreaturen haben ein info feld in das zusätzlicher text kann oder Spezialregeln. Wenn Varianten keine extra Kreatur "wert" sind, können die einfachen Hinweise auch hier mit rein.



### Abweichungen von den Quellen

Diese Liste ist sicherlich unvollständig, da viele Anpassungen durchgeführt wurden um die Kreaturen in die DB-Struktur zu 'zwängen'.

* Elementare werden nach Element und Typ eingetragen (zB Feuerdschinn) alle Individuellen Elementare als varianten einer dieser algemeinen bezeichnungen, werte können an der Stelle sehr unterschiedlich sein.



### Erforderliche Daten

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