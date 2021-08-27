import random
import json
from auth import generate_form_data_payload

import requests
import names
import asyncio
from datetime import date, datetime, timedelta

LOCALHOST = 'http://localhost'
TFDEV = 'https://tfdev.screel.in'
DEV = 'http://dev.screel.in'

BASE_URL = LOCALHOST


# docs 
docs_path='/mnt/d/kalingaraj/screel labs/poc/'
for_nurse = 'Nurse_Resume_Template'
for_dentist='Dentist_Doctor_Resume_Template'
others = 'Sample_Doctor_Resume_Template.pdf'

def attach_docs(candidate_type_id:int):
    if candidate_type_id == 4:
        return docs_path+for_nurse
    elif candidate_type_id == 6:
        return docs_path+for_dentist
    else:
        return docs_path+others


# const
# customer_uid = 8
# organisation_id=7
# candidate_type_id=1
# candidate_uid = 7505 #auto-gen
# country_id=181  #  random


# access_token = None
# [ auth ]

# ------WebKitFormBoundaryYrMFkLgguOYlHqSk
# Content-Disposition: form-data; name="username"

# testOne@gmail.com
# ------WebKitFormBoundaryYrMFkLgguOYlHqSk
# Content-Disposition: form-data; name="password"

# Qwerty@123
# ------WebKitFormBoundaryYrMFkLgguOYlHqSk--

# post_access_token_url = f'{BASE_URL}/api/v1/login/access-token'
# get_refresh_token_url = f'{BASE_URL}/api/v1/login/refresh-token/?refresh_token={access_token}'


# [ GET ]
# get_non_medical_qual_url=f'{BASE_URL}/api/v1/non_medical_qualification/?customer_id={customer_uid}'
# get_non_medical_qual_score_url=f'{BASE_URL}/api/v1/non_medical_qualification/CEFR%20-%20Common%20European%20Framework%20of%20Reference%20for%20Languages?customer_id={customer_uid}'


# [ POST ]
# quick_reg_url =f'{BASE_URL}/api/v1/customer/{customer_uid}/candidate/'

# detail_reg_url = f'{BASE_URL}/api/v1/customer/{customer_uid}/candidate/'

# qual_url =f'{BASE_URL}/api/v1/customer/{customer_uid}/candidate/{candidate_uid}/qualification/'

# special_interest_url=f'{BASE_URL}/api/v1/customer/{customer_uid}/candidate/{candidate_uid}/speciality/'




# quick_reg [ DEMO1 ]

f = open('/home/kalingaraj/github/PythonExercises/generate_data/generate_data/data.json',)
data = json.load(f)
FILE_NAME = 'candidate.json'
PATH = f"/mnt/c/Users/kalingaraj/Desktop/{FILE_NAME}"

# 1 -> Phy
# 2 -> Nurse/Midwife
# 3 -> Allied Health Professional
# 4 -> Dentist
# 6 -> Non-Clinical/Administration

TOTAL = 11
CANDIDATES_GOT=0

CANDIDATE_TYPES = [1,2,3,4,6]
CANDIDATE_TYPE_NAMES = ['PHYSICIAN','NURSE','AHP','DENTIST','NON-CLINICAL']
DOMAINS = ['demo1','uemae', 'uemhp', 'uemmf', 'uemdt', 'hmgsa', 'hmgad', 'hmgoh']
SUB_DOMIANS = [ ".com", ".in", ".hf", ".hc", ".dr", ".care"]

# Agency
# 8645 ->  82
# 8646 ->  83
# 8647 ->  84
CREATED_BY = 8645
CONTACT_ID = None
CUSTOMER_UID = 13
# ORGANISATION_ID = --------------------------------  xxxxxxxxxxxxxxxx ----------------------------------

def get_gender_id():
    return 1 if CANDIDATES_GOT <= TOTAL/2 else 2

