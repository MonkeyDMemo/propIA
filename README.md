# Generador de Propuestas Técnicas con Azure Functions

Este proyecto es una Azure Function App en Python que automatiza la generación de documentos Word de propuestas técnicas, integrando Azure OpenAI y Azure Blob Storage. Permite recibir un prompt con información del proyecto y devuelve un documento Word personalizado, almacenado y accesible mediante una URL segura.

## Características

- **Generación automática de propuestas técnicas** usando Azure OpenAI (GPT).
- **Plantillas Word** almacenadas en Azure Blob Storage.
- **Reemplazo inteligente de placeholders** en la plantilla con contenido generado.
- **Endpoints HTTP** para generar, listar y obtener propuestas.
- **URLs pre-firmadas (SAS)** para descargar documentos de manera segura.

## Estructura del Proyecto

```
.
├── function_app.py                # Punto de entrada principal de Azure Functions
├── propia/
│   ├── __init__.py                # Implementación principal de endpoints y lógica
│   └── de_1.py                    # Lógica alternativa para generación de propuestas
├── requirements.txt               # Dependencias del proyecto
├── host.json                      # Configuración de Azure Functions
├── local.settings.json            # Variables de entorno locales (no subir a producción)
└── .vscode/extensions.json        # Recomendaciones de extensiones para VS Code
```

## Endpoints Disponibles

- **POST `/api/generar_propuesta`**  
  Genera una propuesta técnica a partir de un prompt.  
  **Body:**  
  ```json
  {
    "prompt": "Texto con la información del proyecto"
  }
  ```
  **Respuesta:**  
  ```json
  {
    "message": "Propuesta generada exitosamente",
    "document_id": "...",
    "filename": "...",
    "url_presignada": "...",
    "expira_en_horas": 24,
    "empresa": "...",
    "titulo": "...",
    "cambios_realizados": ...,
    "status": "completed"
  }
  ```

- **GET `/api/obtener_propuesta/{document_id}`**  
  Obtiene la URL de descarga de una propuesta generada.

- **GET `/api/listar_propuestas`**  
  Lista todas las propuestas generadas y sus URLs de descarga.

## Configuración

1. **Variables de entorno**  
   Configura tus claves y endpoints en `local.settings.json`:
   - `AZURE_OPENAI_ENDPOINT`
   - `OPENAI_API_KEY`
   - `DEPLOYMENT_NAME`
   - `STORAGE_CONNECTION_STRING`

2. **Dependencias**  
   Instala las dependencias con:
   ```sh
   pip install -r requirements.txt
   ```

3. **Plantilla Word**  
   Sube tu plantilla base a Azure Blob Storage en la ruta:  
   `propia/plantilla/Plantilla-Propuesta.docx`

## Ejecución Local

1. Inicia el entorno de Azure Functions:
   ```sh
   func start
   ```
2. Realiza peticiones HTTP a los endpoints usando Postman, curl o tu frontend.

## Notas Técnicas

- El reemplazo de placeholders en Word soporta párrafos, tablas y cuadros de texto.
- El contenido generado por OpenAI es limpiado para evitar formato Markdown y adaptarse a Word.
- Los documentos generados se almacenan en Azure Blob Storage bajo la carpeta `propuestas/`.

## Seguridad

- No subas `local.settings.json` ni tus claves a repositorios públicos.
- Las URLs de descarga usan SAS y expiran automáticamente.

## Créditos

Desarrollado por el equipo de HITSS.

---

¿Dudas o sugerencias? Abre un issue o contacta al responsable