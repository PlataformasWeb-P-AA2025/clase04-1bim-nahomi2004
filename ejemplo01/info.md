## Pasos

1. Crear una base de datos en couchDB; usar Fauxton
2. Darle los permisos necesario a la base datos
3. A través del comando curl en un terminal, ejecutar el siguiente comando:

```
  curl -d @datos.json -H "Content-type: application/json" -X POST http://127.0.0.1:5984/dem02025/_bulk_docs
```
4. Ingresar a Fauxton y comprar que la data esté disponible