def get_dob():
    start_date = date(1970, 1, 1)
    end_date = date(2010, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

# 1-mr [3-miss, 4-ms] < 30 | 1-mr 2-mrs,ms < 45| 5,6 >45    

def get_title_id(gender_id, dob):
    # print(dob)
    today=datetime.now().date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    ms_miss_ids = [3,4]
    ms_mrs_ids = [3,2]
    dr_prof_ids = [5,6]
    if age > 45:
        return  dr_prof_ids[random.randint( 0, len(dr_prof_ids)-1)]
    elif gender_id == 1:
        return 1
    elif gender_id == 2:
        if age < 30:
            return  ms_miss_ids[random.randint( 0, len(ms_miss_ids)-1)]
        elif age < 45:
            return  ms_mrs_ids[random.randint( 0, len(ms_mrs_ids)-1)]
        


def get_first_name(gender_id):
    return names.get_first_name(gender='male' if gender_id == 1 else 'female').replace(" ","").lower()

def get_last_name():
    return names.get_last_name().replace(" ","").lower()

def get_full_name(gender_id):
    return get_first_name(gender_id)+get_last_name()

def get_customer_org_ids(acronym):
    if acronym == 'demo1':
        return (8,7)
    elif acronym == 'uemae':
        return (9,73)
    elif acronym == 'uemhp':
        return (9,74)
    elif acronym == 'uemmf':
        return (9,75)
    elif acronym == 'uemdt':
        return (9,78)
    elif acronym == 'hmgsa':
        return (12,76)
    elif acronym == 'hmgad':
        return (12,79)
    elif acronym == 'hmgoh':
        return (12,77)
    else:
        return None
    

# def get_email(candidate_type_id_,domain):
#     suffix = f'-type{candidate_type_id_}@'+domain
#     return get_full_name(1)+suffix

def logger(response):
    if response.status_code != 200:
        print(response.__dict__)
        return "failed"
    else:
        print('done!')
        return "done"

@asyncio.coroutine
def quick_registration(
    session,
    customer_uid,
    organisation_id,
    candidate_type_id,
    acronym,
    contact_id,
    created_by
    ):

    dob = get_dob()

    data_ = data['candidate']['quick_reg']
    data_['customer_id']=customer_uid
    data_['organisation_id']=organisation_id
    # data_['location_id']=customer_uid
    data_['gender_id'] = get_gender_id()
    data_['first_name']=get_first_name(data_['gender_id'])
    data_['surname']=get_last_name()
    data_['email'] = data_['first_name'].replace(" ","").lower()+data_['surname'].replace(" ","").lower()+f'-type{candidate_type_id}@'+acronym+SUB_DOMIANS[random.randint( 0, len(SUB_DOMIANS)-1)]
    data_['dob']=str(dob)
    data_['title_id']=get_title_id(data_['gender_id'],dob)
    data['alternate_email'] = data_['email']
    data_['candidate_type_id'] = candidate_type_id
    data_['contact_id'] = contact_id
    data_['created_by'] = created_by
    response = session.post(f'{BASE_URL}/api/v1/customer/{customer_uid}/candidate/', json=data_)
    logger(response)
    email =  data_['email']
    print(f'done for: {email}')


async def get_distinct_country():
    url= f'{BASE_URL}/api/v1/location/country_info/distinct_country'
    distinct_country=requests.get(url)
    logger(distinct_country)
    return [item['country_id'] for item in distinct_country]


async def get_qual_ids_based_on_country_id_or_candidate_type_id(country_id_,candidate_type_id_):
    get_qual_for_country_url=f'{BASE_URL}/api/v1/qualification/filtered/?country_id={country_id_}&candidate_type_id={candidate_type_id_}'
    get_qual_for_country = await requests.get(get_qual_for_country_url)
    logger(get_qual_for_country)
    return [item['qualification_id'] for item in get_qual_for_country.json()]


loop = asyncio.get_event_loop()
async def create_quick_candidates():
    quick_candidate_no = 0
    acronym = 'ohr'
    # for acronym in DOMAINS:
    for type_id in CANDIDATE_TYPES:
        tasks=list()
        # print(f'start populating {CANDIDATE_TYPE_NAMES[CANDIDATE_TYPES.index(type_id)]} for {acronym}')
        print('\n')
        for no in range(1,TOTAL):
            quick_candidate_no = quick_candidate_no+1
            print(f'{CANDIDATE_TYPE_NAMES[CANDIDATE_TYPES.index(type_id)]} @ [ {acronym} ]: candidate_no:{quick_candidate_no} with type:{type_id} for {acronym}')
            # customer_uid,organisation_id=get_customer_org_ids(acronym)
            customer_uid = CUSTOMER_UID
            if customer_uid == None or organisation_id == None:
                print(f'customer/organisation lookup failed for {acronym};\ndetail \n[\ncustomer_id: {customer_uid},\n org_id: {organisation_id}\n]\n ')
                break
            with requests.Session() as session:
                try:
                    tasks.append(asyncio.create_task(quick_registration(
                        session=session,
                        customer_uid=customer_uid,
                        organisation_id=organisation_id,
                        candidate_type_id=type_id,
                        acronym=acronym,    
                        contact_id=CONTACT_ID,
                        created_by=CREATED_BY
                    )))
                except Exception as err:
                    print(f"Exception occured: {err}")
                    break
        await asyncio.wait(tasks)
        print(f'\n\t\t\t\t\t\t\t\t\tfinished populating {CANDIDATE_TYPE_NAMES[CANDIDATE_TYPES.index(type_id)]} for {acronym}\n')
    print(f'\n\n\t\t\t{"="*50}\n\n\t\t\tcandidate populating process done for {acronym}\n\n\t\t\t{"="*50}')


loop.run_until_complete(create_quick_candidates())
loop.close()