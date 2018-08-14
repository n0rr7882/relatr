PRELATR API Document
===================

# Index

## `/sign`

- `/sign/obtain/`
- `/sign/verify/`
- `/sign/refresh/`

## `/users`

- `/users/`
- `/users/{user_id}/`
- `/users/{user_id}/follow/`
- `/users/accounts/`
- `/users/accounts/{user_id}/`
- `/users/accounts/{user_id}/followings/`
- `/users/accounts/{user_id}/followers/`
- `/users/change-password/`

## `/chains`

- `/chains/`
- `/chains/timeline/`
- `/chains/{chain_id}/`
- `/chains/{chain_id}/parent-chain/`
- `/chains/{chain_id}/child-chains/`
- `/chains/{chain_id}/like/{account_id}/`

## `/notifications`

- 작업중

# `/sign/obtain/`

## POST

API View that receives a POST with a user's username and password.

Returns a JSON Web Token that can be used for authenticated requests.

### request

```http
Request Body
    username: string
    password: string
```

### response

```js
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOi..."
}
```

# `/sign/verify/`

## POST

API View that checks the veracity of a token, returning the token if it
is valid.

### request

```http
request Body
    token: string(token)
```

### response

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJ..."
}
```

# `/sign/refresh/`

## POST


API View that returns a refreshed token (with new expiration) based on
existing token

If 'orig_iat' field (original issued-at-time) is found, will first check
if it's within expiration window, then copy it to the new token

### request

```http
Request Body
    token: string(token)
```

### response

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJ..."
}
```

# `/users/`

## POST

### request

```http
Request Body
    username: string
    password: string
    first_name: string
    last_name: string
    email: string
```

### response

```json
{
    "id": 3,
    "thumbnail": null,
    "banner": null,
    "username": "testuser",
    "first_name": "Issac",
    "last_name": "Foster",
    "email": "test1234@gmail.com",
    "date_joined": "2018-08-13T15:58:17.739909Z"
}
```

## GET

### request

```http
Query String Parameters
    limit: number
    offset: number
```

### response

```json
{
    "count": 3,
    "next": null,       // 다음 자원 URI
    "previous": null,   // 이전 자원 URI
    "results": [
        {
            "id": 1,
            "thumbnail": null,
            "banner": null,
            "username": "norr",
            "first_name": "Dongho",
            "last_name": "Yu",
            "email": "n0rr7882@gmail.com",
            "date_joined": "2018-07-19T06:00:31.103179Z"
        }
    ]
}
```

# `/users/{user_id}/`

## GET

### response

```json

{
    "id": 1,
    "thumbnail": null,
    "banner": null,
    "username": "norr",
    "first_name": "Dongho",
    "last_name": "Yu",
    "email": "n0rr7882@gmail.com",
    "date_joined": "2018-07-19T06:00:31.103179Z"
}
```

## PUT

### request

```http
Request Headers
    Authorization: JWT <token>
Request Body
    username: string
    first_name: string
    last_name: string
    email: string
```

### response

```json
{
    "id": 1,
    "thumbnail": null,
    "banner": null,
    "username": "norr",
    "first_name": "DH",
    "last_name": "Yu",
    "email": "n0rr7882@gmail.com",
    "date_joined": "2018-07-19T06:00:31.103179Z"
}
```

## PATCH

### request

```http
Request Headers
    Authorization: JWT <token>
Request Body
    username?: string
    first_name?: string
    last_name?: string
    email?: string
```

### response

```json
{
    "id": 1,
    "thumbnail": null,
    "banner": null,
    "username": "norr",
    "first_name": "DH",
    "last_name": "Yu",
    "email": "n0rr7882@gmail.com",
    "date_joined": "2018-07-19T06:00:31.103179Z"
}
```

## DELETE

### request

```http
Request Headers
    Authorization: JWT <token>
```

### response

```
HTTP 204 No Content
```

# `/users/{user_id}/follow/`

## POST

### request

```http
Request Headers
    Authorization: JWT <token>
```

### response

```
HTTP 201 Creeated
```

## DELETE

### request

```http
Request Headers
    Authorization: JWT <token>
```

### response

```
HTTP 204 No Content
```

# `/users/accounts/`

## GET

### request

```http
Query String Parameters
    limit: number
    offset: number
```

### response

