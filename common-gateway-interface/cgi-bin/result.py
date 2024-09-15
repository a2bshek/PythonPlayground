import cgi
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

formDetails = cgi.FieldStorage()
rollno=formDetails["roll"].value

db = client["cgicourse"]
mycollection = db["results"]

one = mycollection.find_one({"rollno": rollno})
sub = one["course"]

print('''Content-Type: text/html\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>%s-Results</title>
    <style>
        body
        {
            font-size:20px;
        }
        .header
        {
            align-items:"center";
            padding-left: 250px;
        }
        .img
        {
            width:1000px;
            height:100px;
            border-radius: 5px;
            border-width: 10px;
            border-style: double;
            border-color: red;
        }
        .result
        {
            border-radius: 5px;
            border-width: 10px;
            border-style: double;
            border-color: red;
            align-items: center;
            text-align: center;
        }
        .left
        {
            text-align: left;
        }
        .mid
        {
            text-align: center;
        }
        .center 
        {
            margin-left: auto;
            margin-right: auto;
        }
        table, th, td
        {
            border: 1px solid black;
            padding:10px;
        }
        .strong
        {
            font-weight:bold;
        }
    </style>
</head>
<body>
    <div class="header">
        <img src="../Images/srec.png" class="img">
    </div>
    <br>
    <div class="result">
        <br>
        <label class="mid strong">%s</label>
        <br>
        <label class="mid strong">%s</label>
        <br>
        <label class="mid strong">%s</label>
        <br><br>
        <table class="center tableborder">
            <thead>
                <tr>
                    <th>Subject Code</th>
                    <th>Subject Title</th>
                    <th>Grade</th>
                    <th>Result</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>21PY001</td>
                    <td>Python</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
                <tr>
                    <td>21PY011</td>
                    <td>Python Laboratory</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
                <tr>
                    <td>21MSF02</td>
                    <td>Metasploit Framework</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
                <tr>
                    <td>21MSF22</td>
                    <td>Metasploit Framework Laboratory</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
                <tr>
                    <td>21NM003</td>
                    <td>NMAP</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
                <tr>
                    <td>21NM033</td>
                    <td>NMAP Laboratory</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
            </tbody>
        </table>
        <br>
    </div>
</body>
</html>

'''%( one["rollno"],one["rollno"],one["name"],one["dep"],sub[0]["py"],sub[0]["grade"],sub[1]["pylab"],sub[1]["grade"],
     sub[2]["msf"],sub[2]["grade"],sub[3]["msflab"],sub[3]["grade"],sub[4]["nmap"],sub[4]["grade"],sub[5]["nmaplab"],sub[5]["grade"]))