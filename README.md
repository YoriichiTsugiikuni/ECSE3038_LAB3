# Lab 3

Please read the entire document before submitting your repo.

## Aim

This lap is meant to get students more accustomed to the technologies used in designing and implementing a RESTful API server.

## Requirements

The specifications have shifted slightly since the last developer meeting. Your client's budget recently increased and now they're able to pay for a database service. You've done your research and found that MongoDB is the most suitable database platform for the project. With this new information, the client has asked that you modify the API server to store all `Tank` related data to be stored in the database. The `Profile` data can be handled the same way as it was originally implemented, where the profile data is saved in a variable on the server. If you want to modify the `Profile` routes to save the data in the database as well, you may, but you don't have to (you won't get extra marks if you do and you won't lose marks if you don't).

You'll need to sign up on the MongoDB website, create a project and add a cluster to your project.

The following routes should be modified to support the use of the mongodb database.

```jsx
GET /data
POST /data
PATCH /data/:id
DELETE /data/:id
```

**GET /data**

As previously implemented, when this route is requested, the server should respond with an array of zero or more tank objects.

When there are no tanks in the db:

```jsx
GET /data

Expected Response
[]
```

When the table used to store tank data is populated:

```jsx
GET /data

Expected Response
[
    {
        "_id": {
            "$oid": "602bd7955b1c30eb21b821c5"
        },
        "location": "Nardo's",
        "lat": "18.00481892242301",
        "long": "-76.74592179547767",
        "percentatge_full": 100,
    },
		.
		.
		.
]
```

**POST /data**

Just as previously implemented, the server should be able to handle a POST request that consumes a JSON body, validates it against schema and returns the saved document.

**The server should respond an appropriate error message and error code when JSON body sent to the server is malformed.**

```jsx
POST /data

Example Request
{
    "location": "Physics department",
    "lat": "18.004741066082236",
    "long": "-76.74875280426826",
    "percentage_full": 56
}

Expected Response
{
		"_id": {
        "$oid": "6c3055b121bd79821ceb02b6"
    },
    "location": "Physics department",
    "lat": "18.004741066082236",
    "long": "-76.74875280426826",
    "percentage_full": 56
}
```

**PATCH /data/:id**

As previously implemented, your server should allow a user to alter the parts of one of the tanks after it has been posted. The server should allow the requester to make a JSON body with any combination of the four attributes and update them as necessary (The requester should NOT be allowed to edit the `id` attribute). The server should respond with the edited document.

**The server should respond with an appropriate error message and error code when the JSON body sent to the server is malformed.**

```jsx
PATCH /data/:id

Example Request
{
    "location": "<new location>", //optional
    "lat": "<new lat>", //optional
    "long": "<new long>", //optional
    "percentage_full": "<new percentage_full>" //optional
}

Expected Response
{
		"_id": {
        "$oid": "<id>"
    },
    "location": "<updated location>",
    "lat": "<updated lat>",
    "long": "<updated long>",
    "percentage_full": "<updated percentage_full>"
}
```

**DELETE /data/:id**

Your server should allow the requester to delete any previously POSTed object.

**The server should respond an appropriate error message and error code when the input ID of the required tank object does not exist.**

```jsx
DELETE /data/:id

Expected Response
{
    "success": true
}
```

## Submission

Your code should be uploaded to your GitHub account.

The repo should be called "ECSE3038_lab3".

**Your main python script must be called app.py.**

**The application must be hosted on all IP address of the server.**

**The application must listen for incoming request on port 3000.**

You should include a .gitignore file that omits any file that isn’t the [app.py](http://app.py) and requirements.txt.

You should include a [README.md](http://readme.md/) file that describes the purpose and operation of your API.

Python repos should also contain a requirements.txt file with a list of all the packages used in the project.

Due date is Sunday, February 13, 2022 at 11:59PM.

You're only required to provide a link to your GitHub repository.

Any commits made to the repo after the due date will not be considered.