```json
{
    "count": 2,
    "next": null,       // 다음 자원 URI
    "previous": null,   // 이전 자원 URI
    "results": [
        {
            "id": 1,
            "user": {
                "id": 1,
                "thumbnail": null,
                "banner": null,
                "username": "norr",
                "first_name": "DH",
                "last_name": "Yu",
                "email": "n0rr7882@gmail.com",
                "date_joined": "2018-07-19T06:00:31.103179Z"
            },
            "thumbnail": null,
            "banner": null,
            "created_at": "2018-07-19T06:00:31.224239Z"
        }
    ]
}
```

# `/users/accounts/{user_id}`

## GET

### response

```json
{
    "id": 1,
    "user": {
        "id": 1,
        "thumbnail": null,
        "banner": null,
        "username": "norr",
        "first_name": "DH",
        "last_name": "Yu",
        "email": "n0rr7882@gmail.com",
        "date_joined": "2018-07-19T06:00:31.103179Z"
    },
    "thumbnail": null,
    "banner": null,
    "created_at": "2018-07-19T06:00:31.224239Z"
}
```

## PUT

### request

```http
Request Headers
    Authorization: JWT <token>
Request Files
    thumbnail: file(image)
    banner: file(image)
```

### response

```json
{
    "id": 1,
    "user": {
        "id": 1,
        "thumbnail": "http://localhost:8000/public/users/1/thumbnails/6be03543-7dd8-4299-9b5a-12090e925ff6.jpeg",
        "banner": "http://localhost:8000/public/users/1/banners/c7466a4a-0a98-4539-ae09-eac48650d625.jpeg",
        "username": "norr",
        "first_name": "DH",
        "last_name": "Yu",
        "email": "n0rr7882@gmail.com",
        "date_joined": "2018-07-19T06:00:31.103179Z"
    },
    "thumbnail": "http://localhost:8000/public/users/1/thumbnails/6be03543-7dd8-4299-9b5a-12090e925ff6.jpeg",
    "banner": "http://localhost:8000/public/users/1/banners/c7466a4a-0a98-4539-ae09-eac48650d625.jpeg",
    "created_at": "2018-07-19T06:00:31.224239Z"
}
```

## PATCH

### request

```http
Request Headers
    Authorization: JWT <token>
Request Files
    thumbnail?: file(image)
    banner?: file(image)
```

### response

```json
{
    "id": 1,
    "user": {
        "id": 1,
        "thumbnail": "http://localhost:8000/public/users/1/thumbnails/6be03543-7dd8-4299-9b5a-12090e925ff6.jpeg",
        "banner": "http://localhost:8000/public/users/1/banners/c7466a4a-0a98-4539-ae09-eac48650d625.jpeg",
        "username": "norr",
        "first_name": "DH",
        "last_name": "Yu",
        "email": "n0rr7882@gmail.com",
        "date_joined": "2018-07-19T06:00:31.103179Z"
    },
    "thumbnail": "http://localhost:8000/public/users/1/thumbnails/6be03543-7dd8-4299-9b5a-12090e925ff6.jpeg",
    "banner": "http://localhost:8000/public/users/1/banners/c7466a4a-0a98-4539-ae09-eac48650d625.jpeg",
    "created_at": "2018-07-19T06:00:31.224239Z"
}
```

## DELETE

### request

```http
Request Headers
    Authorization: JWT <token>
```

### response

```
HTTP 204 No Content
```

# `/users/accounts/{user_id}/followings/`

## GET

### request

```http
Request Headers
    Authorization: JWT <token>
Query String Parameters
    limit: number
    offset: number
```

### response

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "user": {
                "id": 2,
                "thumbnail": null,
                "banner": null,
                "username": "test",
                "first_name": "Harry",
                "last_name": "Lee",
                "email": "test1@gmail.com",
                "date_joined": "2018-07-20T03:16:03.788796Z"
            },
            "thumbnail": null,
            "banner": null,
            "created_at": "2018-07-20T03:16:03.920303Z"
        }
    ]
}
```

# `/users/accounts/{user_id}/followers/`

## GET

### request

```http
Request Headers
    Authorization: JWT <token>
Query String Parameters
    limit: number
    offset: number
