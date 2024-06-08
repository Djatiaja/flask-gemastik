
# Flask Backend





## Installation

Install my-project with npm

```bash
  pip install -r requirement.txt
```
    
## API Reference

#### Get data tempat wisata

```http
  GET /tempat_wisata/<int:tempat_wisata_id>
```

| Parameter      | Type        | Description                             |
|----------------|-------------|-----------------------------------------|
| `id`           | Integer     | Unique identifier for the place.        |
| `name`         | String      | Name of the place.                      |
| `description`  | String      | Description of the place.               |
| `category`     | String      | Category of the place.                  |
| `city`         | String      | City where the place is located.        |
| `price`        | Float       | Price associated with the place.        |
| `rating`       | Float       | Rating of the place.                    |
| `time_minutes` | String      | Time in minutes.                        |
| `coordinate`   | String      | Coordinate details.                     |
| `lat`          | Float       | Latitude of the place.                  |
| `long`         | Float       | Longitude of the place.                 |

#### Get rekomendasi tempat wisata

```http
  GET /get_recommendation/<int:tempat_wisata_id>
```
bakal ada json dengan Parameter tempat_wisata_id dengan nilai sebagai berikut

| Parameter      | Type        | Description                             |
|----------------|-------------|-----------------------------------------|
| `id`           | Integer     | Unique identifier for the place.        |
| `name`         | String      | Name of the place.                      |
| `description`  | String      | Description of the place.               |
| `category`     | String      | Category of the place.                  |
| `city`         | String      | City where the place is located.        |
| `price`        | Float       | Price associated with the place.        |
| `rating`       | Float       | Rating of the place.                    |
| `time_minutes` | String      | Time in minutes.                        |
| `coordinate`   | String      | Coordinate details.                     |
| `lat`          | Float       | Latitude of the place.                  |
| `long`         | Float       | Longitude of the place.                 |


#### Create User
```http
  POST /create_user
```

| Parameter      | Type   | Description                            |
|----------------|--------|----------------------------------------|
| `Nama_lengkap` | String | Full name of the user.                 |
| `Email`        | String | Email address of the user.             |
| `Password`     | String | Password of the user (plain text, not hashed). |
| `Jenis_kelamin`| String | Gender of the user.                    |
| `Tanggal_lahir`| String | Date of birth of the user.             |

### Login

```http
  POST /login
```
| Parameter      | Type   | Description              |
|----------------|--------|--------------------------|
| `Email`        | String | Email address of the user.|
| `Password`     | String | Password of the user.     |

### Logout

```http
  POST or GET /Logout
```

### Check apakah user login
```http
  GET /api/status
```

Jika login 
| Parameter | Type   | Description                           |
|-----------|--------|---------------------------------------|
| `status`  | String | Logged in                             |
| `user`    | String | Representation of the logged-in user. |

jika tidak login
| Parameter | Type   | Description                           |
|-----------|--------|---------------------------------------|
| `status`  | String | Not logged in                         |

### Get current user login
```http
  GET /api/user
```
| Parameter      | Type   | Description                            |
|----------------|--------|----------------------------------------|
| `Nama_lengkap` | String | Full name of the user.                 |
| `Email`        | String | Email address of the user.             |
| `Password`     | String | Password of the user (plain text, not hashed). |
| `Jenis_kelamin`| String | Gender of the user.                    |
| `Tanggal_lahir`| String | Date of birth of the user.             |
