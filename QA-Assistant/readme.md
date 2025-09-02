1) To run this file on user system he have to first install all packages in requirements.txt file

2) User must user gmini llm api key

3) use must give clear prompt as the input to the model 
    like : give me country DDD all data from rev_table 

4) The output that user get is the dictionsry form and structure of dictionary is as following.
    {
        "Query" : "Here is the sql query returned by model"
        "description" : "Here is the description of the the query returned by the model"
        "output" : "Here is the fetched data from the table. It is of list type where first list is the table data and second list is the column list" 
    }