from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Liste von Wörtern
words = ["Lionel Messi", "Cristiano Ronaldo", "Kylian Mbappe", "Jude Bellingham", "Pedri", "Gavi", "David Beckham", "Raul", "Lamine Yamal","Arturo Vidal","Florian Wirtz", "Gökhan Töre","Victor Boniface","Amine Adli","Patrik Schick", "Adam Hlozek", "Borja Iglesias", "Granit Xhaka", "Exequiel Palacios", "Jeremie Frimpong", "Jonas Hofmann","Robert Andrich","Alejandro Grimaldo","Edmond Tapsoba", "Josip Stanisic","Piero Hincapie", "Jonathan Tah","Lukas Hradecky","Harry Kane","Eric Maxim Choupo-Moting", "Mathys Tel","Jamal Starboy Musiala","Leroy Sane","Thomas Müller", "Joshua Kimmich","Serge Gnabry","Kingsley Coman","Leon Goretzka", "Konrad Laimer","Aleksander Pavlovic","Alphonso Davies","Matthijs de Ligt", "Noussair Mazraoui", "Kim Min Jae", "Dayot Upamecano","Sacha Boey","Raphael Guerreiro","Eric Dier", "Bouna Sarr","Manuel Neuer", "Sven Ulreich","Sehrou Guirassy","Silas Katompa Mvumpa","Deniz Undav","Jamie Leweling", "Mahmoud Dahoud", "Chris Führich","Enzo Millot", "Angelo Stiller", "Atakan Karazor","Josha Vagnoman","Hiroki Ito","Dan-Axel Zagadou","Maxi Mittelstädt", "Waldemar Anton", "Alexander Nübel", "Sebastien Haller","Youssoufa Moukoko","karim Adeyemi", "Donyell Malen","Niclas Füllkrug"]
click_count = None
impostor_index = None
non_impostor_word = None  # Zufälliges Wort als globale Variable definieren
num_players = None

@app.route('/' , methods = ['GET', 'POST'] )
def index():
    global num_players
    global impostor_index
    global non_impostor_word
    global click_count

    if request.method == 'POST':
        num_players = int(request.form['num_players'])
        impostor_index = random.randint(0, num_players - 1)  # Neuen Impostor-Index generieren
        non_impostor_word = random.choice(words)  # Neues zufälliges Wort auswählen
        click_count = 0
        return redirect(url_for('game'))
    return render_template('index.html', impostor_index=impostor_index, non_impostor_word=non_impostor_word)


@app.route('/game', methods=['POST', 'GET'])
def game():
    global click_count
    global impostor_index
    global non_impostor_word

    current_player = int(request.form.get('current_player', 0))
    if request.method == 'POST':
        click_count +=1
        if click_count <= num_players:
            if current_player == impostor_index:
                word = "Impostor du Ayri hahah viel Glück.\n PS: Inflation steigt"  # Impostor sieht "X"
            else:
                word = non_impostor_word  # Alle normalen Spieler sehen das gleiche zufällige Wort
            current_player = (current_player + 1)
        else:
            click_count = 0
            return redirect(url_for('index'))  # Zurück zum Startmenü nach dem dritten Klick
    else:
        word = "auf der nächsten Seite"
        current_player = 0
    return render_template('game.html', word=word, current_player=current_player, num_players=num_players, impostor_index=impostor_index, non_impostor_word=non_impostor_word)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
