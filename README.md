# juez-virtual-BP

Proyecto de IA para debate BP (British Parliamentary) usando web scraping y RAG (Retrieval-Augmented Generation).

## ¿Qué hace?

- Extrae mociones históricas desde torneos de debate mediante web scraping.
- Procesa manuales de BP para mejorar legibilidad y búsqueda semántica.
- Usa embeddings + FAISS para recuperación de contexto.
- Utiliza Groq + Llama 3 para:
  - responder preguntas sobre el manual,
  - buscar mociones similares,
  - generar nuevas mociones en español.

## Fuentes

- CMUDE
- Rosarista
- WUDC
- Tabbycat

## Stack

- Python
- FAISS
- Sentence Transformers
- Groq API
- Llama 3
- BeautifulSoup / Selenium

## Instalación

## Requerimientos

Python 12, instalar dependencias del requirements.txt

## .env

```env
GROQ_API_KEY=tu_api_key
```

## Referencias

- https://retorika.es/tabbycats/list
- https://drive.google.com/file/d/1zlFnq6pziaioZgtKljBM3IRAcIS4Oo1n/view
