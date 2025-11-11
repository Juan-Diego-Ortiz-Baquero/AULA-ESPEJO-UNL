# 📡 API Documentation - FUNDECO Chatbot

## Overview
La API del chatbot FUNDECO proporciona endpoints para interactuar con el asistente virtual especializado en agricultura sostenible.

## Base URL
```
http://localhost:5000/api
```

## Authentication
No se requiere autenticación para los endpoints públicos.

## Endpoints

### Chat Endpoint

#### `POST /api/chat`

Envía un mensaje al chatbot y recibe una respuesta.

**Request Body:**
```json
{
    "message": "¿Cuáles son los beneficios de las fundas biodegradables?"
}
```

**Response (Success):**
```json
{
    "response": "🌿 Las fundas biodegradables de FUNDECO ofrecen múltiples beneficios: son 100% naturales, se degradan sin contaminar, ahorran costos de limpieza y mejoran la imagen de tu negocio agrícola.",
    "status": "success"
}
```

**Response (Error):**
```json
{
    "error": "Mensaje vacío",
    "details": "No message provided"
}
```

**HTTP Status Codes:**
- `200 OK` - Respuesta exitosa
- `400 Bad Request` - Mensaje vacío o inválido
- `500 Internal Server Error` - Error del servidor

## Request Examples

### JavaScript (Fetch)
```javascript
fetch('/api/chat', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        message: '¿Cuáles son los precios?'
    })
})
.then(response => response.json())
.then(data => {
    console.log('Respuesta:', data.response);
});
```

### Python (requests)
```python
import requests

response = requests.post('http://localhost:5000/api/chat', 
    json={'message': '¿Cómo hago un pedido?'}
)

if response.status_code == 200:
    data = response.json()
    print(data['response'])
```

### cURL
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Información de contacto"}'
```

## Chat Modes

### 1. Intelligent Mode (OpenAI)
Cuando `OPENAI_API_KEY` está configurada:
- Respuestas dinámicas y contextuales
- Comprensión natural del lenguaje
- Personalización según el contexto

### 2. Demo Mode
Cuando OpenAI no está disponible:
- Respuestas predefinidas basadas en palabras clave
- Sistema de coincidencias simple
- Funcionalidad completa sin API externa

## Message Categories

El chatbot reconoce las siguientes categorías de mensajes:

| Categoría | Palabras Clave | Ejemplo |
|-----------|----------------|---------|
| Saludo | hola, buenos días, saludos | "¡Hola! ¿Cómo están?" |
| Productos | producto, funda, biodegradable | "¿Qué productos ofrecen?" |
| Beneficios | beneficio, ventaja, por qué | "¿Por qué elegir FUNDECO?" |
| Precios | precio, costo, cotización | "¿Cuáles son los precios?" |
| Contacto | contacto, teléfono, email | "¿Cómo los contacto?" |

## Error Handling

### Common Errors

1. **Empty Message**
   ```json
   {
       "error": "Mensaje vacío",
       "details": "No message provided"
   }
   ```

2. **Server Error**
   ```json
   {
       "error": "Error procesando mensaje",
       "details": "Internal server error details"
   }
   ```

3. **OpenAI API Error**
   - Automáticamente fallback a modo demo
   - Error logged en servidor
   - Usuario recibe respuesta demo

## Rate Limiting

Actualmente no hay límites de velocidad implementados. Para producción, se recomienda implementar:
- Rate limiting por IP
- Throttling de requests
- Cache de respuestas frecuentes

## Testing

### Unit Tests
```bash
# Ejecutar tests (cuando estén implementados)
python -m pytest tests/
```

### Manual Testing
1. Ejecutar servidor: `python src/api/app.py`
2. Usar herramientas como Postman o curl
3. Probar diferentes tipos de mensajes

## Configuration

### Environment Variables
```env
OPENAI_API_KEY=your_api_key_here  # Para modo inteligente
FLASK_ENV=development             # Para debugging
```

### Logging
Los logs incluyen:
- Requests de chat
- Errores de OpenAI
- Estados de inicialización

## Integration Examples

### Integración en HTML
```html
<div id="chat-container">
    <input type="text" id="messageInput" placeholder="Escribe tu mensaje...">
    <button onclick="sendMessage()">Enviar</button>
    <div id="chatResponse"></div>
</div>

<script>
async function sendMessage() {
    const message = document.getElementById('messageInput').value;
    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message})
    });
    
    const data = await response.json();
    document.getElementById('chatResponse').innerHTML = data.response;
}
</script>
```

### Integración con React
```jsx
import React, { useState } from 'react';

function ChatComponent() {
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState('');

    const sendMessage = async () => {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });
        
        const data = await res.json();
        setResponse(data.response);
    };

    return (
        <div>
            <input 
                value={message} 
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Mensaje..."
            />
            <button onClick={sendMessage}>Enviar</button>
            <div>{response}</div>
        </div>
    );
}
```

## Performance Considerations

1. **OpenAI Response Time**: 1-3 segundos típico
2. **Demo Mode**: <100ms respuesta
3. **Caching**: Considerar implementar para respuestas frecuentes
4. **Connection Pooling**: Para múltiples requests simultáneos

## Security Notes

- No se almacenan mensajes de usuarios
- API key de OpenAI debe estar en variables de entorno
- Validación de input implementada
- CORS configurado para desarrollo

## Future Enhancements

- [ ] Autenticación de usuarios
- [ ] Historial de conversaciones
- [ ] Métricas y analytics
- [ ] Webhooks para integraciones
- [ ] Support para multimedia
- [ ] Rate limiting avanzado
