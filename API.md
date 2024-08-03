
# Documentação da API

Documento gerado a partir da documentação no Swagger, disponível na rota /docs na API.
Métodos e Funcionalidades da API listadas abaixo:

---

## Login

| Method | URL |
|--------|-----|
| POST | /auth/login |

#### Request Body
| Field | Type | Description | Required |
|-------|------|-------------|----------|
| username | string | email  | Required |
| password | string | password | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| token_type | string | bearer |
| access_token | string | - |

---

## Get Me

| Method | URL |
|--------|-----|
| GET | /users/me |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| token | query | bearer token | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| name  | string | - |
| email | string | - |

---

## Create User

| Method | URL |
|--------|-----|
| POST | /users/ |

#### Request Body
| Field | Type | Description | Required |
|-------|------|-------------|----------|
| name | string | -  | Required |
| email | string | -  | Required |
| password | string | -  | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| name | string |  |
| email | N/A |  |

---

## Get Playlists

| Method | URL |
|--------|-----|
| GET | /playlists/ |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| city_name | query | city name | Required |
| state_code | query | state | Required |
| country_code | query | country | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| coordinates | object | coordinates data |
| location | object | location data |
| weather | object | weather info |
| playlists | object | recommended playlists |


---

## List Favorites

| Method | URL |
|--------|-----|
| GET | /playlists/favorites |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| token | query | access_token | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| playlists | list[object] | list of favorites playlists |


---

## Create Favorite


| Method | URL |
|--------|-----|
| POST | /playlists/favorites |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| token | query | access token | Required |

#### Request Body
| Field | Type | Description | Required |
|-------|------|-------------|----------|
| weather | object | weather from /playlists | Required |
| playlist | object |  playlist from /playlists | Required |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| id | string | reference id |
| weather | object | weather info |
| playlist | object | favorited playlist |


---

## Delete Favorite

| Method | URL |
|--------|-----|
| DELETE | /playlists/favorites/{favorite_id} |

#### Parameters
| Name | In | Description | Required |
|------|----|-------------|----------|
| favorite_id | path | object id | Required |
| token | query | access token | Required |

##### Response (200)

---

## Get Health

| Method | URL |
|--------|-----|
| GET | /health |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| status | string | OK |

---

## Get Info

| Method | URL |
|--------|-----|
| GET | /info |

##### Response (200)
| Field | Type | Description |
|-------|------|-------------|
| app_name | string | name |
| developer_email | string | email |

---
