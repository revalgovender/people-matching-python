# People Matching Code Task (45min time limit)

## Contents

1. [Task Description](#task-description)
2. [My solution](#my-solution)
3. [Future Improvements](#future-improvements)

## Task Description

Given two lists with personal data of people (name, email, company)

### Candidates

```json
[
  {
    "id": 1,
    "name": "John Dorian",
    "email": "jd@yahoo.com",
    "company": ""
  },
  {
    "id": 2,
    "name": "Chris Turk",
    "email": "chris.turk@gmail.com",
    "company": "iotech"
  },
  {
    "id": 3,
    "name": "Elliot Reed",
    "email": "elliot.reed+1@gmail.com",
    "company": "microsoft"
  },
  {
    "id": 4,
    "name": "Perry Cox",
    "email": "perry.cox+1@heart.com",
    "company": "microsoft"
  }
]
```

### Developers

```json
[
  {
    "name": "John Dorian",
    "email": "john.dorian@yahoo.com",
    "company": "google"
  },
  {
    "name": "Chris Turk",
    "email": "chris.turk@gmail.com",
    "company": "netflix"
  },
  {
    "name": "Elliot Reed",
    "email": "elliot.reed@gmail.com",
    "company": "microsoft"
  },
  {
    "name": "Perry Cox",
    "email": "perry.cox@heart.com",
    "company": "microsoft"
  }
]

```

### Goal

Add the candidate ids to the corresponding developer entries if you find a match.

#### Limitations

A match is defined as one of the following:

- Exact match of the email addresses
- The same combination of name and company (both values need to be defined)

Assume that each array will contain millions of entries - performance is important.

## My Solution

```bash
$ python main.py                                               
{                                        
    "john.dorian@yahoo.com": {           
        "name": "John Dorian",           
        "email": "john.dorian@yahoo.com",
        "company": "google"              
    },                                   
    "chris.turk@gmail.com": {            
        "name": "Chris Turk",            
        "email": "chris.turk@gmail.com", 
        "company": "netflix",            
        "id": 2                          
    },                                   
    "elliot.reed@gmail.com": {           
        "name": "Elliot Reed",
        "email": "elliot.reed@gmail.com",
        "company": "",
        "id": 3
    },
    "perry.cox@heart.com": {
        "name": "Perry Cox",
        "email": "perry.cox@heart.com",
        "company": "microsoft",
        "id": 4
    }
}
```

## Future Improvements

- Add more tests
- Maybe add more comments to make code easier to understand