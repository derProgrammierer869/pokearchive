from crypt import methods
from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__, static_url_path='')

app.config['SECRET_KEY'] = '0x10200e3b0'
#main tabs
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/cards')
def cards():
    return render_template('cards.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')    



#drop down tabs
@app.route('/japancards')
def japancards():
    return render_template('japancards.html')

@app.route('/gameevents')
def gameevents():
    return render_template('gameevents.html')

@app.route('/expansionsets')
def expansionsets():
    return render_template('expansionsets.html')

@app.route('/specialcards')
def specialcards():
    return render_template('specialcards.html')

@app.route('/exlist')
def exlist():
    return render_template('exlist.html')

@app.route('/goldstar')
def goldstar():
    return render_template('goldstar.html')

@app.route('/deltaspecies')
def deltaspecies():
    return render_template('deltaspecies.html')



#expansion card list tabs
@app.route('/rubysapphire')
def rubysapphire():
    return render_template('RubySapphire.html')

@app.route('/sandstorm')
def sandstorm():
    return render_template('Sandstorm.html')

@app.route('/dragon')
def dragon():
    return render_template('Dragon.html')

@app.route('/magmaaqua')
def magmaaqua():
    return render_template('MagmaAqua.html')    

@app.route('/hiddenlegends')
def hiddenlegends():
    return render_template('HiddenLegends.html')

@app.route('/frlg')
def frlg():
    return render_template('FRLG.html')

@app.route('/rocketreturns')
def rocketreturns():
    return render_template('RocketReturns.html')

@app.route('/deoxys')
def deoxys():
    return render_template('/Deoxys.html')

@app.route('/emerald')
def emerald():
    return render_template('Emerald.html')

@app.route('/unseenforces')
def unseenforces():
    return render_template('UnseenForces.html')

@app.route('/exdeltaspecies')
def exdeltaspecies():
    return render_template('EXDeltaSpecies.html')

@app.route('/legendmaker')
def legendmaker():
    return render_template('LegendMaker.html')

@app.route('/holonphantoms')
def holonphantoms():
    return render_template('HolonPhantoms.html')

@app.route('/crystalguardians')
def crystalguardians():
    return render_template('CrystalGuardians.html')

@app.route('/dragonfrontiers')
def dragonfrontiers():
    return render_template('DragonFrontiers.html')

@app.route('/powerkeepers')
def powerkeepers():
    return render_template('PowerKeepers.html')



#games tabs
@app.route('/battleEcards')
def battleEcards():
    return render_template('battleEcards.html')

@app.route('/RSE')
def RSE():
    return render_template('RSE.html')

@app.route('/FRLGgames')
def FRLGgames():
    return render_template('FRLGgames.html')

if __name__ == '__main__':
    app.run(debug=True)

'''
To run the server:
1. Have the Flask Project folder open in terminal
2. export FLASK_APP=flasktest.py
3. run flask
4. For debug mode:
    -export FLASK_DEBUG=1
    -run flask

or just run project in IDE
'''
#flash message doesnt work.

#everything within the block content will be imported from or to the layouts page. it works almost like importing from another file.