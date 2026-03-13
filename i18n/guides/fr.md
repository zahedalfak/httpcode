# Guide des codes de statut HTTP

Les codes de statut de réponse HTTP indiquent si une requête HTTP spécifique a été complétée avec succès. Les réponses sont regroupées en cinq classes :

1.  **Réponses informatives** (100–199)
2.  **Réponses réussies** (200–299)
3.  **Messages de redirection** (300–399)
4.  **Réponses d'erreur du client** (400–499)
5.  **Réponses d'erreur du serveur** (500–599)

## Comment utiliser ce projet

Vous pouvez utiliser l'outil CLI pour trouver rapidement des descriptions pour n'importe quel code :

```bash
python httpcode.py 404 --lang fr
```

Cela affichera la description complète du code 404 en français.
