# todoapp

This application is an API for a todo app which is written using the python django rest framework and mysql backend which is going to give users of the application access to 3 endpoints which includes:

    1. Users are able to create a todo using the "/api/task-create." endpoint.
        a POST request is sent to the "/api/task-create/ endpoint with the following parameters:

        task-name: a string which signifies task name
        completed: a boolean true or false to determine if task has been completed or not


    2. Users are able to view tasks that has been created using the "api/task-list/" endpoint.
        a GET request is sent to the "/api/task-list/" endpoint which return all the list that has been added.

    3. Users are able to update task if it has been completed using the id of the task and the "/api/task-update/<id>" endpoint.
        a POST request is sent to the "/api/task-update/<id>" endpoint with the following parameters:

            id: id of the task to be updated
            completed: boolean true or false to toggle if the task hae been completed or not


The api return is json formatted and has been sorted according to the datetime of last updated which is the completed_at field. This is automatically generated when the task is updated.

The application has been containerized and a server.sh script has been written for ease of deployment to any kubernetes cluster.

To run the deployment, 

RUN sh server.sh to execute the script which runs the deployment

Automated tests were also added to test validity of the endpoints. To run the tests, a script has been written to run this which is sh test.sh.