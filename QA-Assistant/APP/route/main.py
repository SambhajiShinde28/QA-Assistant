from flask import Blueprint,request
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel,Field
from dotenv import dotenv_values
import sqlite3 as sq
import pandas as pd
import os

doc_bp=Blueprint('/sql',__name__)

class struct_output(BaseModel):
    query:str=Field(description="This key only contain the sql query here do not use any special symbols like backward and forward sslash if it not neccessary in the query. The query must be in sigle line")
    descri:str=Field(description="This is the detailed explaination about the query in 2 to 3 lines.")

def SQLDatabase():

    if not os.path.exists("QA_Database/qa_database.db"):
        qa_df=pd.read_csv("CSV_Files/sample_bo_tbl_large.csv")
        rev_df=pd.read_csv("CSV_Files/sample_revenue_large.csv")
        sub_df=pd.read_csv("CSV_Files/sample_sub_details_large.csv")

        con=sq.connect("QA_Database/qa_database.db")
        curs=con.cursor()

        dut_table="""
            create table bo_table(
                country varchar(200),
                date varchar(200),
                total_mins int,
                internation_mins int,
                sms int,
                total_data_usage int,
                payg_amount float
            )
        """

        r_table = """
            CREATE TABLE rev_table (
                country VARCHAR(200),
                channel VARCHAR(200),
                date VARCHAR(200),
                revenue FLOAT,
                net_revenue FLOAT
            )
        """

        sub_table="""
            CREATE TABLE subdetails_table (
                country VARCHAR(200),
                channel VARCHAR(200),
                date VARCHAR(200),
                subs int,
                netadds int,
                churn int
            )
        """

        curs.execute(dut_table)
        curs.execute(r_table)
        curs.execute(sub_table)

        for i in range(len(qa_df)):
            cou=qa_df["country"][i]
            date=qa_df["date"][i]
            tm=qa_df["total_mins"][i]
            im=qa_df["international_mins"][i]
            sms=qa_df["sms"][i]
            tdu=qa_df["total_data_usage"][i]
            pa=qa_df["payg_amount"][i]

            query=f"Insert Into bo_table values('{cou}','{date}',{tm},{im},{sms},{tdu},{pa})"

            curs.execute(query)

        for i in range(len(rev_df)):
            cou_r=rev_df["country"][i]
            chan=rev_df["channel"][i]
            dt=rev_df["date"][i]
            r=rev_df["revenue"][i]
            nr=rev_df["net_revenue"][i]
        
            query=f"Insert Into rev_table values('{cou_r}','{chan}','{dt}',{r},{nr})"

            curs.execute(query)

        for i in range(len(sub_df)):
            co=sub_df["country"][i]
            ch=sub_df["channel"][i]
            d=sub_df["date"][i]
            sub=sub_df["subs"][i]
            na=sub_df["netadds"][i]
            ch=sub_df["churn"][i]
        
            query=f"Insert Into subdetails_table values('{co}','{ch}','{d}',{sub},{na},{ch})"

            curs.execute(query)

        data=curs.execute('''Select * from subdetails_table''')
        for row in data:
            print(row)

        con.commit()
        con.close()
        return {"data" : "ok"}

SQLDatabase()

def read_sql_query(sql, db):
    try:
        conn = sq.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        col_names = [desc[0] for desc in cur.description] 
        conn.close()
        return rows, col_names
    except sq.Error as e:
        return [("SQL Error", str(e))], ["Error"]


@doc_bp.route('/fetch',methods=["POST"])
def Fetching_Data():
    api_key=dotenv_values()["GEMINI_API_KEY"]
    question=request.form['que']
    
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        api_key=api_key
    )

    parser=llm.with_structured_output(struct_output)
    res=parser.invoke(question)
    sql_res=read_sql_query(res.query,"QA_Database/qa_database.db")

    return {"description" : f"{res.descri}","Query" : f"{res.query}","output":sql_res}

   
