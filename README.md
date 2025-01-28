# ICS-2000 Home Assistant Integratie

Eenvoudige stappen om de KlikAanKlikUit ICS-2000 te integreren in Home Assistant.

---

## Installatie

Volg deze stappen om de integratie te installeren:

1. **HACS installeren**
   - Volg de instructies op [HACS Setup](https://hacs.xyz/docs/setup/download/) om HACS in Home Assistant te installeren.

2. **Custom Repository toevoegen**
   - Voeg in HACS een custom integratie-repository toe:
     - **URL:** `https://github.com/Otte-S/KlikAanKlikUit/`
   - Selecteer deze custom repository in HACS en klik op **DOWNLOAD**.

3. **Configuratie aanpassen**
   - Voeg de File Editor add-on toe in Home Assistant.
   - Gebruik de File Editor om het volgende toe te voegen aan je `<config_dir>/configuration.yaml`:

     ```yaml
     light:                                      
       - platform: ics2000
         mac: MAC_HERE
         email: EMAIL_HERE
         password: PASSWORD_HERE_OR_secrets.yaml
         tries: 3                              # Optioneel, standaard is 1
         sleep: 2                              # Optioneel, standaard is 3
         aes: 185dd26964b583ca097231a7ea3ba407 # Optioneel
         ip_address: 192.168.1.205             # Optioneel
     ```

4. **Herstart Home Assistant**
   - Herstart Home Assistant om de wijzigingen door te voeren.

5. **Dashboard aanpassen**
   - Voeg een 'Light'-kaart toe aan je dashboard met behulp van een van de aangemaakte 'light'-entiteiten.

---

## Optionele Instellingen

- **Retries en pauzes instellen**
  - De ICS-2000/KAKU kan de huidige status van een verbonden apparaat niet opvragen.
  - Gebruik `tries` en `sleep` om herhaalde commando’s te sturen voor betrouwbaarheid:
    - **tries:** Aantal herhalingen (standaard: 1).
    - **sleep:** Pauze tussen commando’s in seconden (standaard: 3).
  
  **Voorbeeld:**
  Bij `tries: 3` en `sleep: 3` wordt het commando 3 keer verzonden met een totale tijd van 6 seconden:
  Klik - pauze - klik - pauze - klik.

- **Thread Management**
  - Het verzenden van commando’s gebeurt in een aparte thread.
  - De integratie controleert of een apparaat al een actieve thread heeft.

---

## Probleemoplossing

- **Foutmelding bij toevoegen van een 'Light'-kaart**
  - Voeg eerst een 'Button'-kaart toe met de entiteit en probeer daarna opnieuw een 'Light'-kaart.

---

## Op macOS Dependencies Installeren

Voor macOS-gebruikers kunnen extra stappen nodig zijn bij het installeren van dependencies. Gebruik Homebrew:

```bash
brew install openssl@1.1

CPATH=/usr/local/Cellar/openssl\@1.1/1.1.1s/include/ \
  LIBRARY_PATH=/usr/local/Cellar/openssl\@1.1/1.1.1s/lib/ \
  pip install --upgrade -r dev_requirements.txt
```

---

Met deze stappen zou je ICS-2000 naadloos moeten integreren in Home Assistant. Veel succes!

