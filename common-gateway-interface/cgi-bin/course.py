import cgi
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

formDetails = cgi.FieldStorage()
Roll=formDetails["roll_num"].value
First=formDetails["first_name"].value
Last=formDetails["last_name"].value
Gender=formDetails["gender"].value
Dob=formDetails["dob"].value
Email=formDetails["email"].value
Course=formDetails["course"].value

db = client["cgicourse"]
mycollection = db["registration"]

one=mycollection.insert_one({"roll":Roll,"first_name":First,"last_name":Last,"gender":Gender,"dob":Dob,"email":Email,"course":Course})

print("""Content-Type: text/html\n

<!DOCTYPE html>
<html>
    <head>
        <title>    
            Student Registration
        </title>
        <link rel="icon" type="image/png" href="../Images/Logosrec.jpg">
        <style>
            body 
            {
                background-color: #000;
                color:#FFF;
                font-family: Arial, Helvetica, sans-serif;
            }
            h1
            {
                text-align: center;
            }
            hr
            {
                border: 4px solid #FFF;
            }
            button 
            {
                background-color: #2230afbb;
                color: white;
                padding: 10px 15px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <hr>
        <img src="../Images/Logosrec.jpg" align="left" height="80" width="100">
        <img src="../Images/download.png" align="right" height="80" width="100">
        <h1>
            <font color="#99ff99">Government of SREC - </font>
            <font color="#0000ff">SREC Engineering Admission 2021</font>
        </h1>
        <hr>    
        <center>
            <table width="500px">
                <tr>
                    <td align="center"><h1><font color="#ff0000">Student Registration</font></h1></td>
                </tr>
            </table>
            <table width="400px" cellspacing="10px" cellpadding="10px">
                <form>
                    <tr>
                        <td>
                            Roll Number:
                        </td>
                        <td>
                            <label>%s</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Name:
                        </td>
                        <td>
                            <label>%s</label> <label>%s</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Gender:
                        </td>
                        <td>
                            <label>%s</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            DOB:
                        </td>
                        <td>
                            <label>%s</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Email:
                        </td>
                        <td>
                            <label>%s</label>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Course Selected:
                        </td>
                        <td>
                            <label>%s</label>
                        </td>
                    </tr>
                </form>
            </table>
        </center>
    </body>
</html>
"""%(Roll,First,Last,Gender,Dob,Email,Course))
