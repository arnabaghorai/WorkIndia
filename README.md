# API

Start server:

`cd notes`

`python run.py`

endpoints:

> `/app/user` - METHOD `POST`

Response:

```@json
{'status' : 'Account created!'}

```

Status Code - `201`

> `/app/user/auth` - Method `POST`

```@json
{'status' : 'Success' , "userId" : 2}

```

Status Code - `200`




> `/app/sites/?user=1` - Method `POST`

```@json
{'status' : 'success'}

```

Status Code - `201`

> `/app/sites/list/?user=1` - Method `GET`

```@json
{
  "notes": [
    {
      "id": 1,
      "note": "yo"
    }
  ]
}

```

Status Code - `200`

