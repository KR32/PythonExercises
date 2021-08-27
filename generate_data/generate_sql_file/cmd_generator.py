# https://stackoverflow.com/questions/32234863/create-sql-insert-script-with-python 

FILE_NAME = 'insert_data.sql'
PATH = f"/mnt/c/Users/kalingaraj/Desktop/{FILE_NAME}"

# details = {
#     'table_name' : 'users',
#     'columns'    :"""
#         customer_id,
#         email,
#         hashed_password,
#         is_active,
#         user_name,
#         created_at,
#         first_name,
#         surname,
#         dob,
#         alternate_phone,
#         known_as,
#         contact_phone,
#         set_passwd_on_login,
#         suspended,
#         date_suspended,
#         comments,
#         created_on,
#         created_by,
#         last_modified_on,
#         last_modified_by,
#         first_login_date,
#         last_login_date,
#         deleted,
#         deleted_by,
#         deleted_on
#         """,
#     "values":[
#         [8,
#         'johnsmith@gmail.com',
#         '$2b$12$BAqyyZhtCWVuiIrFpyGrZOIi7MdjZYuftXtKJeOj6RFDJPiuZjH/.',
#         "true",
#         'johnsmith@gmail.com',
#         '2021-03-17 11:54:13.402053',
#         'John',
#         'Smith',
#         '1975-06-28',
#         '',
#         "NULL",
#         '+44^1234244',
#         "false",
#         "false",
#         "NULL",
#         "NULL",
#         '2021-03-17 11:54:13.402053',
#         0,
#         '2021-05-31 06:45:43.462341',
#         8454,
#         '2021-03-17 11:54:56.765578',
#         '2021-06-11 09:43:13.24611',
#         "NULL",
#         "NULL",
#         "NULL"]
#     ]
# }

def create_sql_script_file(data_condtions:dict,path:str=PATH):
    myfile = open(path, 'w')
    parsed_colums = None
    if data_condtions["columns"] and data_condtions["columns"].find('\n') > -1:
        parsed_colums = [column for column in data_condtions["columns"].replace('\n',"").replace(" ","").split(',') if column != ""]
        parsed_values = [str(val).replace('\n',"").replace(" ","") for val in data_condtions['values']]
        print(parsed_colums)
        print(parsed_values)
        if not len(parsed_colums) == len(parsed_values):
            raise ValueError(
                "Column count and Value count are not matched !!"
            )
    else:
        raise SyntaxError(
            "Invalid columns input Syntax; columns should be multiline string!"
        )
    myfile.write(f'INSERT INTO {data_condtions["table_name"]} ({",".join(parsed_colums)})\nVALUES\t')
    myfile.write(f'({",".join(parsed_values)})')
    #set counter variable
    # X X X  do something....
    #  if values is first 
    myfile.write(';')
    myfile.close()

# create_sql_script_file(PATH, details)