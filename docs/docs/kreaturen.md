---
permalink: /docs/db/kreaturen
layout: default
---

## Kreaturen

Die Kreaturentabelle ist die erste Tabelle in der Datenbank. Ihre Struktur soll die Einträge aus dem Bestarium des Ilaris Regelbuchs möglichst vollständig abbilden können, aber trotzdem algemein und erweiterbar bleiben. Viele Daten werden sehr kleinteilig zerlegt und reine Werte von möglichen Bemerkungen und Spezialfällen getrennt, damit sie automatisiert verarbeitet werden können (zB `tp.anzahl:4`, `tp.W: 6`, `tp.plus: 3` statt `tp: 4W6+3`). Dies erlaubt/erleichtert beispielsweise das Sortieren oder Filtern der Kreaturen nach konkreten Eigenschaften oder das exportieren zu Tokens für verschiedene Virtual Table Tops (VTT).

### Inahltliche Unterschiede

Kreaturen unterliegen nicht den selben Regeln der Generierung und weichen daher auch in den Angaben ihrer Werte von generierten (N)SCs ab. Im wesentlichen bedeutet dies, das nur die wichtigsten Werte angegeben werden und diese nicht dynamisch berechnet sondern direkt festgelegt worden sind. Die folgende Liste zeigt einige konzeptionelle Unterschiede, die bei der Erstellung der Datenbank berücksichtigt wurden:

* PW für Talente (profane fertigkeiten werden teilweise übergangen)
* Kampfwerte (GS, WS, TP, AT, INI, ...) festgelegt und nicht berechnet
* Besonderheiten nach Kreaturenklassen: Daimonid, Dämon, Elementar, Feenwesen, Humanoid, Mythenwesen, Tier, Untoter
*  Eigenschaften statt Vorteilen: Kreaturen können neben alg. Vorteilen auch bestimmte Nachteile und Anfälligkeiten (zB gegen Feuer) oder besondere Fähigkeiten (zB Fliegen) haben.
* Varianten: Viele Kreaturen unterscheiden sich nur in Kleinigkeiten oder lassen sich in einer allgemeineren Gruppe zusammenfassen, oft sind 'kleinere' verträter als `variantevon` gekennzeichnet.
* Info: Kreaturen haben ein info feld in das zusätzlicher text kann oder Spezialregeln. Wenn Varianten keine extra Kreatur "wert" sind, können die einfachen Hinweise auch hier mit rein



### Abweichungen von den Quellen

Diese Liste ist sicherlich unvollständig, da viele Anpassungen durchgeführt wurden um die Kreaturen in die DB-Struktur zu 'zwängen'.

* Elementare werden nach Element und Typ eingetragen (zB Feuerdschinn) alle Individuellen Elementare als varianten einer dieser algemeinen bezeichnungen, werte können an der Stelle sehr unterschiedlich sein.