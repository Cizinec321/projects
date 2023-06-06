def gen_text(in_val):
    return {
        'about': (
            '<p style="font-size:15px; position: relative;margin-right: 2em;margin-left: 2em; margin-top: 10em; margin-bottom: 0em; text-align: left;"><b>About Me</b><br><br>'


                "I am a Development Engineer with a wide range of interests and skills currently living in Cluj - Romania .<br><br>"

                "Nowadays I am mostly interested in any technology related to database development and maintanance (with SQL and Python) and software development "
                " but I am also widening my skill range in web development.<br><br>"

                "In the past, I have worked on various small personal projects (mostly in C# but I have explored the entire .net ecosystem) which later evolved into automating server-side ETL processes in various scripting languages (Python, VB, powershell). "
                "Now allot of my work revolves around developing server-side ETL processes.</p>"
                
                ),
        'edu': (

                '<p style="font-size:15px; position: relative;margin-right: 2em;margin-left: 2em; margin-top: 10em; margin-bottom: 0em; text-align: left;"><b>Education</b><br><br><br>'


                "<b>BABES BOLYAI UNIVERSITY, CLUJ-NAPOCA ( RO )</b><br><br>"
                "October 2014 to July 2016<br>"
                "Masters Degree within the Clinical Psychology Department<br>"
                "Faculty of Psychology and Education Sciences<br>"
                "Title of Master's program: Psychological techniques for behavior control and development of human potential<br><br><br>"

                "<b>BABES BOLYAI UNIVERSITY, CLUJ-NAPOCA ( RO )</b><br><br>"
                "October 2011 to July 2014<br>"
                "Bachelor degree in Psychology within the Psychology Department<br>"
                "Faculty of Psychology and Education Sciences<br></p>"

        ),





        'xp':(
            '<p style="font-size:15px; position: relative;margin-right: 2em;margin-left: 2em; margin-top: 10em; margin-bottom: 0em; text-align: left;"><b>Experience</b><br><br><br>'
            "<b>Development Engineer @ ING Tech</b><br>"
            "December 2021 to present<br>"
            "ETL process development<br>"
            "Data administration with SQL<br><br><br>"

            "<b>IT Data Analytics Developer @ Emerson Commercial & Residential Solutions</b><br>"
            "January 2020 to December 2021<br>"
            "Heavily involved in the development and launch of three Hyperion Cloud PBCS environments with multiple complex applications in each environment.<br>"
            "Heavily involved in data migration from old OnPremise solution to the cloud application and responsible with maintaing data integrity during migration.<br>"
            "Responsible with debuging, reviewing, building and maintaining complex ETL processes that transfer and transform data used in MS SQL databases, SnowFlake and Hyperion PBCS.</b><br>"
            "Involved in data maintanance automatization and process improvement with Microsoft Azure,Python and BluePrism.<br><br><br>"

            "<b>Business Analyst @ Bombardier Transportation</b><br>"
            "September 2015 to August 2016 / September 2017 to January 2020<br>"
            "Headcount data integrity and consisstency evaluation and maintanance, data reporting and visualization.<br><br><br>"


            "<b>HR/Payroll Admin @ Bombardier Transportation</b><br>"
            "July 2012 to August 2015<br>"
            "Headcount & Payroll reporting,Data maintanance & validation. <br>"



        ),



        'contact':(
            '<p style="font-size:30px; position: relative;margin-right: 2em;margin-left: 2em; margin-top: 10em; margin-bottom: 0em; text-align: left;"><b>Contact</b><br><br><br>'

            "<b>Email:</b> velich.eduard@gmail.com<br>"

            "<b>LinkedIn:</b> <a href='https://www.linkedin.com/in/eduard-matei-velich-0ba0ba19a/'> Here</a>"

        ),
        '':('')
    }[in_val]