```

### response

```json
{
    "count": 1,
    "next": null,       // 다음 자원 URI
    "previous": null,   // 이전 자원 URI
    "results": [
        {
            "id": 1,
            "user": {
                "id": 1,
                "thumbnail": "http://localhost:8000/public/users/1/thumbnails/6be03543-7dd8-4299-9b5a-12090e925ff6.jpeg",
                "banner": "http://localhost:8000/public/users/1/banners/c7466a4a-0a98-4539-ae09-eac48650d625.jpeg",
                "username": "norr",
                "first_name": "DH",
                "last_name": "Yu",
                "email": "n0rr7882@gmail.com",
                "date_joined": "2018-07-19T06:00:31.103179Z"
            },
            "thumbnail": "http://localhost:8000/public/users/1/thumbnails/6be03543-7dd8-4299-9b5a-12090e925ff6.jpeg",
            "banner": "http://localhost:8000/public/users/1/banners/c7466a4a-0a98-4539-ae09-eac48650d625.jpeg",
            "created_at": "2018-07-19T06:00:31.224239Z"
        }
    ]
}
```

# `/users/change-password/`

## PUT

### request

```http
Request Headers
    Authorization: JWT <token>
Request Body
    old_password: string
    new_password: string
```

### response

```
HTTP 204 No Content
```

# `/chains/`

## POST

### request

```http
Request Headers
    Authorization: JWT <token>
Request Body
    text: string
    parent_chain: number(chain_id)
Request Files
    image: file(image)
```

### response

```json
{
    "id": 1,
    "account": {
        "id": 1,
        "user": {
            "id": 1,
            "thumbnail": null,
            "banner": null,
            "username": "norr",
            "first_name": "DH",
            "last_name": "Yu",
            "email": "n0rr7882@gmail.com",
            "date_joined": "2018-07-19T06:00:31.103179Z"
        },
        "thumbnail": null,
        "banner": null,
        "created_at": "2018-07-19T06:00:31.224239Z"
    },
    "text": "이것은 #태그\r\n입니다. @test",
    "image": null,
    "tags": [
        {
            "id": 6,
            "name": "태그"
        }
    ],
    "mentions": [
        {
            "id": 2,
            "user": {
                "id": 2,
                "thumbnail": null,
                "banner": null,
                "username": "test",
                "first_name": "Harry",
                "last_name": "Lee",
                "email": "test1@gmail.com",
                "date_joined": "2018-07-20T03:16:03.788796Z"
            },
            "thumbnail": null,
            "banner": null,
            "created_at": "2018-07-20T03:16:03.920303Z"
        }
    ],
    "likes": [
        {
            "id": 2,
            "user": {
                "id": 2,
                "thumbnail": null,
                "banner": null,
                "username": "test",
                "first_name": "Harry",
                "last_name": "Lee",
                "email": "test1@gmail.com",
                "date_joined": "2018-07-20T03:16:03.788796Z"
            },
            "thumbnail": null,
            "banner": null,
            "created_at": "2018-07-20T03:16:03.920303Z"
        }
    ],
    "parent_chain": 4,
    "child_chains": [
        76, 77, 102
    ],
    "created_at": "2018-07-19T06:01:04.765431Z"
}
```

## GET

### request

```http
Request Headers
    Authorization: jWT <token>
Query String Parameters
    limit: number
    offset: number
```

### response

```json
{
    "count": 1,
    "next": null,       // 다음 자원 URI
    "previous": null,   // 이전 자원 URI
    "results": [
        {
            "id": 1,
            "account": {
                "id": 1,
                "user": {
                    "id": 1,
                    "thumbnail": null,
                    "banner": null,
                    "username": "norr",
                    "first_name": "DH",
                    "last_name": "Yu",
                    "email": "n0rr7882@gmail.com",
                    "date_joined": "2018-07-19T06:00:31.103179Z"
                },
                "thumbnail": null,
                "banner": null,
                "created_at": "2018-07-19T06:00:31.224239Z"
            },
            "text": "이것은 #태그\r\n입니다. @test",
            "image": null,
            "tags": [
                {
                    "id": 6,
                    "name": "태그"
                }
            ],
            "mentions": [
                {
                    "id": 2,
                    "user": {
                        "id": 2,
                        "thumbnail": null,
                        "banner": null,
                        "username": "test",
                        "first_name": "Harry",
                        "last_name": "Lee",
                        "email": "test1@gmail.com",
                        "date_joined": "2018-07-20T03:16:03.788796Z"
                    },
                    "thumbnail": null,
                    "banner": null,
                    "created_at": "2018-07-20T03:16:03.920303Z"
                }
            ],
            "likes": [
                {
                    "id": 2,
                    "user": {
                        "id": 2,
                        "thumbnail": null,
                        "banner": null,
                        "username": "test",
                        "first_name": "Harry",
                        "last_name": "Lee",
                        "email": "test1@gmail.com",
                        "date_joined": "2018-07-20T03:16:03.788796Z"
                    },
                    "thumbnail": null,
                    "banner": null,
                    "created_at": "2018-07-20T03:16:03.920303Z"
                }
            ],
            "parent_chain": 4,
            "child_chains": [
                76, 77, 102
            ],
            "created_at": "2018-07-19T06:01:04.765431Z"
        }       
    ]
}
```

# `/chains/timeline/`

## GET

### request

```http
Request Headers
    Authorization: jWT <token>
