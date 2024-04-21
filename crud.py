import mysql.connector
import streamlit as st

#Establish a connection to mysql server

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)


mycursor=mydb.cursor()
print("Connection Established")

#Create Web Streamlit App
def main():
    st.title("Crud Operation with mysql")

    #Display Action option for crud operation
    option=st.sidebar.selectbox("Select an Operation",("Create","Read","Update","Delete"))

    #Perform Selected Crud Operation
    if option=="Create":
        st.subheader("Create a record")
        name = st.text_input("Create a Name")
        email = st.text_input("Create a Email")
        if st.button("Create"):
            sql="insert into users(name,email) values (%s,%s)"
            val=(name,email)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Created Successfully")
    elif option=="Read":
        st.subheader("Read a Record")
        mycursor.execute("select * from users")
        result=mycursor.fetchall()
        for row in result:
            st.write(row)
    elif option=="Update":
        st.subheader("Update a Record")
        id=st.number_input("Enter ID",min_value=1)
        name=st.text_input("Input New Name")
        email=st.text_input("Input New Email")
        if st.button("Update"):
            sql="update users set name=%s ,email=%s where id=%s"
            val=(name,email,id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Data Updated Successfully")
    elif option == "Delete":
        st.subheader("Delete a Record")
        id=st.number_input("Input Id",min_value=1)
        if st.button("Delete"):
            sql="delete from users where id=%s"
            val=(id,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Data Deleted Successfully")


if __name__ == "__main__":
    main()