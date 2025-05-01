## Pasos

1. Crear una base de datos en couchDB
2. Darle los permisos necesario a la base datos
3. A través del comando curl en un terminal, ejecutar el siguiente comando:

```
  curl -d @datos.json -H "Content-type: application/json" -X POST http://127.0.0.1:5984/personas004/_bulk_docs
```
