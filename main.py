import json

candidates = [
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
        "email": "elliot.reed@gmail.com",
        "company": "microsoft"
    },
    {
        "id": 4,
        "name": "Perry Cox",
        "email": "perry.cox+1@heart.com",
        "company": "microsoft"
    }
]
developers = [
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
        "company": ""
    },
    {
        "name": "Perry Cox",
        "email": "perry.cox@heart.com",
        "company": "microsoft"
    }
]


def add_matching_id_to_developer(candidates: list, developers: list) -> list:
    # Create dictionaries with keys for matching.
    candidates_by_email = {}
    candidates_by_name_company = {}
    for candidate in candidates:
        candidates_by_email[candidate["email"]] = candidate

        if not candidate["name"] or not candidate["company"]:
            continue

        company_name_key = f"{candidate['name']}_{candidate['company']}"
        candidates_by_name_company[company_name_key] = candidate

    # Add id to developer
    for developer in developers:
        if developer["email"] in candidates_by_email:
            developer["id"] = candidates_by_email[developer["email"]]["id"]
            continue

        company_name_key = f"{developer['name']}_{developer['company']}"
        if company_name_key in candidates_by_name_company:
            developer["id"] = candidates_by_name_company[company_name_key]["id"]

    return developers


if __name__ == "__main__":
    matched_people = add_matching_id_to_developer(candidates, developers)
    print(json.dumps(matched_people, indent=4))
