# Discord Role Verification API

A simple API to verify if a Discord user has a specific role in a given server.

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

