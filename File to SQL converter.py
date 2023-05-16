#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd


# In[74]:


df=pd.read_excel(r'C:\Users\User\OneDrive\Desktop\practice files\remote_df.xlsx')


# In[75]:


df.head()


# In[76]:


df.columns


# In[77]:


tablename='Kegan'


# In[78]:


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


# In[79]:


print(create_statement)


# In[80]:


df.head(2)


# In[81]:


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


# In[82]:


ists= insert_statement(df,'Isaac')
print(list(ists))


# In[83]:


def sql_generator(table, tablename):
    crt = create_statement(table, tablename)
    ins = insert_statement(table, tablename)
    final_statement = f"{crt} {' '.join(list(ins))}"
    return final_statement


# In[84]:


dff=pd.read_csv(r'C:\Users\User\OneDrive\Desktop\practice files\violations.csv')


# In[85]:


sql_sts = sql_generator(dff, "violation")


# In[86]:


with open('Lorna.txt','w')as file:
    file.write(sql_sts)


# In[ ]:




