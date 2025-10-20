# Haushaltsausgaben in der Schweiz
## Ein Vergleich nach Alter, Haushaltstyp und Zeit (2006 – 2022)

---

## 📊 Projektübersicht

Dieses Projekt analysiert die Entwicklung der Haushaltsausgaben in der Schweiz über einen Zeitraum von 16 Jahren (2006-2022). Ziel ist es, datenbasierte Einsichten für Politik, Konsumentenforschung und Wirtschaftsplanung zu gewinnen.

**CAS Information Engineering – Scripting**  
**Hochschule für Angewandte Wissenschaften Zürich (ZHAW)**  
**Gruppenname:** SC02_Gruppe_09

---

## 🎯 Forschungsfragen

1. Wie haben sich die durchschnittlichen monatlichen Haushaltsausgaben in der Schweiz von 2006 bis 2022 verändert?
2. Welche Unterschiede gibt es zwischen Altersgruppen (z. B. Junge vs. Pensionierte)?
3. Wie unterscheiden sich Familienhaushalte von Einpersonenhaushalten in ihrer Ausgabenstruktur?
4. Welche Kategorien (z. B. Wohnen, Verkehr, Gesundheit) sind über die Jahre am stärksten gewachsen?

---

## 📁 Datenquellen

Alle Datensätze stammen vom **Bundesamt für Statistik (BFS)** über [opendata.swiss](https://opendata.swiss):

- **Datensatz 1:** Gesamtausgaben der Haushalte 2006–2022
- **Datensatz 2:** Ausgaben nach Altersklassen
- **Datensatz 3:** Ausgaben nach Haushaltstypen

> **Hinweis:** Die genauen URLs befinden sich in `data/README.md`

---

## 📂 Projektstruktur
```markdown
haushaltsausgaben-schweiz/
│
├── notebooks/
│   ├── 01_datenladen_bereinigung.ipynb    # Daten laden & bereinigen
│   ├── 02_datenanalyse.ipynb              # Analyse & Auswertung
│   ├── 03_visualisierung.ipynb            # Diagramme & Heatmap
│   └── 04_business_case.ipynb             # Business Case Bericht
│
├── data/
│   ├── raw/                               # Original Excel-Dateien
│   └── processed/                         # Bereinigte CSV/JSON-Dateien
│
├── outputs/
│   ├── figures/                           # Visualisierungen (PNG)
│   └── tables/                            # Exportierte Statistiken
│
└── src/                                   # Python-Module (optional)
```

## 🛠️ Setup & Installation

### Voraussetzungen
- Python 3.8 oder höher
- Jupyter Notebook / JupyterLab

### Installation

1. **Repository klonen**
```bash
git clone https://github.com/[euer-username]/haushaltsausgaben-schweiz.git
cd haushaltsausgaben-schweiz
```

   Virtual Environment erstellen (empfohlen)
```bash   
python -m venv venv
source venv/bin/activate        # Auf macOS/Linux
venv\Scripts\activate           # Auf Windows
```

Abhängigkeiten installieren
```bash   
pip install -r requirements.txt
```

Jupyter Notebook starten
```bash   
jupyter notebook
```

📊 Technologie-Stack

Python 3.x
Pandas – Datenverarbeitung
Matplotlib / Seaborn – Visualisierung
Jupyter Notebook – Entwicklungsumgebung
Excel – Datenquellen (BFS)


📝 Bewertungskriterien (gemäss Modulvorgabe)
1. Jupyter Notebooks & Code (30 Punkte)

✅ Gut strukturierter, dokumentierter Code<br>
✅ Selbsterklärende Kommentare<br>
✅ Saubere Pandas DataFrames

2. Bericht als Jupyter Notebook (15 Punkte)

✅ Klare Einleitung mit Business Case<br>
✅ Beschreibung der Daten & Methodik<br>
✅ Gut formatiert und verständlich