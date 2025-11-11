# FUNDECO Chatbot - Guía Completa

## Descripción
El chatbot de FUNDECO es un asistente virtual inteligente que ayuda a los usuarios con información sobre productos biodegradables, servicios de agricultura sostenible y consultas generales sobre la empresa.

## Características

### Funcionalidades Principales
- **Interfaz moderna**: Diseño integrado con la paleta de colores FUNDECO
- **Respuestas inteligentes**: Sistema basado en OpenAI GPT-3.5 Turbo
- **Modo demo**: Funciona sin API key con respuestas predefinidas
- **Responsive**: Se adapta a todos los dispositivos (móvil, tablet, desktop)
- **Animaciones suaves**: Efectos visuales profesionales

### Características de Diseño
- **Botón flotante**: Icono de chat siempre visible en la esquina inferior derecha
- **Ventana emergente**: Se abre/cierra con animaciones suaves
- **Avatar del bot**: Icono de hoja que representa sostenibilidad
- **Indicador de escritura**: Animación mientras el bot "piensa"
- **Sugerencias rápidas**: Chips clickeables para consultas comunes

## Instalación y Configuración

### 1. Dependencias
```bash
pip install -r requirements.txt
```

### 2. Variables de Entorno
Edita el archivo `.env` en la raíz del proyecto:

```env
# OpenAI API Configuration
OPENAI_API_KEY=tu_clave_real_de_openai_aqui

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
```

### 3. Obtener API Key de OpenAI
1. Ve a [platform.openai.com](https://platform.openai.com)
2. Crea una cuenta o inicia sesión
3. Ve a "API Keys" en tu dashboard
4. Crea una nueva API key
5. Cópiala y pégala en el archivo `.env`

### 4. Iniciar el Servidor
```bash
cd src/api
python app.py
```

## Uso del Chatbot

### Para Usuarios
1. **Abrir el chat**: Haz clic en el botón flotante verde con icono de chat
2. **Escribir mensaje**: Usa el campo de texto en la parte inferior
3. **Enviar**: Presiona Enter o haz clic en el botón de envío
4. **Sugerencias**: Haz clic en los chips de sugerencias para consultas rápidas

### Consultas Que Puede Responder
- ✅ Información sobre productos biodegradables
- ✅ Beneficios de la agricultura sostenible
- ✅ Servicios ofrecidos por FUNDECO
- ✅ Precios y planes disponibles
- ✅ Información de contacto
- ✅ Proceso de fabricación
- ✅ Impacto ambiental

## 🛠️ Desarrollo y Personalización

### Estructura de Archivos
```
src/
├── static/
│   ├── css/
│   │   └── chatbot.css          # Estilos del chatbot
│   └── js/
│       └── chatbot.js           # Lógica del chatbot
├── api/
│   └── app.py                   # Backend Flask con API
└── templates/
    └── home/
        └── home.html            # Página que incluye el chatbot
```

### Personalizar Respuestas Demo
En `app.py`, función `get_demo_response()`:

```python
def get_demo_response(user_message):
    message_lower = user_message.lower()
    
    # Agregar nuevas palabras clave y respuestas
    if 'nueva_palabra_clave' in message_lower:
        return "Tu respuesta personalizada aquí"
```

### Personalizar Estilos
En `chatbot.css`, modifica las variables CSS:

```css
:root {
    --primary-green: #2d5016;      /* Color principal */
    --accent-green: #7cb342;       /* Color de acento */
    --warm-orange: #ff8f00;        /* Color de usuario */
}
```

### Agregar Nuevas Funcionalidades JavaScript
En `chatbot.js`, en la clase `FundecoBot`:

```javascript
// Agregar método personalizado
sendPredefinedMessage(message) {
    this.openChatbot();
    setTimeout(() => {
        this.sendMessage(message);
    }, 500);
}
```

## 🔧 API del Chatbot

### Endpoint Principal
```
POST /api/chat
Content-Type: application/json

{
    "message": "¿Qué son las fundas biodegradables?"
}
```

### Respuesta
```json
{
    "response": "Las fundas biodegradables de FUNDECO...",
    "status": "success"
}
```

### Manejo de Errores
```json
{
    "error": "Error processing your message",
    "details": "Descripción del error"
}
```

## Casos de Uso

### 1. Integración en Otras Páginas
```html
<!-- Incluir CSS y JS -->
<link rel="stylesheet" href="/static/css/chatbot.css">
<script src="/static/js/chatbot.js"></script>

<!-- El chatbot se inicializa automáticamente -->
```

### 2. Abrir Chatbot Programáticamente
```javascript
// Abrir el chatbot
openFundecoBot();

// Enviar mensaje predefinido
sendToFundecoBot("Quiero información sobre precios");
```

### 3. Personalizar Mensajes de Bienvenida
En `chatbot.js`, modifica el HTML del mensaje de bienvenida:

```javascript
<div class="welcome-message">
    <h4>¡Tu saludo personalizado! 👋</h4>
    <p>Mensaje personalizado aquí...</p>
</div>
```

## 🔍 Modo Demo vs Modo OpenAI

### Modo Demo (Sin API Key)
- ✅ Respuestas instantáneas predefinidas
- ✅ No requiere configuración externa
- ✅ Funciona sin conexión a OpenAI
- ❌ Respuestas limitadas a patrones predefinidos

### Modo OpenAI (Con API Key)
- ✅ Respuestas inteligentes y contextuales
- ✅ Comprende consultas complejas
- ✅ Aprende del contexto de la conversación
- ❌ Requiere API key y conexión a internet
- ❌ Puede tener costos asociados

## Solución de Problemas

### El chatbot no aparece
1. Verifica que `chatbot.css` y `chatbot.js` estén incluidos
2. Revisa la consola del navegador por errores
3. Asegúrate de que Font Awesome esté cargado

### Error en las respuestas
1. Verifica que el servidor Flask esté corriendo
2. Revisa la configuración de la API key en `.env`
3. Checa los logs del servidor para errores

### Problemas de estilos
1. Verifica que no hay conflictos CSS
2. Asegúrate de que las variables CSS están definidas
3. Revisa que las fuentes (Teko, Poppins) se carguen correctamente

## Compatibilidad

### Navegadores Soportados
- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+

### Dispositivos
- ✅ Desktop (1200px+)
- ✅ Tablet (768px - 1199px)
- ✅ Mobile (320px - 767px)

## Próximas Funcionalidades

### En Desarrollo
- [ ] Historial de conversaciones
- [ ] Modo offline avanzado
- [ ] Integración con base de datos
- [ ] Métricas y analytics
- [ ] Soporte para archivos/imágenes
- [ ] Chatbot multiidioma

### Mejoras Planificadas
- [ ] Respuestas más contextuales
- [ ] Integración con CRM
- [ ] Notificaciones push
- [ ] Chat en tiempo real
- [ ] Transferencia a humano

## Soporte

¿Necesitas ayuda con el chatbot? Contacta:
- Email: info@fundeco.ec
- Teléfono: +593 99 123 4567
- Ubicación: Loja, Ecuador

---

**FUNDECO** - Innovación sostenible para la agricultura del futuro