Query String Parameters
    limit: number
    offset: number
```

### response

```json
{
    "count": 1,
    "next": null,       // 다음 자원 URI
    "previous": null,   // 이전 자원 URI
    "results": [
        {
            "id": 1,
            "account": {
                "id": 1,
                "user": {
                    "id": 1,
                    "thumbnail": null,
                    "banner": null,
                    "username": "norr",
                    "first_name": "dh",
                    "last_name": "yu",
                    "email": "n0rr7882@gmail.com",
                    "date_joined": "2018-07-19t06:00:31.103179z"
                },
                "thumbnail": null,
                "banner": null,
                "created_at": "2018-07-19t06:00:31.224239z"
            },
            "text": "이것은 #태그\r\n입니다. @test",
            "image": null,
            "tags": [
                {
                    "id": 6,
                    "name": "태그"
                }
            ],
            "mentions": [
                {
                    "id": 2,
                    "user": {
                        "id": 2,
                        "thumbnail": null,
                        "banner": null,
                        "username": "test",
                        "first_name": "harry",
                        "last_name": "lee",
                        "email": "test1@gmail.com",
                        "date_joined": "2018-07-20t03:16:03.788796z"
                    },
                    "thumbnail": null,
                    "banner": null,
                    "created_at": "2018-07-20t03:16:03.920303z"
                }
            ],
            "likes": [
                {
                    "id": 2,
                    "user": {
                        "id": 2,
                        "thumbnail": null,
                        "banner": null,
                        "username": "test",
                        "first_name": "harry",
                        "last_name": "lee",
                        "email": "test1@gmail.com",
                        "date_joined": "2018-07-20t03:16:03.788796z"
                    },
                    "thumbnail": null,
                    "banner": null,
                    "created_at": "2018-07-20t03:16:03.920303z"
                }
            ],
            "parent_chain": 4,
            "child_chains": [
                76, 77, 102
            ],
            "created_at": "2018-07-19t06:01:04.765431z"
        }       
    ]
}
```

# `/chains/{chain_id}/`

## GET

### request

```http
Request Headers
    Authorization: JWT <token>
```

### response

```json
{
    "id": 1,
    "account": {
        "id": 1,
        "user": {
            "id": 1,
            "thumbnail": null,
            "banner": null,
            "username": "norr",
            "first_name": "dh",
            "last_name": "yu",
            "email": "n0rr7882@gmail.com",
            "date_joined": "2018-07-19t06:00:31.103179z"
        },
        "thumbnail": null,
        "banner": null,
        "created_at": "2018-07-19t06:00:31.224239z"
    },
    "text": "이것은 #태그\r\n입니다. @test",
    "image": null,
    "tags": [
        {
            "id": 6,
            "name": "태그"
        }
    ],
    "mentions": [
        {
            "id": 2,
            "user": {
                "id": 2,
                "thumbnail": null,
                "banner": null,
                "username": "test",
                "first_name": "harry",
                "last_name": "lee",
                "email": "test1@gmail.com",
                "date_joined": "2018-07-20t03:16:03.788796z"
            },
            "thumbnail": null,
            "banner": null,
            "created_at": "2018-07-20t03:16:03.920303z"
        }
    ],
    "likes": [
        {
            "id": 2,
            "user": {
                "id": 2,
                "thumbnail": null,
                "banner": null,
                "username": "test",
                "first_name": "harry",
                "last_name": "lee",
                "email": "test1@gmail.com",
                "date_joined": "2018-07-20t03:16:03.788796z"
            },
            "thumbnail": null,
            "banner": null,
            "created_at": "2018-07-20t03:16:03.920303z"
        }
    ],
    "parent_chain": 4,
    "child_chains": [
        76, 77, 102
    ],
    "created_at": "2018-07-19t06:01:04.765431z"
}
```

## PUT

### request

```http
Request Headers
    Authorization: JWT <token>
