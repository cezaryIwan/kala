# Project start up for development:
### go to kala/docker directory
-----
### run ``` docker compose up ```
-----
### after a while you should see all 4 containers running correctly
-----
### project is running in debug mode, so you'll have to add launch.json file in .vscode folder. This setup should work for you:

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Docker Attach Debug",
            "type": "debugpy",
            "request": "attach",
            "connect": {
                "host": "localhost", 
                "port": 5678 
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}/server", 
                    "remoteRoot": "/app" 
                }
            ],
            "justMyCode": true 
        }
    ]
}
```
#### with that setup you can run 'Python: Docker Attach Debug' in debug section
-----
### go to: 
#### localhost:5137 for client
#### localhost:8000/docs for swagger of server
#### localhost:5050 for pgadmin
-----
### unfortunatelly, you'll have to add database in pgadmin, authenticate and propagate database properties using docker-compose.yaml.db and docker-compose.yaml.pgadmin services:
-----
#### login with admin@admin/password
-----
#### propagate with:
#### general tab -> name: e.g. kala
#### connection tab -> host:db
#### connection tab -> port:5432
#### connection tab -> username:root
#### connection tab -> password:password
