# Vast-api 

Backend api test project using FastApi & sqlite 

## Structure
- main.py - main app 
- config.py - contain external api url and extra configuration variables.
- routes - contain route endpoints.
- models.py - contains database models. 
- schemas.py - contains api model schemas.
- database.py - contains database configuration.

## Build 
Use Docker-Compose to spin up containers `docker-compose up`

## Notes
1. All client checks has done on 'username' field only.
2. You can aplay the same logic on 'sdk_version' field.

## Main route
Main api url: `localhost:8000`

## Documentation
Documentation url:  `localhost:8000/docs`



