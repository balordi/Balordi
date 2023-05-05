# Balordi
Balordi è il nome che abbiamo scelto per il nostro gruppo di lavoro.

# Breve descrizione dell'app
Quest'app vuole permettere all'utente di inserire delle caratteristiche di una bandiera tramite un'interfaccia web per poi andare a "indovinare" la nazione a cui appartiene la bandiera.

# Installazione e esecuzione

Prima di installare o eseguire l'app, si devono installare i requisiti:
```
pip install -r ./requirements.txt
```
Oppure, se si è su una distribuzione Linux con `make` installato:
```
make install-reqs
```

## Esecuzione
Per eseguire l'app, basterà avere installato python e flask, per poi eseguire il comando:

```
python -m flask --app ./src/bandiere/__init__.py run
```

Oppure, se si è su una qualsiasi distribuzione di Linux e si ha il programma `make` installato:

```
make run
```

 ## Installazione
 Per installare l'app, dovremo usare `pip`:
 ```
 pip install -e .
 ```
 In alternativa, se si è su una qualsiasi distribuzione di Linux con il programma `make` installato:
 ```
 make install
 ```

 Una volta installata l'app, dovremo utilizzare flask per lanciarla:
 ```
 python -m flask --app bandiere run
 ```

 Una volta lanciata l'app, basterà recarsi all'URL `127.0.0.1:5000` per visualizzare l'interfaccia web.