Request Body
    text: string
    parent_chain: number(chain_id)
Request Files
    image: file(image)
```

### response

```json
{
    "id": 1,
    "account": {
        "id": 1,
        "user": {
            "id": 1,
            "thumbnail": null,
            "banner": null,
            "username": "norr",
            "first_name": "dh",
            "last_name": "yu",
            "email": "n0rr7882@gmail.com",
            "date_joined": "2018-07-19t06:00:31.103179z"
        },
        "thumbnail": null,
        "banner": null,
        "created_at": "2018-07-19t06:00:31.224239z"
    },
    "text": "이것은 #태그\r\n입니다. @test",
    "image": null,
    "tags": [
        {
            "id": 6,
            "name": "태그"
        }
    ],
    "mentions": [
        {
            "id": 2,
            "user": {
                "id": 2,
                "thumbnail": null,
                "banner": null,
                "username": "test",
                "first_name": "harry",
                "last_name": "lee",
                "email": "test1@gmail.com",
                "date_joined": "2018-07-20t03:16:03.788796z"
            },
            "thumbnail": null,
            "banner": null,
            "created_at": "2018-07-20t03:16:03.920303z"
        }
    ],
    "likes": [
        {
            "id": 2,
            "user": {
                "id": 2,
                "thumbnail": null,
                "banner": null,
                "username": "test",
                "first_name": "harry",
                "last_name": "lee",
                "email": "test1@gmail.com",
                "date_joined": "2018-07-20t03:16:03.788796z"
            },
            "thumbnail": null,
            "banner": null,
            "created_at": "2018-07-20t03:16:03.920303z"
        }
    ],
    "parent_chain": 4,
    "child_chains": [
        76, 77, 102
    ],
    "created_at": "2018-07-19t06:01:04.765431z"
}
```

## PATCH

### request

```http
Request Headers
    Authorization: JWT <token>
Request Body
    text?: string
    parent_chain?: number(chain_id)
Request Files
    image?: file(image)
```

### response

```json
{
    "id": 1,
    "account": {
        "id": 1,
        "user": {
            "id": 1,
            "thumbnail": null,
            "banner": null,
            "username": "norr",
            "first_name": "dh",
            "last_name": "yu",
            "email": "n0rr7882@gmail.com",
            "date_joined": "2018-07-19t06:00:31.103179z"
        },
        "thumbnail": null,
        "banner": null,
        "created_at": "2018-07-19t06:00:31.224239z"
    },
    "text": "이것은 #태그\r\n입니다. @test",
    "image": null,
    "tags": [
        {
            "id": 6,
            "name": "태그"
        }
    ],
    "mentions": [
        {
            "id": 2,
            "user": {
                "id": 2,
                "thumbnail": null,
                "banner": null,
                "username": "test",
                "first_name": "harry",
                "last_name": "lee",
                "email": "test1@gmail.com",
                "date_joined": "2018-07-20t03:16:03.788796z"
            },
            "thumbnail": null,
            "banner": null,
            "created_at": "2018-07-20t03:16:03.920303z"
        }
    ],
    "likes": [
        {
            "id": 2,
            "user": {
                "id": 2,
                "thumbnail": null,
                "banner": null,
                "username": "test",
                "first_name": "harry",
                "last_name": "lee",
                "email": "test1@gmail.com",
                "date_joined": "2018-07-20t03:16:03.788796z"
            },
            "thumbnail": null,
            "banner": null,
            "created_at": "2018-07-20t03:16:03.920303z"
        }
    ],
    "parent_chain": 4,
    "child_chains": [
        76, 77, 102
    ],
    "created_at": "2018-07-19t06:01:04.765431z"
}
```

## DELETE

### request

```http
Request Headers
    Authorization: JWT <token>
