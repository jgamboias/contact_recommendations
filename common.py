import pandas as pd

def enrich_dataset(connections, users):
    
    # merge information on user
    connections = connections.merge(
        users,
        left_on='user_id',
        right_on='user_id'
    )
    connections = connections.rename(columns={
        "country_code": "country_code_user", 
        "city_id": "city_id_user",
        "company_id": "company_id_user",
        "discipline_id": "discipline_id_user"
    })

    # merge information on recommendaded user
    connections = connections.merge(
        users,
        left_on='recommended_contact_id',
        right_on='user_id'
    )
    connections = connections.rename(columns={
        "country_code": "country_code_rec", 
        "city_id": "city_id_rec",
        "company_id": "company_id_rec",
        "discipline_id": "discipline_id_rec"
    })

    # do they live in the same country?
    connections['same_country'] = 0
    connections.loc[
        connections['country_code_user'] == connections['country_code_rec'],
        'same_country'
        ] = 1

    # do they live in the same city?
    connections['same_city'] = 0
    connections.loc[
        connections['city_id_user'] == connections['city_id_rec'],
        'same_city'
        ] = 1

    # do they work in the same company?
    connections['same_company'] = 0
    connections.loc[
        connections['company_id_user'] == connections['company_id_rec'],
        'same_company'
        ] = 1

    # do they work in the same discipline?
    connections['same_discipline'] = 0

    connections.loc[
        connections['discipline_id_user'] == connections['discipline_id_rec'],
        'same_discipline'
        ] = 1
    
    return connections