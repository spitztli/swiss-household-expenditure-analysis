"""
Excel-Dateien Inspektion
========================
Dieses Script inspiziert die drei BFS Excel-Dateien und zeigt deren Struktur.
"""

import pandas as pd
from pathlib import Path

# Pfade definieren
BASE_DIR = Path(__file__).parent
RAW_DATA_DIR = BASE_DIR / 'data' / 'raw'

# Die drei Dateien
files = {
    'Gesamtausgaben': RAW_DATA_DIR / 'gesamtausgaben_2006_2022.xlsx',
    'Ausgaben nach Alter': RAW_DATA_DIR / 'ausgaben_nach_alter.xlsx',
    'Ausgaben nach Haushaltstyp': RAW_DATA_DIR / 'ausgaben_nach_haushaltstyp.xlsx'
}

print("="*80)
print("INSPEKTION DER BFS EXCEL-DATEIEN")
print("="*80)

# Jede Datei inspizieren
for name, filepath in files.items():
    print(f"\n{'='*80}")
    print(f"📁 DATEI: {name}")
    print(f"{'='*80}")
    
    # Prüfen ob Datei existiert
    if not filepath.exists():
        print(f"❌ FEHLER: Datei nicht gefunden!")
        print(f"   Erwartet: {filepath}")
        continue
    
    try:
        # Excel-Datei laden (ohne Zeilen zu überspringen)
        df = pd.read_excel(filepath)
        
        # Grundinformationen
        print(f"\n📊 GRUNDINFORMATIONEN:")
        print(f"   Anzahl Zeilen: {len(df)}")
        print(f"   Anzahl Spalten: {len(df.columns)}")
        
        # Die ersten 20 Zeilen anzeigen (um Metadaten zu sehen)
        print(f"\n📋 ERSTE 20 ZEILEN:")
        print("-" * 80)
        print(df.head(20).to_string())
        
        # Spaltennamen
        print(f"\n🏷️  SPALTENNAMEN:")
        for i, col in enumerate(df.columns, 1):
            print(f"   {i}. {col}")
        
        # Datentypen
        print(f"\n🔤 DATENTYPEN:")
        print(df.dtypes)
        
        # Fehlende Werte
        print(f"\n⚠️  FEHLENDE WERTE:")
        missing = df.isnull().sum()
        if missing.sum() > 0:
            print(missing[missing > 0])
        else:
            print("   Keine fehlenden Werte gefunden")
        
    except Exception as e:
        print(f"❌ FEHLER beim Laden: {e}")

print("\n" + "="*80)
print("INSPEKTION ABGESCHLOSSEN")
print("="*80)