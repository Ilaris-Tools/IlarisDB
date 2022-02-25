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
> TODO