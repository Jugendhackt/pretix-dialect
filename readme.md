
Pretix Translation für Jugend hackt
===================================

Da sich unsere Teilnehmer*innen anmelden und nicht ein Ticket bestellen,
überschreiben wir die Standardtext von de_Informal mit unseren eigenen.


Änderungen sollten bei einem Pretix-Update aus der originalen
de_Informal Übersetzung nachgezogen werden.



Usage
=====

Referenz für Konfiguration des Servers:

[https://docs.pretix.eu/en/latest/admin/config.html#translations]


Eintrag in der pretix.cfg:

    [laguages]
    path=/path/to/my/translations

Diese Repository muss in dem Pfad zu finden sein.
Sprachen in diesem Pfad werden den internen bevorzugt.


Die .po Dateien sind mit msgfmt in .mo Dateien zu übersetzen.
