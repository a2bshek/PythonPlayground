import cgi
import cgitb
form = cgi.FieldStorage()
first = form.getvalue('first_name')
last = form.getvalue('last_name')
print('Content-type:text/html\r\n\r\n')
print(f'''
    <html>
        <head>
            <title>
                Welcome {first} {last}
            </title>
        </head>
        <body style="background-color: #000;">
            <div style="padding-top:200px; padding-left: 650px; color: #00A300; font-size: 55px; font-weight: bold;">
                    Welcome<br>{first} {last}
            </div>
            <br>
            <div style="padding-top:50px; padding-left: 350px; color: #F00; font-size: 25px;">
                The entire world is thrilled to welcome you. We hope you’ll do some amazing works here!
            </div>
        <body>
</html>
''')