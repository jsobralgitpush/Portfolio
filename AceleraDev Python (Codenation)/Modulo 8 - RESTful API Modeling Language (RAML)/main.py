
doc = '''
#%RAML 1.0


securitySchemes:
    JWT:
        description: Auth JWT
        type: string
        describedBy:
            headers:
                Authorization:
                    type: string
                    required: true
            responses:
                201:
                    body: 
                        application/json:
                            description: Token was generated
                404:
                    body: 
                        application/json:
                            description: Not found
        settings:
            roles: []


    
types:
    Auth:
        type: object
        discriminator: token
        properties:
            token : string
     
    User:
        type: object
        discriminator: user
        properties:
            user_id:
                type: integer
                required: true
                example: 1
            name:
                type: string
                required: true
                example: "name"
            email:
                type: string
                format: email
                required: true
                example: "email@example.com"
            last_login:
                type: string
                format: date
                required: true
                example: "2019-11-20"
            group_id: 
                type: integer
                required: true
                example: 1
        example:
            user_id: 1
            name: "name"
            email: "email@example.com"
            last_login: "2019-11-20"
            group_id: 1
                
    Group:
        type: object
        discriminator: group
        properties:
            group_id:
                type: integer
                required: true
                example: 1
            name:
                type: string
                required: true
                example: "name"
        example:
            group_id: 1
            name: "group"
    
    Agent:
        type: object
        discriminator: agent
        properties:
            agent_id:
                type: integer
                required: true
                example: 1
            name:
                type: string
                required: true
                example: "name"
            status:
                type: boolean
                required: true
                example: true
            environment:
                type: string
                required: true
                example: "environment"
            version:
                type: string
                required: true
                example: "version"
            address:
                type: string
                required: true
                example: "address"
            user_id:
                type: integer
                required: true
                example: 1
        example:
            agent_id: 1
            user_id: 1
            name: "name"
            status: true
            environment: "environment"
            version: "version"
            address: "address"
    
    
    Event:
        type: object
        discriminator: event
        properties:
            event_id:
                type: integer
                required: true
                example: 1
            agent_id:
                type: integer
                required: true
                example: 1
            level:
                type: string
                required: true
                example: "level"
            payload:
                type: string
                required: true
                example: "payload"
            shelved:
                type: boolean
                required: true
                example: true
            date:
                type: string
                format: date-time
                required: true
                example: "2018-11-26T16:17:18Z"
        example:
            event_id: 1
            agent_id: 1
            level: "level"
            payload: "payload"
            shelve: true
            data: "2018-11-26T16:17:18Z"
                
    Response:
        discriminator: response
        properties:
            message:
                type: string
                example: "example"
            
/auth/token:
    get:
        description: Get a JWT Token
        response:
            200:
                body:
                    type: Response
                example:
                    message: Successfully generated token
            401:
                body:
                    type: Response
                example:
                    message: Unauthorized 
            404:
                body:
                    type: Response
                example:
                    message: Not found
            
    post:
        description: Send a JWT to validated it
        body:
            application/json:
                type: string
                username: string
                password: string
        responses: 
            201:
                body: 
                    application/json:
                        description: Valid Token
            400:
                body: 
                    application/json:
                        description: Invalid Token
        securedBy: [JWT]
    
           
/agents:
    get:
        description: Return list agents
        responses: 
            200:
                body:
                    type: Response
                example:
                    message: Created
            401:
                body:
                    type: Response
                example:
                    message: Unauthorized
            404:
                body:
                    type: Response
                example:
                    message: Not Found
        securedBy: [JWT]

    post:
        description: New Agent
        body: 
            application/json:
                example: {
                    "agent_id": 1,
                    "user_id": 1,
                    "name": "name",
                    "status": true,
                    "environment": "environment",
                    "version": "version",
                    "address": "address"
                    }
        responses: 
            201:
                body:
                    type: Response
                example:
                    message: Created

            401:
                body:
                    type: Response
                example:
                    message: Unauthorized
        securedBy: [JWT]

    /{id}:
        get:
            description: Agent detail
            responses: 
                200:
                    body:
                        type: Response
                    example:
                        message: Created
                401:
                    body:
                        type: Response
                    example:
                        message: Unauthorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found
            securedBy: [JWT]

        put:
            responses:
                200:
                    body:
                        type: Response
                    example:
                        message: Created
                401:
                    body:
                        type: Response
                    example:
                        message: Unauthorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found
            securedBy: [JWT]

        delete:
            description: Delete Agent
            responses:
                200:
                    body:
                        type: Response
                    example:
                        message: Created
                401:
                    body:
                        type: Response
                    example:
                        message: Unauthorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found
            securedBy: [JWT]

    /{id}/events:
        get:
            description: Events list
            responses:
                200:
                    body:
                        type: Event
                401:
                    body:
                        type: Response
                    example:
                        message: Unauthorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found
            securedBy: [JWT]

        post:
            body: 
                application/json:
                    example: {
                        "event_id": 1,
                        "agent_id": 1,
                        "level": "level example",
                        "data": "payload example",
                        "shelve": true
                        }
                201:
                    body:
                        type: Response
                    example:
                        message: Created
                401:
                    body:
                        type: Response
                    example:
                        message: Unauthorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found
            securedBy: [JWT]

        put:
            description: Update Event
            body:
                type: Event
                
                200:
                    body:
                        type: Response
                    example:
                        message: Created
                401:
                    body:
                        type: Response
                    example:
                        message: Unauthorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found
            securedBy: [JWT]

        delete:
            description: Delete Event
            body: 
                application/json:
                    properties: 
                        example: {}

                200:
                    body:
                        type: Response
                    example:
                        message: Created
                401:
                    body:
                        type: Response
                    example:
                        message: Unauthorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found  
            securedBy: [JWT]
            
    /{id}/events/{id}:
        get:
            description: A single Event
            responses:
                200:
                    body:
                        type: Event
                401:
                    body:
                        type: Response
                    example:
                        message: Unauthorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found
            securedBy: [JWT]
         
        put:
            description: Update Event
            body:
                type: Even
                200:
                    body:
                        type: Response
                    example:
                        message: Updated
                401:
                    body:
                        type: Response
                    example:
                        message: Unauthorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found
            securedBy: [JWT]

        delete:
            description: Delete Event
            body: 
                application/json:
                    properties: 
                        example: {}
            responses:
                200:
                    body:
                        type: Response
                    example:
                        message: Created
                401:
                    body:
                        type: Response
                    example:
                        message: Unauthorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found  
            securedBy: [JWT]

        
/groups:
    get:
        description: Group list
        responses:
            200:
                body:
                    type: Group
            401:
                body:
                    type: Response
                example:
                    message: Not Authorized
        securedBy: [JWT]

    post:
        description: Create Group
        body:
            application/json:
                properties: 
                    example: {
                        "group_id": 1,
                        "name": "group"
                        }
                example: {
                    "group_id": 1,
                    "name": "group"
                    }
        responses:
            201:
                body:
                    type: Group
            401:
                body:
                    type: Response
                example:
                    message: Not Authorized
        securedBy: [JWT]

    /{id}:
        get:
            description: Group detail
            responses:
                200:
                    body:
                        type: Group
                401:
                    body:
                        type: Response
                    example:
                        message: Not Authorized
                404:
                    body:
                        type: Response
                        example:
                            message: Not Found
            securedBy: [JWT]

        put:
            description: Edit Group
            body:
                type: Group
            responses:
                200:
                    body:
                        type: Group
                401:
                    body:
                        type: Response
                    example:
                        message: Not Authorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found
            securedBy: [JWT]

        delete:
            description: Delete Group
            responses:
                204:
                    body:
                        type: Response
                    example:
                        message: Deleted 
                401:
                    body:
                        type: Response
                    example:
                        message: Not Authorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found
            securedBy: [JWT]
    
/users:
    get:
        description: User list
        responses:
            200:
                body:
                    type: User
        securedBy: [JWT]

    post:
        description: Create User
        body:
            application/json:
                properties:
                    example: {
                        "user_id": 1,
                        "name": "name",
                        "email": "email",
                        "last_login": "2019-11-20",
                        "group_id": 1
                        }
        responses:
            201:
                body:
                    type: User
            401:
                body:
                    type: Response
                example:
                    message: Unauthorized
            404:
                body:
                    type: Response
                example:
                    message: Not Found
        securedBy: [JWT]

    /{id}:
        get:
            description: User detail
            responses:
                200:
                    body:
                        type: User
                401:
                    body:
                        type: Response
                    example:
                        message: Unauthorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found  
            securedBy: [JWT]

        put:
            description: Edit User
            body:
                type: User
            responses:
                200:
                    body:
                        type: User
                    example:
                        message: User created 
                401:
                    body:
                        type: Response
                    example:
                        message: Unauthorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found
            securedBy: [JWT]

        delete:
            responses:
                200:
                    body:
                        type: Response
                    example:
                        message: Deleted
                401:
                    body:
                        type: Response
                    example:
                        message: Unauthorized
                404:
                    body:
                        type: Response
                    example:
                        message: Not Found
            securedBy: [JWT]
 
'''
