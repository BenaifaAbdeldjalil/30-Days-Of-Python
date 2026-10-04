# -*- coding: utf-8 -*-
# Exercises: Day 22
# part 1 
import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
import json

url1 = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Lets use the requests get method to fetch the data from url

response = requests.get(url1)
soup = BeautifulSoup(response.text, "html.parser")
donnees = []

# Exemple 1 : récupérer tous les paragraphes
for p in soup.find_all(['p','div','article','span','li']):
    texte = p.get_text(strip=True)
    if texte:
        donnees.append({
            "type": "paragraphe",
            "contenu": texte
        })

# Exemple 2 : récupérer les titres (h2, h3)
for h in soup.find_all(['h2', 'h3']):
    texte = h.get_text(strip=True)
    if texte:
        donnees.append({
            "type": h.name,
            "contenu": texte
        })

# Exemple 3 : récupérer les tableaux de statistiques
for table in soup.find_all('table'):
    lignes = []
    for tr in table.find_all('tr'):
        cellules = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
        if cellules:
            lignes.append(cellules)
    if lignes:
        donnees.append({
            "type": "tableau",
            "contenu": lignes
        })
for l in soup.find_all('a'):
    link = p.get_text(strip=True)
    if link:
        donnees.append({
            "type": "link",
            "contenu": link
        })

destination = Path("22_Day_Web_scraping/part1.json")
destination.parent.mkdir(parents=True, exist_ok=True)
# Enregistrement dans un fichier JSON
with destination.open('w', encoding='utf-8') as f:
    json.dump(donnees, f, ensure_ascii=False, indent=4)

print(f"✅ {len(donnees)} éléments enregistrés dans {destination}")

#part 2 
url2 = 'https://archive.ics.uci.edu/datasets'

# Lets use the requests get method to fetch the data from url

response = requests.get(url2)
soup = BeautifulSoup(response.text, "html.parser")
donnees = []

# Exemple 1 : récupérer tous les paragraphes
for p in soup.find_all(['p','div','article','span','li']):
    texte = p.get_text(strip=True)
    if texte:
        donnees.append({
            "type": "paragraphe",
            "contenu": texte
        })

# Exemple 2 : récupérer les titres (h2, h3)
for h in soup.find_all(['h2', 'h3']):
    texte = h.get_text(strip=True)
    if texte:
        donnees.append({
            "type": h.name,
            "contenu": texte
        })

# Exemple 3 : récupérer les tableaux de statistiques
for table in soup.find_all('table'):
    lignes = []
    for tr in table.find_all('tr'):
        cellules = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
        if cellules:
            lignes.append(cellules)
    if lignes:
        donnees.append({
            "type": "tableau",
            "contenu": lignes
        })
for l in soup.find_all('a'):
    link = p.get_text(strip=True)
    if link:
        donnees.append({
            "type": "link",
            "contenu": link
        })

destination = Path("22_Day_Web_scraping/part2.json")
destination.parent.mkdir(parents=True, exist_ok=True)
# Enregistrement dans un fichier JSON
with destination.open('w', encoding='utf-8') as f:
    json.dump(donnees, f, ensure_ascii=False, indent=4)

print(f"✅ {len(donnees)} éléments enregistrés dans {destination}")

# part 3 





url3 = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url3)
soup = BeautifulSoup(response.text, "html.parser")

donnees = []
categorie_actuelle = None
bloc = None

# On prend TOUTES les balises pertinentes dans l'ordre du document,
# sans distinguer p / h2 / li / td / span ...
for balise in soup.find_all(['h2', 'h3', 'h4', 'p', 'li', 'td', 'th', 'strong', 'span']):
    texte = balise.get_text(" ", strip=True)
    if not texte:
        continue

    # 1) Détection d'un titre de catégorie (h2/h3 courts, sans ":")
    if balise.name in ['h2', 'h3','h4'] and ':' not in texte and len(texte) < 40:
        # On ferme le bloc précédent s'il existe
        if bloc is not None:
            donnees.append(bloc)

        categorie_actuelle = texte
        bloc = {"category": categorie_actuelle}
        continue

    # 2) Ligne de statistique "clé : valeur"
    if ':' in texte:
        # On sépare uniquement sur le premier ":"
        cle, valeur = texte.split(':', 1)
        cle = cle.strip()
        valeur = valeur.strip()

        # Si on n'a pas encore de catégorie, on en crée une par défaut
        if bloc is None:
            bloc = {"category": "General"}

        # On ignore les entrées vides ou trop longues (paragraphes)
        if cle and valeur and len(valeur) < 100:
            bloc[cle] = valeur

# On n'oublie pas le dernier bloc
if bloc is not None:
    donnees.append(bloc)

# Nettoyage : on garde seulement les blocs qui ont au moins 2 stats
donnees = [b for b in donnees if len(b) > 2]
destination3 = Path("22_Day_Web_scraping/part3.json")
destination3.parent.mkdir(parents=True, exist_ok=True)

# Sauvegarde JSON
with destination3.open('w', encoding='utf-8') as f:
    json.dump(donnees, f, ensure_ascii=False, indent=4)

print(f"✅ {len(donnees)} catégories enregistrées")
for d in donnees:
    print(f"  • {d['category']} ({len(d)-1} stats)")
