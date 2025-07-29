## Athena Integration

Eine benutzerdefinierte Integration für Home Assistant, die Unterstützung für Athena Überwachungs- und Steuerungssysteme bietet.

### Features

- **Sensoren**: Temperatur, Luftfeuchtigkeit, Druck, Signalstärke, Status
- **Schalter**: Stromsteuerung, Automatischer Modus
- **Binäre Sensoren**: Online-Status, Fehlererkennung, Wartungsmodus
- **Konfigurationsentitäten**: Schwellenwerte, Intervalle, Modi und Profile
- **Echtzeit-Überwachung**: Kontinuierliche Datenaktualisierungen

### Installation

1. Fügen Sie diese Repository zu HACS als benutzerdefinierte Integration hinzu
2. Installieren Sie "Athena Integration" über HACS
3. Starten Sie Home Assistant neu
4. Gehen Sie zu Einstellungen → Geräte & Dienste
5. Klicken Sie auf "Integration hinzufügen" und suchen Sie nach "Athena"

### Konfiguration

Die Integration verwendet einen Konfigurationsassistenten:
- Geben Sie die IP-Adresse Ihres Geräts ein
- Setzen Sie den Port (Standard: 80)
- Geben Sie Benutzername und Passwort ein
- Wählen Sie den Gerätetyp aus
- Konfigurieren Sie das Scan-Intervall

### Unterstützte Gerätetypen

- **Controller**: Vollständige Steuerung mit allen Entitäten
- **Monitor**: Nur-Lese-Überwachung
- **Sensor**: Grundlegende Sensordaten
