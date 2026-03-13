# HTTP-Statuscodes Leitfaden

HTTP-Antwortstatuscodes geben an, ob eine bestimmte HTTP-Anfrage erfolgreich abgeschlossen wurde. Antworten werden in fünf Klassen eingeteilt:

1.  **Informative Antworten** (100–199)
2.  **Erfolgreiche Antworten** (200–299)
3.  **Umleitungsnachrichten** (300–399)
4.  **Client-Fehlermeldungen** (400–499)
5.  **Server-Fehlermeldungen** (500–599)

## So verwenden Sie dieses Projekt

Mit dem CLI-Tool können Sie schnell Beschreibungen für jeden Code finden:

```bash
python httpcode.py 404 --lang de
```

Dies zeigt die vollständige Beschreibung des 404-Codes auf Deutsch an.
