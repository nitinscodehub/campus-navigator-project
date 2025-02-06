from flask import Flask, render_template, request, redirect, url_for # type: ignore

app = Flask(__name__)

#Assumed facilities names on campus
facilities = [
    {"name": "Sam Jonah Library", "info": "Main library, Sam Jonah Library. Northern Campus opposite the Shuttle bus station; PMB, University of Cape Coast ; 302 21 30952/3 ; library@ucc.edu.gh ; CC-167-5810 ... UCC Journals; Research Guides; Library Policies; Support the Libraries; Library Spaces; Borrowing Materials; Library Services; Library hour. Semester "},
    {"name": "UCC main Hospital", "info": "The University of Cape Coast Hospital is located on the campus of the University of Cape Coast. The hospital provides services to both the university and the communities surrounding the university. The hospital has several sections: the outpatient clinic department (OPD), the medical laboratory, the male and female wards, and the children's ward."},
    {"name": "Science Market", "info": "Market students"},
    {"name": "Institute of Education", "info": "Institute of Education, University of Cape Coast. New Site, Opposite CALC Building Complex ; ioe@ucc.edu.gh Outreach Sandwich Support Lines: 0303956523; 0535560996; 0535410424; 0246337487 (Whatsapp only)"},
    {"name": "Auditorium 900", "info": "site"},
    {"name": "Sandwich Lecture Theater (SWL)", "info": "Near Science market"},
    {"name": "Kwame Nkrumah Hall", "info": "New site, 15 Minute of Campus"},
    {"name": "SRC Hall", "info": "Near Cape Coast Sport Stadium"},
    {"name": "Valco Hall", "info": "Located at new site, 15 of campus"},
    {"name": "New Lecture Theater(NLT)", "info": "Located 10 minute of Sam Jonah Library"},
    
    
]



#This this route for home the page of the application
@app.route('/')
def home():
    return render_template('home.html', facilities=facilities)


#This is the route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Dummy authentication
        if username == "admin" and password == "password":
            return redirect(url_for('home'))
    return render_template('login.html')



@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Dummy authentication
        if username == "admin" and password == "password":
            return redirect(url_for('home'))
    return render_template('profile.html')



#This is the route for facility on campus
@app.route('/facility/<name>')
def facility(name):
    facility_info = next((f for f in facilities if f["name"] == name), None)
    return render_template('facility.html', facility=facility_info)

if __name__ == '__main__':
    app.run(debug=True)
