# ZSSN (Zombie Survival Social Network)

## Description
The world as we know it has fallen into an apocalyptic scenario. A laboratory-made virus is transforming human beings and animals into zombies, hungry for fresh flesh.

I, as a zombie resistance member (and the last survivor who knows how to code), was designated to develop a system to share resources between non-infected humans.

## Technologies
- Python 3.6
- Django 2.2
- Django-rest-framework 3.10
- SQLite

## Requirements
- [Python 3.6](https://www.python.org/downloads/)
- [Pipenv](https://pipenv-es.readthedocs.io/es/stable/)
- [Git](https://www.atlassian.com/git/tutorials/install-git)


## Running the project
> Note: If you don't have Python, Pipenv and/or Git installed, please, see the topic `Requirements`.

To run the project, you have to follow the steps below.

Clone the repository from Github:

```
git clone https://github.com/yuriscosta/zssn-api.git
```

Enter the directory and create a virtual enviroment:
```
cd zssn-api
pipenv --python 3.6
```

Activate the virtual enviroment:
```
pipenv shell
```

Install the dependencies:
```
pipenv install
```

Run the server:
```
./manage.py runserver
```

Run the tests:
```
./manage.py test
```

## Using the API

Now that you have run the server, you can access the endpoints listed below.

### Survivors
> Allowed HTTP methods: _get_, _post_ \
> Actions: _list_, _detail_, _create_

To __list__ all the survivors:
```
# Request
GET localhost:8000/survivors/
```

```
# Response
[
    {
        "id": 1,
        "last_location": {
            "id": 1,
            "latitude": 300611.5,
            "longitude": 300744.5
        },
        "inventory": {
            "id": 1,
            "water": 0,
            "food": 0,
            "medication": 2,
            "ammunition": 10
        },
        "name": "Fugiro Nakombi",
        "age": 60,
        "gender": "M",
        "infected_reports": 2,
        "is_infected": false
    },
    ...
]
```

To __detail__ a specific survivor:
```
# Request
GET localhost:8000/survivors/<int:id>/
```

```
# Response
{
    "id": 4,
    "last_location": {
        "id": 13,
        "latitude": 300611.5,
        "longitude": 300744.5
    },
    "inventory": {
        "id": 4,
        "water": 0,
        "food": 0,
        "medication": 2,
        "ammunition": 10
    },
    "name": "Satoshi Nakamoto",
    "age": 60,
    "gender": "M",
    "infected_reports": 3,
    "is_infected": true
}
```

To __create__ a survivor:
```
# Request
POST localhost:8000/survivors/
```

```
# Body
{
    "name": "James",
    "last_location": {
        "latitude": 107771,
        "longitude": 3075446
    },
    "inventory": {
        "water": 3,
        "food": 2,
        "medication": 1,
        "ammunition": 0
    },
    "age": 87,
    "gender": "M",
    "infected_reports": 0
}
```

```
# Response
{
    "id": 24,
    "last_location": {
        "id": 35,
        "latitude": 107771.0,
        "longitude": 3075446.0
    },
    "inventory": {
        "id": 14,
        "water": 3,
        "food": 2,
        "medication": 1,
        "ammunition": 0
    },
    "name": "James",
    "age": 87,
    "gender": "M",
    "infected_reports": 0,
    "is_infected": false
}
```

## Locations
> Allowed HTTP methods: _get_, _put_ \
> Actions: _list_, _update_

To __list__ all the locations:
```
# Request
GET localhost:8000/locations/
```

```
# Response
[
    {
        "id": 1,
        "latitude": 3006332.0,
        "longitude": 3006744.0
    },
    ...
    {
        "id": 25,
        "latitude": 3006431.0,
        "longitude": 3004744.0
    },
]
```

To __update__ a location:
```
# Request
PUT localhost:8000/locations/<int:id>/
```

```
# Body
{
    "latitude": 22222,
    "longitude": 111111
}
```

```
# Response
{
    "id": 10,
    "latitude": 22222.0,
    "longitude": 111111.0
}
```

## Flag Survivor
> Allowed HTTP methods: _post_ \
> Actions: _create_

To __flag__ as infected a survivor:
```
# Request
POST localhost:8000/flag-survivor/
```

```
# Body
{
    # Both values are ids from survivors
    author: 4,
    target: 5
}
```

```
# Response
{
    "id": 6,
    "date": "2019-08-14T06:01:05.957580Z",
    "author": 4,
    "target": 5
}
```

## Inventories
> Allowed HTTP methods: _get_ \
> Actions: _list_, _detail_

To __list__ all the inventories:
```
# Request
GET localhost:8000/inventories/
```

```
# Response
[
    {
        "id": 1,
        "water": 2,
        "food": 2,
        "medication": 1,
        "ammunition": 3
    },
    ...
    {
        "id": 25,
        "water": 1,
        "food": 1,
        "medication": 4,
        "ammunition": 1
    }
]
```

To __detail__ a specific inventory:
```
# Request
GET localhost:8000/inventories/<int:id>/
```

```
# Response
{
    "id": 1,
    "water": 2,
    "food": 2,
    "medication": 1,
    "ammunition": 3
}
```

## Trade
> Allowed HTTP methods: _post_ \
> Actions: _create_

### Details
Survivors can trade items among themselves.

To do that, they must respect the price table below, where the value of an item is described in terms of points.

Both sides of the trade should offer the same amount of points. For example, 1 Water and 1 Medication (1 x 4 + 1 x 2) is worth 6 ammunition (6 x 1) or 2 Food items (2 x 3).

| Item         | Points   |
|--------------|----------|
| 1 Water      | 4 points |
| 1 Food       | 3 points |
| 1 Medication | 2 points |
| 1 Ammunition | 1 point  |

```
# Request
POST http://localhost:8000/trade/
```

```
# Body
{
    "sender": 27,
    "receiver": 23,
    "sender_water": 0,
    "sender_food": 0,
    "sender_medication": 1,
    "sender_ammunition": 0,
    "receiver_water": 0,
    "receiver_food": 0,
    "receiver_medication": 0,
    "receiver_ammunition": 2
}
```

```
# Response
{
    "details": "The trade was successful."
}
```

## Reports
> Allowed HTTP methods: _get_ \
> Actions: _list_

To __list__ all reports:
```
# Request
GET localhost:8000/reports/
```

```
# Response
[
    {
        "description": "Percentage of non-infected survivors",
        "value": "88.24%"
    },
    {
        "description": "Percentage of infected survivors",
        "value": "11.76%"
    },
    {
        "description": "Points lost because of infected survivors",
        "value": 14
    },
    {
        "description": "Average amount of each kind of resource by survivor",
        "value": {
            "water": 2.93,
            "food": 2.6,
            "medication": 3.53,
            "ammunition": 3.6
        }
    }
]
```