```

### response

```
HTTP 204 No Content
```

# `/chains/{chain_id}/parent-chain/`

## GET

### request

```http
Request Headers
    Authorization JWT <token>
```

### response

```json
{
    "id": 1,
    "account": {
        "id": 1,
        "user": {
            "id": 1,
            "thumbnail": null,
            "banner": null,
            "username": "norr",
            "first_name": "dh",
            "last_name": "yu",
            "email": "n0rr7882@gmail.com",
            "date_joined": "2018-07-19t06:00:31.103179z"
        },
        "thumbnail": null,
        "banner": null,
        "created_at": "2018-07-19t06:00:31.224239z"
    },
    "text": "이것은 #태그\r\n입니다. @test",
    "image": null,
    "tags": [
        {
            "id": 6,
            "name": "태그"
        }
    ],
    "mentions": [
        {
            "id": 2,
            "user": {
                "id": 2,
                "thumbnail": null,
                "banner": null,
                "username": "test",
                "first_name": "harry",
                "last_name": "lee",
                "email": "test1@gmail.com",
                "date_joined": "2018-07-20t03:16:03.788796z"
            },
            "thumbnail": null,
            "banner": null,
            "created_at": "2018-07-20t03:16:03.920303z"
        }
    ],
    "likes": [
        {
            "id": 2,
            "user": {
                "id": 2,
                "thumbnail": null,
                "banner": null,
                "username": "test",
                "first_name": "harry",
                "last_name": "lee",
                "email": "test1@gmail.com",
                "date_joined": "2018-07-20t03:16:03.788796z"
            },
            "thumbnail": null,
            "banner": null,
            "created_at": "2018-07-20t03:16:03.920303z"
        }
    ],
    "parent_chain": 4,
    "child_chains": [
        76, 77, 102
    ],
    "created_at": "2018-07-19t06:01:04.765431z"
}
```

# `/chains/{chain_id}/child-chains/`

## GET

### request

```http
Request Headers
    Authorization: JWT <token>
Query String Parameters
    limit: number
    offset: number
```

### response

```json
{
    "count": 1,
    "next": null,       // 다음 자원 URI
    "previous": null,   // 이전 자원 URI
    "results": [
        {
            "id": 1,
            "account": {
                "id": 1,
                "user": {
                    "id": 1,
                    "thumbnail": null,
                    "banner": null,
                    "username": "norr",
                    "first_name": "dh",
                    "last_name": "yu",
                    "email": "n0rr7882@gmail.com",
                    "date_joined": "2018-07-19t06:00:31.103179z"
                },
                "thumbnail": null,
                "banner": null,
                "created_at": "2018-07-19t06:00:31.224239z"
            },
            "text": "이것은 #태그\r\n입니다. @test",
            "image": null,
            "tags": [
                {
                    "id": 6,
                    "name": "태그"
                }
            ],
            "mentions": [
                {
                    "id": 2,
                    "user": {
                        "id": 2,
                        "thumbnail": null,
                        "banner": null,
                        "username": "test",
                        "first_name": "harry",
                        "last_name": "lee",
                        "email": "test1@gmail.com",
                        "date_joined": "2018-07-20t03:16:03.788796z"
                    },
                    "thumbnail": null,
                    "banner": null,
                    "created_at": "2018-07-20t03:16:03.920303z"
                }
            ],
            "likes": [
                {
                    "id": 2,
                    "user": {
                        "id": 2,
                        "thumbnail": null,
                        "banner": null,
                        "username": "test",
                        "first_name": "harry",
                        "last_name": "lee",
                        "email": "test1@gmail.com",
                        "date_joined": "2018-07-20t03:16:03.788796z"
                    },
                    "thumbnail": null,
                    "banner": null,
                    "created_at": "2018-07-20t03:16:03.920303z"
                }
            ],
            "parent_chain": 4,
            "child_chains": [
                76, 77, 102
            ],
            "created_at": "2018-07-19t06:01:04.765431z"
        }       
    ]
}
```

# `/chains/{chain_id}/like/{account_id}/`

## POST

### request

```http
Request Headers
    Authorization: JWT <token>
```

### response

```
HTTP 201 Created
```

## DELETE

### request

```http
Request Headers
    Authorization: JWT <token>
```

### response

```
HTTP 204 No Content
```
