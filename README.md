# IlarisDB
Sammelstelle für strukturierte Ilaris Daten, wie Kreaturen, NSCs, Zauber usw.. Eine Webansicht befindet sich in Arbeit, der aktuelle Stand ist hier zu begutachten: [https://ilaris-tools.github.io/IlarisDB](https://ilaris-tools.github.io/IlarisDB/db/kreaturen/)

> Hinweis: Die Datenbank befindet sich noch im Aufbau, die Strukturen und technische Details ändern sich möglicherweise schneller, als die Beschreibungen und Änderungen müssen aktuell noch manuell exportiert werden.


## Die Idee
Das Ziel ist hier Daten rund um das Ilaris Regelsystem strukturiert zu sammeln, sodass sie von anderen Tools genutzt werden können.
Wir haben vorerst davon abgesehen eine "echte" Datenbank zu erstellen, da sich strukturierte Textdateien (yaml/json) einfacher handhaben lassen und nicht verloren gehen falls das Projekt einschläft. Eine solche Datei enthält beliebig viele Einträge die einem vorgegebenen [Schema](https://ilaris-tools.github.io/IlarisDB/docs/datenbank/) folgen und einen eindeutigen Namen (ID) haben. Mit einfachen Skripten können zum Beispiel Tokens für VTTs oder Monsterboxen für das Latex-Template generiert werden. Diese "Tabellen" liegen im Ordner `daten`. Sie können durch die IDs lose aufeinander verweisen. Ob die Trennbarkeit der Tabellen, teilweise Redundanz in den Daten zB Namen von Talenten/Vorteilen rechtfertigt, wird sich zeigen.  
[Mehr Infos](https://ilaris-tools.github.io/IlarisDB/docs/datenbank/)


## Daten

Folgende Tabellen gibt es bereits oder befinden sich in Arbeit. Die Links führen zu den Beschreibungen in der Online-Dokumentation.

* `kreaturen.yml` Monster, NSCs, Beschworene Wesen und vieles mehr zum schnellen Einsatz im Spiel. [Mehr Infos](https://ilaris-tools.github.io/IlarisDB/docs/db/kreaturen/)
* `charaktere.yml` Regelkonforme Charaktere, wie sie mit Sephrasto oder nach den Regeln im Buch generiert werden könnten. Geeignet für Spieler-Charaktere und NSCs aus Abenteuern. [Mehr Infos](https://ilaris-tools.github.io/IlarisDB/docs/db/kreaturen/)
* `quellen.yml` Infos zu den Quellen aus denen die Daten gesammelt wurden.

Folgende Tabellen könnten je nach Bedarf folgen um mehr Details für externe Tools bereit zu stellen.

* eigenheiten
* fertigkeiten/talente
* vorteile
* manöver
* publikationen
* gegenstände
    * waffen
    * rüstungen
    * gegenstände
    * artefakte
    * pflanzen
    * tränke
