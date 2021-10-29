# this is our backend

set up by cloning, cd to the base folder, then setting up a python virtual environment 
and activating it (if you don't know how, you can google this)

then install the packages. in terminal:
```
pip install -r requirements.txt
```
Then set up the Django project as according to the youtube tutorial sent over slack.
Make sure you can run in locally with no issues.

# API endpoints documentation 

## GET request to: userprofile/favorites/<str:id>
Where id = the id field of the user. Returns a dictionary form list of all of the favorite items of the user as well as the item info. 

Error handles to check if user and item exists.

for example, a GET request to http://localhost:8000/userprofile/favorites/0 might return: 
```
{
    "0": {
        "id": 0,
        "seller": 0,
        "title": "Book",
        "description": "this is a book",
        "price": 1,
        "sold": false,
        "condition": "ok"
    },
    "1": {
        "id": 1,
        "seller": 0,
        "title": "Tree",
        "description": "fjdkslaf;dsa",
        "price": 3,
        "sold": false,
        "condition": "good"
    }
}
```

## PUT request to: userprofile/newfavorite/<str:userid>
Where id = the id field of the user. If successful, returns json dict of the favorite object created and saved to database.

Error handles to check if item and object exists and the data is in valid json dict form for saving to database.

for example, a PUT request to http://localhost:8000/userprofile/favorites/0 with the data body:
```
{
    "user": 0, 
    "item":"0"
}
```

will return: 
```
{
    "user": 0, 
    "item":"0"
}
```

