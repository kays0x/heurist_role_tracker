## API Usage

Endpoint: `POST /api/verify`

Request Body:
```json
{
  "discord": "USER_ID",
  "role_id": "ROLE_ID"
}
```

Response:
```json
{
  "error": {
    "code": 0,
    "message": ""
  },
  "data": {
    "result": true | false
  }
}
```

