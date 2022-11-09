#  Mermaid 실습
- 순서도
    - 첫번째 샘플
```mermaid 
classDiagram 
    class Person{
        +name : str
        +phoneNumber : str
        +emailAddress : str 
        +purchaseParkingPass()
    }
    class Address{
        +street: str
        +city:str
        +state: str
        +postalCode: int
        +contry: str
        -vaildate() : bool
        +outputAsLabel(): str
    }
    class Student{
        +studentNumber: int
        +averageMark: int
        +isEligibleToEnroll(str): bool
        +getSeminarsTaken(): int
    }
    class Professor{
        /salary: int
        #staffNumber: int
        -yearOfService: int
        +numberOfClasses: int
    }

    Student"0..*" <-- "1..5" Professor : supervises
    Person <-- Student
    Person <-- Professor
    Address "1"<--"0..1" Person : lives at
```

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

```mermaid
sequenceDiagram
    participant User
    participant Client
    participant Server
    participant Database
    
    User ->> Client: Fill username
    User ->> Client: Fill password
    Client ->> User: Enable "Login" button
    User ->> Client : Click "Login" button
    Client ->> Server : POST/login
    
    activate Server
    Server ->> Database: SELECT FROM users
    
    activate Database
    Note over Server , Database : See login.py for impl. details
    
    Database -->> Server: results 
    deactivate Database
    
    Server -->> Client: {authenticated: true}
    deactivate Server
    Client ->> User: redirect / home
```












<!-- ```mermaid
sequenceDiagram
    participant A as Data Updater
    participant B as DB
    loop 1시간마다 수행
        A ->> B: send update data
        B ->> A: update result
    end
``` -->
<!-- ```
flowchart 
    a([밥을 먹지 않았다])
    b{{String status = hunger  <br> String food = nothing}}
    c{배가 고픈가}
    d{먹을 것이 있는가?}
    e[밥을 먹는다]
    f[밥을 먹는다]
    g([end])
    aa[배불러]
    a -- b -- c --|yes| d --|yes| e -- f -- g
    h[안 먹는다.]
    i[먹지 않는다.]
    c --|no|aa -- h
    d --|no| h -- i--g
``` -->