# Essay Evaluation API

An AI-powered API that evaluates essay answers against questions using Google's Gemini model.

## Setup

1. Clone the repository
2. Create a `.env` file with:

```
   GEMINI_API_KEY=your_api_key_here
```

3. Install dependencies:

```bash
   pip install -r requirements.txt
```

## Running Locally

```bash
uvicorn main:app --reload
```

Server runs on `http://localhost:8000`

## API Usage

### Endpoint: POST `/evaluate`

**Request Format:**

```json
{
  "content": "$Question$Answer"
}
```

**Example:**

```bash
curl -X POST "http://localhost:8000/evaluate" \
  -H "Content-Type: application/json" \
  -d '{"content": "$What is photosynthesis?$Photosynthesis is the process by which plants convert sunlight into chemical energy."}'
```

**Response:**

```json
{
  "mark": 75
}
```

**Notes:**

- Format: `$Question$Answer` (exactly two dollar signs)
- Mark: 0 if answer unrelated, 1-100 if related
- Temperature set to 0.1 for consistent evaluation

## Deployment on Render

1. Push to GitHub
2. Connect repo to Render
3. Add environment variable `GEMINI_API_KEY`
4. Deploy with:

```
   uvicorn main:app --host 0.0.0.0
```

## Available Methods

- `GET /` - Health check
- `POST /evaluate` - Evaluate essay answer
