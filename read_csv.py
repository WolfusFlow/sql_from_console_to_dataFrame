import os
import sys
import pandas as pd
import pandasql as ps

'''
QUERY EXAMPLES:
select * from csv_table;
select * from csv_table where Grade in ('B','C');
select last_name where first_name like 'M%';
'''

QUIT_COMMANDS = {'q', '\q', 'quit', '\quit'}
EXIT_TEXT = 'Program execution is finished'
FILE_EXTENTION = '.csv'
RETURN_TO_FILE_COOSING = {'back', 'return', 'choose new file'}

def check_file_exist(filename):    
    if not FILE_EXTENTION in filename:
        filename+=FILE_EXTENTION
    file_exist = True if os.path.exists(f'{filename}.csv') | os.path.exists(f'{filename}') else False
    return filename, file_exist


class Sql_Operations:
    
    def __init__(self):
        self.data = None

    def init_table_from_file(self, filename):
        try:
            self.data = pd.read_csv(filename, sep=',')
            print('Selected table from file: \n', self.data)
            if self.data.empty:
                print('This table have no data to work with! Try other file or quit')
                return True
            print('for operating with this table call it csv_table')
        except Exception as e:
            print('Exception: ', e)       


    def input_query(self, input_query):
        if input_query in QUIT_COMMANDS:
            print(EXIT_TEXT)
            sys.exit()
        if input_query in RETURN_TO_FILE_COOSING:
            return 'exit_quering'
        if input_query in [None, '', ' ', '\n']:
            return 'You inputed nothing. Try again or exit' 
        if input_query[-1] != ';':
            return 'Your query don\'t ending with ";" - fix it and try again'
        try:        
            csv_table = pd.DataFrame(self.data)
            type(ps.sqldf(input_query, locals()))
            return str(ps.sqldf(input_query, locals()))
        except Exception as e:
            print(f'Exception with SQL query: {e}')


if __name__ == "__main__":
    filename = None
    print("For exit use - 'q', '\q', 'quit', '\quit'")
    while True:
        filename = input('Enter your csv filename: ')
        if filename in QUIT_COMMANDS:
            print(EXIT_TEXT)
            sys.exit()

        filename, exist = check_file_exist(filename)

        if not exist:
            print(f'File_name: "{filename}" doesn\'t exist - try different filename or exit\n')
            continue

        empty_file = os.stat(filename).st_size == 0

        if empty_file:
            print(f'File_name: {filename} is complitly empty - try different filename or exit\n')
            continue

        if exist and not empty_file:
            print(f'File_name - "{filename}" exist and not empty - we may proceed\n')
            sql_operations = Sql_Operations()
            empty_values = sql_operations.init_table_from_file(filename)
            if empty_values:
                continue

            print('\nIf you want to return back to file choosing - type - "back" or "return"')

            while True:
                result = sql_operations.input_query(input('\nInput your query for table:\n'))
                if result == 'exit_quering':
                    break
                print(result)