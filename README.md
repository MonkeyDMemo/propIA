# 🚀 Generador de Propuestas Técnicas con Azure Functions

Este proyecto es una Azure Function App en Python que automatiza la generación de documentos Word de propuestas técnicas, integrando Azure OpenAI y Azure Blob Storage. Permite recibir un prompt con información del proyecto y devuelve un documento Word personalizado, almacenado y accesible mediante una URL segura.

## ✨ Características

- **🤖 Generación automática de propuestas técnicas** usando Azure OpenAI (GPT-4).
- **📄 Plantillas Word** almacenadas en Azure Blob Storage.
- **🔄 Reemplazo inteligente de placeholders** en párrafos, tablas y cuadros de texto.
- **🌐 Endpoint HTTP** para generar propuestas.
- **🔒 URLs pre-firmadas (SAS)** para descargar documentos de manera segura.
- **📝 Múltiples secciones generadas**: resumen ejecutivo, alcance, plan de trabajo, equipo, inversión, etc.

## 📁 Estructura del Proyecto

```
.
├── 📜 function_app.py                # Punto de entrada principal de Azure Functions
├── 📂 propia/
│   ├── 🐍 __init__.py                # (vacío)
│   └── 📝 de_1.py                    # Lógica completa de generación de propuestas
├── 📋 requirements.txt               # Dependencias del proyecto
├── ⚙️ host.json                      # Configuración de Azure Functions
├── 🔐 local.settings.json            # Variables de entorno locales (no subir a producción)
└── 🧩 .vscode/extensions.json        # Recomendaciones de extensiones para VS Code
```

## 🔌 Endpoint Disponible

### 📤 **POST `/api/generar_documento`**
Genera una propuesta técnica a partir de un prompt.

**Opciones de envío:**

1. **JSON Body:**
```json
{
  "prompt": "Texto con la información del proyecto",
  "placeholders_personalizados": {
    "[CUSTOM]": "Contenido personalizado opcional"
  }
}
```

2. **Texto plano en el body:**
```
Información completa del proyecto para generar la propuesta...
```

3. **Query parameter:**
```
/api/generar_documento?prompt=Información del proyecto
```

**Response exitosa:**
```json
{
  "url": "https://storage.blob.core.windows.net/...",
  "empresa": "Nombre de la Empresa",
  "fecha": "12 de agosto de 2025",
  "titulo": "Título del Proyecto",
  "mensaje": "Propuesta generada exitosamente"
}
```

## ⚙️ Configuración

### 1. 🔑 Variables de entorno
Configura estas variables en `local.settings.json`:
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "...",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AZURE_OPENAI_ENDPOINT": "https://your-resource.openai.azure.com/",
    "OPENAI_API_KEY": "your-api-key",
    "DEPLOYMENT_NAME": "gpt-4o-mini",
    "API_VERSION": "2024-02-15-preview",
    "STORAGE_CONNECTION_STRING": "your-storage-connection-string"
  }
}
```

### 2. 📦 Dependencias principales
El archivo `requirements.txt` incluye:
- `azure-functions`
- `requests`
- `python-docx`
- `azure-storage-blob`

Instala con:
```bash
pip install -r requirements.txt
```

### 3. 📄 Plantilla Word
La plantilla debe estar ubicada en Azure Blob Storage:
- **Container**: `propia`
- **Path**: `plantilla/Plantilla-Propuesta.docx`
- **Placeholders disponibles**:
  - `[RESUMEN]` - Resumen ejecutivo
  - `[ALCANCE]` - Alcance mínimo del proyecto
  - `[PLAN_TRABAJO]` - Plan de trabajo con fases
  - `[EQUIPO]` - Estructura del equipo
  - `[INVERSION]` - Inversión detallada
  - `[SUPUESTOS]` - Supuestos y condiciones
  - `[CARTA_PRESENTACION]` - Carta de presentación
  - `[titulo]` - Título del proyecto
  - `[fecha]` - Fecha de la propuesta

## 🏃‍♂️ Ejecución Local

1. **Inicia Azure Functions Core Tools:**
   ```bash
   func start
   ```

2. **El endpoint estará disponible en:**
   ```
   http://localhost:7071/api/generar_documento
   ```

## 🛠️ Características Técnicas

### 📊 Procesamiento de Documentos
- ✅ Reemplazo en **párrafos normales**
- ✅ Reemplazo en **tablas**
- ✅ Reemplazo en **cuadros de texto** (textboxes)
- 🧹 Limpieza automática de formato Markdown
- 📐 Preservación de datos numéricos y tablas

### 🤖 Integración con Azure OpenAI
- Modelo: `gpt-4o-mini`
- Generación específica para cada sección
- Prompts optimizados para documentos Word
- Límites de tokens configurables por sección

### 💾 Almacenamiento
- Los documentos generados se guardan en: `propia/propuestas/`
- Nomenclatura: `Propuesta_[Empresa]_[Timestamp].docx`
- URLs pre-firmadas con expiración configurable (default: 60 minutos)

## 🔒 Seguridad

- ⚠️ **NO subas** `local.settings.json` a repositorios públicos
- 🔐 Las URLs de descarga usan SAS tokens temporales
- ⏰ Expiración automática de URLs configurada
- 🛡️ Validación de entrada en todos los endpoints

## 📝 Notas de Implementación

### Extracción de Información
El sistema extrae automáticamente:
- **Nombre de empresa**: Busca patrones como "SA de CV", "S.A.", "Inc."
- **Fecha**: Formatos "DD de Mes de YYYY" o "DD/MM/YYYY"
- **Título**: Extrae de headers markdown (#) si están presentes

### Manejo de Errores
- Logging detallado en cada etapa del proceso
- Respuestas JSON estructuradas para errores
- Traceback completo en modo debug

## 🚦 Requisitos

- 🐍 Python 3.8+
- ☁️ Azure Functions Core Tools v4
- 🔑 Cuenta de Azure con:
  - Azure OpenAI Service
  - Azure Blob Storage
  - Azure Functions

## 💼 Créditos

Desarrollado por el equipo de **HITSS**.

---

## 📞 Soporte

¿Dudas o sugerencias? 
- 🐛 Abre un issue en el repositorio
- 📧 Contacta al equipo de desarrollo
- 📚 Revisa los logs en Azure Portal para debugging

---

**⭐ Recuerda configurar correctamente todas las variables de entorno antes de desplegar a producción!**