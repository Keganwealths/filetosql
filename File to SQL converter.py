import pandas as pd
df=pd.read_excel(r'C:\Users\User\OneDrive\Desktop\practice files\remote_df.xlsx')
#GLOBAL VARIABLE
tablename='Kegan'
#CREATE STATEMENT FUNCTION
def create_statement(table,tablename):
    create_statement=f'CREATE TABLE {tablename}('
    for column in table.columns:
        column_name=column.replace(' ','_')
        column_type=table[column].dtype
        if column_type in ['int','int8','int32','int64']:
            column_type='INT'
        elif column_type in ['float','float8','float32','float64']:
            column_type='NUMERIC(9,2)'
        elif column_type=='object':
            column_type='VARCHAR(255)'
        elif column_type=='datetime64':
            column_type='TIMESTAMP'
        else:
            column_type='VARCHAR(255)'
        create_statement+=f'\n\t{column_name} {column_type}'
    create_statement +='\n);'
    return create_statement
#INSERT VALUES FRNCTION
def insert_statement(table,tablename):
    for index, row in table.iterrows():
        values=[]
        for value in row:
            if pd.isna(value):
                value='NULL'
            else:
                value=f'"{value}"'
            values.append(value)
            col_name=', '.join(table.columns)
            change_value =", ".join(values)
        ins_statement=f'INSERT INTO {tablename}({col_name}) VALUES ({change_value}),'
        yield ins_statement
ists= insert_statement(df,'Isaac')
#print(list(ists))
#COMBINE FUNCTIONS
def sql_generator(table, tablename):
    crt = create_statement(table, tablename)
    ins = insert_statement(table, tablename)
    final_statement = f"{crt} {' '.join(list(ins))}"
    return final_statement

dff=pd.read_csv(r'C:\Users\User\OneDrive\Desktop\practice files\violations.csv')
sql_sts = sql_generator(dff, "violation")
with open('Lorna.txt','w')as file:
    file.write(sql_sts)





