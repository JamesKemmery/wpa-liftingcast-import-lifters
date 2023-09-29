import pandas as pd

def create_file():
    df = pd.read_csv("lifters.csv")
    lifters = df.values

    type_mapper_age_male = {
        "Sub Junior": "Men's Raw Sub-Junior",
        "Junior": "Men's Raw Junior",
        "Senior": "Men's Raw Open",
        "M1": "Men's Raw Master I",
        "M2": "Men's Raw Master II",
        "M3": "Men's Raw Master III",
        "M4": "Men's Raw Master IV",
    }

    type_mapper_age_female = {
        "Sub Junior": "Women's Raw Sub-Junior",
        "Junior": "Women's Raw Junior",
        "Senior": "Women's Raw Open",
        "M1": "Women's Raw Master I",
        "M2": "Women's Raw Master II",
        "M3": "Women's Raw Master III",
        "M4": "Women's Raw Master IV",
    }

    column_names =["name","team","lot","platform","session","flight","birthDate","memberNumber","gender","rawOrEquipped","division",
     "declaredAwardsWeightClass","bodyWeight","squatRackHeight","benchRackHeight","squat1","bench1","dead1",
     "wasDrugTested","phoneNumber","country","streetAddress","city","state","zipCode","email","emergencyContactName",
     "emergencyContactPhoneNumber","additionalItems"]

    import_df = pd.DataFrame(columns=column_names)

    for lifter in lifters:
        if lifter[1] == "Male":
            age_class = type_mapper_age_male[lifter[3]]
        else:
            age_class = type_mapper_age_female[lifter[3]]

        info = {"name": lifter[0], "team": "", "lot": "", "platform": "1", "session": lifter[4],
                "flight": lifter[5], "birthDate": "", "memberNumber": "", "gender": lifter[1],
                "rawOrEquipped": "Raw", "division": age_class, "declaredAwardsWeightClass": lifter[2], "bodyWeight": "",
                "squatRackHeight": "", "benchRackHeight": "", "squat1": "", "bench1": "",
                "dead1": "", "wasDrugTested": "N", "phoneNumber": "", "country": "", "streetAddress": "",
                "city": "", "state": "", "zipCode": "", "email": "", "emergencyContactName": "",
                "emergencyContactPhoneNumber": "", "additionalItems": ""}

        import_df = import_df.append(info, ignore_index=True)

    import_df.to_csv("liftingcast.csv", index=False)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_file()
