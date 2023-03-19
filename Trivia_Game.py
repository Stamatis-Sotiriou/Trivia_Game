#Test 2#
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox)

from random import choice
from numpy import array_split

app = QApplication([])

# Αρχική συνάρτηση:

def start_func():
    user_answer(button1, button2, button3, button4)

# Συνάρτηση επιλογής ερώτησης:

def pick_question(btn_1, btn_2, btn_3, btn_4):

    global global_key
    global points
    
    try:        # Εκτέλεσε μόνο αν υπάρχουν διαθέσιμες ερωτήσεις:
        submission.setText("Υποβολή")
                    
        ButtonList = [btn_1,btn_2,btn_3,btn_4] # Φτιάφε λίστα με κουμπιά
                    
        key = choice(list(Questions_dict.keys()))   # Επίλεξε μία τυχέα ερώτηση

        question.setText(key)           # Δείξε την ερώτηση
                        
        value = Questions_dict[key]       # Βγάλε τις απαντήσεις (σε μορφή λίστας // Values)

        Questions_dict.pop(key)         # Αφαίρεσε την ερώτηση και τις απαντήσεις από το λεξικό
                    
        splits = array_split(value, 4)  # Σπάσε την λίστα με τις απαντήσεις

        for array in splits:            # Λουπα ώστε να δωθούν οι απαντήσεις στα κουμπιά
            for button in ButtonList:
                array = ', '.join(array)    # Αφαίρεσε στοιχεία όπως το ', '
                button.setText(array)       # Τοποθέτησε την ερώτηση στο κουμπί
                ButtonList.remove(button)   # Αφαίρεσε το κουμπί από την λίστα
                break       # Σπάσε (εδώ έκανα μια πατέντα ώστε να σπάσει ο βρόχος και να επιλεγχτεί η επόμενη ερώτηση)
                        
        global_key = key
        
    except:     # Αφού τελειώσουν οι διαθέσιμες ερωτήσεις
        group.hide()        # Κρύψε την ομάδα κουμπιών 
        submission.hide()   # Κρύψε το κουμπί υποβολής
        on_off.hide()       # Κρύψε το κουμπί on / off
        
        points = str(points)
        lenght = len(Answers_dict)

        if points == "1":
            ap = "Από τις %s ερωτήσεις μόνο μια απαντήθηκε σωστά" % lenght
        elif points == "0":
            ap = "Από τις %s ερωτήσεις καμία δεν απαντήθηκε σωστά"
        else:
            ap = "Από τις %s ερωτήσεις οι %s απαντήθηκαν σωστά" % (lenght, points)
        
        question.setText(ap)    # Πρόβαλε τον αριθμό τον σωστών απαντήσεων

# Συνάρτηση ελέγχου απάντησης:

def user_answer(btn_1, btn_2, btn_3, btn_4):

    global start_value
    global points

    if on_off.isChecked():      # Λειτουργία κουμπιού on / off
        off = True
    else:
        off = False
    
    if start_value != 0:        # Έλεγξε αν είναι ο πρώτος κύκλος επανάληψης
        ButtonList = [btn_1,btn_2,btn_3,btn_4]      # Φτιάφε λίστα με κουμπιά
        
        for button in ButtonList:       # Λούπα ώστε να ελενχθούν όλα τα κουμιά
            if button.isChecked():      # Αν το κουμπί έχει επιλεχθεί
                 ans = button.text()    # Κατοχείρωσε την απάντηση του χρήστη

        if Answers_dict[global_key] == ans:     # Έλεγξε αν η απάντηση είναι σωστή
            points = points + 1
            if not off:
                correct.show()
        else:
            if not off:
                wrong.show()

        pick_question(btn_1, btn_2, btn_3, btn_4)  # Τρέξε την συνάρτηση επιλογής ερώτησης
        
    else:
        points = 0
        pick_question(btn_1, btn_2, btn_3, btn_4)
        start_value = start_value + 1

# Αρχικοποίηση global μεταβλητών

global button1
global button2
global button3
global button4

global Questions_dict
global Answer_dict

start_value = 0

# Ερωτήσεις (με πολλαπλές απαντήσεις):

Questions_dict = {
            "Ποια χρονιά εκτοξεύτηκε ο πρώτος δορυφόρος;":["1967","1957","1950","1969"],
            "Σε ποιο νησί γεννήθηκε ο Ναπολέων Βοναπάρτης;":["Κορσική","Σαρδινία","Μαγιορκα","Κέρκυρα"],
            "Ποιος έγινε ηγέτης της Γερμανίας μετά το θάνατο του \nΑδόλφου Χίτλερ;":["Χέρμαν\nΓκέρινγκ","Χάινριχ\nΧίμλερ","Καρλ\nΝτένιτς","Κανένας"],
            "Πότε έγινε η 1η Ιανουαρίου η πρώτη μέρα του έτους;":["46 π.Χ","527 μ.Χ","372 μ.Χ.","127 π.Χ."],
            "Ποια χρονιά έλαβε χώρα η πρώτη ελεγχόμενη \nπυρηνική αλυσιδωτή αντίδραση;":["1947","1942","1939","1935"],
            "Ποιο είναι το χημικό σύμβολο του σιδήρου;":["Fe","C","Hg","F"],
            "Κατά μέσο όρο, πόσο καιρό ζει ένα ποντίκι \nστη φύση;":["3 μήνες","9 μήνες","6 μηνες","1 χρόνο"],
            "Ποιο είναι το πρώτο στοιχείο στον περιοδικό πίνακα;":["Οξυγόνο","Άνθρακας","Αλουμίνιο","Υδρογόνο"],
            "Ποιο έτος ανακαλύφθηκαν οι ακτίνες Χ;":["1872","1923","1895","1908"],
            "Πόσα γήινα χρόνια είναι ένα έτος στον Δία;":["14.5","11.9","9  ","4  "],
            "Πόσα φεγγάρια έχει ο Άρης;":["Κανένα","2","3","1"],
            "Πόσες καρδιές έχει ένα χταπόδι;":["1","3","8","5"],
            "Ποιο στοιχείο έχει το χημικό σύμβολο Au;":["Aσήμι","Χρυσός","Χαλκός","Άργυρος"],
            "Πόσα αστέρια είναι στη Μεγάλη Άρκτος;":["5","10","3","7"],
            "Πώς γράφετε το 99 με λατινικούς αριθμούς;":["XCIX","C","LVIII","XCVI"],
            "Ποια χρονιά έγινε ο Ναπολέων βασιλιάς της Ιταλίας;":["1805","1799","1810","Δεν έγινε\n   ποτέ"],
            "Σε ποιο νησί εξορίστηκε ο Ναπολέων το 1814;":["Αγία Ελένη","Έλβα","Αγία Λουκία","Κανένα από τα\n  παραπάνω"],
            "Ποιος από τους παρακάτω Doom cheat codes έχει το \nδικό του παιχνίδι το όνομά του;":["iddqd","idspispopd","idmypos","idkfa"],
            "Πώς ονομαζόταν ο πρώτος ηλεκτρονικός \nυπολογιστής;":["Harvard\n  Mark","SSEM","EDSAC","ENIAC"],
            "Πότε παρουσιάστηκε ο υπολογιστής Apple II;":["1974","1982","1977","1980"]
            }

# Ερωτήσεις (μόνο με την σωστή απάντηση):

Answers_dict = {
            "Ποια χρονιά εκτοξεύτηκε ο πρώτος δορυφόρος;":"1957",
            "Σε ποιο νησί γεννήθηκε ο Ναπολέων Βοναπάρτης;":"Κορσική",
            "Ποιος έγινε ηγέτης της Γερμανίας μετά το θάνατο του \nΑδόλφου Χίτλερ;":"Καρλ\nΝτένιτς",
            "Πότε έγινε η 1η Ιανουαρίου η πρώτη μέρα του έτους;":"46 π.Χ",
            "Ποια χρονιά έλαβε χώρα η πρώτη ελεγχόμενη \nπυρηνική αλυσιδωτή αντίδραση;":"1942",
            "Ποιο είναι το χημικό σύμβολο του σιδήρου;":"Fe",
            "Κατά μέσο όρο, πόσο καιρό ζει ένα ποντίκι \nστη φύση;":"6 μηνες",
            "Ποιο είναι το πρώτο στοιχείο στον περιοδικό πίνακα;":"Υδρογόνο",
            "Ποιο έτος ανακαλύφθηκαν οι ακτίνες Χ;":"1895",
            "Πόσα γήινα χρόνια είναι ένα έτος στον Δία;":"11.9",
            "Πόσα φεγγάρια έχει ο Άρης;":"2",
            "Πόσες καρδιές έχει ένα χταπόδι;":"3",
            "Ποιο στοιχείο έχει το χημικό σύμβολο Au;":"Χρυσός",
            "Πόσα αστέρια είναι στη Μεγάλη Άρκτος;":"7",
            "Πώς γράφετε το 99 με λατινικούς αριθμούς;":"XCIX",
            "Ποια χρονιά έγινε ο Ναπολέων βασιλιάς της Ιταλίας;":"1805",
            "Σε ποιο νησί εξορίστηκε ο Ναπολέων το 1814;":"Έλβα",
            "Ποιος από τους παρακάτω Doom cheat codes έχει το \nδικό του παιχνίδι το όνομά του;":"idspispopd",
            "Πώς ονομαζόταν ο πρώτος ηλεκτρονικός \nυπολογιστής;":"ENIAC",
            "Πότε παρουσιάστηκε ο υπολογιστής Apple II;":"1977"
            }

# Labels:

question = QLabel("Εδώ θα εμφανίζονται οι ερωτήσεις και κάτω \nοι πιθανές απανήσεις.")

# Αρχικοποίηση παραθύρων:

window = QWidget()      # Κύριο παράθυρο
window.setWindowTitle("Ερωτήσεις!")
window.move(450, 300)

window.setFixedSize(650, 390)

# CSS Για την ομάδα κουμπιών και για το κουμπί υποβολής

window.setStyleSheet("""
                QGroupBox{
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #E0E0E0, stop: 1 #FFFFFF); /* Δημιουργεί ένα fade στο κουτί */
                    border: 2px solid gray;
                    border-radius: 5px;
                    margin-top: 1ex;      /* Αφήνει χώρο γύρο από τον τίτλο */
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    subcontrol-position: top center; /* Τοποθέτηση του τίτλου στο κέντρο */
                    padding: 0 3px;
                }

                QPushButton {
                    position: absolute;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #E0E0E0, stop: 1 #FFFFFF)
                }

                QRadioButton::indicator {
                    width: 13px;
                    height: 13px;
                }
                   """)

correct = QMessageBox()     # Παράθυρο σωστής απάντησης
correct.setIcon(QMessageBox.Information)
correct.setText("Η απάντησή σου είναι σωστή.")
correct.setStandardButtons(QMessageBox.Ok)


wrong = QMessageBox()       # Παράθυρο λάθος απάντησης
wrong.setIcon(QMessageBox.Critical)
wrong.setText("Η απάντησή σου είναι λάθος.")
wrong.setStandardButtons(QMessageBox.Ok)


# Κουμπιά // επιλογές:

button1 = QRadioButton("Επιλογή 1η")
button2 = QRadioButton("Επιλογή 2η")
button3 = QRadioButton("Επιλογή 3η")
button4 = QRadioButton("Επιλογή 4η")

submission = QPushButton("Ξεκίνα")

button1.setChecked(True)

on_off = QRadioButton(" Απενεργοποίηση\nμηνύματος ελέγχου")

# Λίστα κουμπιών:

ButtonList = [button1,button2,button3,button4]

# Layout Ερώτησης // Κουμπιού απάντησης:

row_Q = QHBoxLayout()

row_Q.addWidget(question, alignment= Qt.AlignCenter)

row_A = QHBoxLayout()

row_Q.addWidget(submission, alignment= Qt.AlignCenter)

# Layout Κουμπιών

group = QGroupBox("Επιλογές")

comb = QVBoxLayout()

row_Bup = QHBoxLayout()
row_Bdown = QHBoxLayout()

row_Bup.addWidget(button1, alignment = Qt.AlignCenter)
row_Bup.addWidget(button2, alignment = Qt.AlignCenter)

row_Bdown.addWidget(button3, alignment = Qt.AlignCenter)
row_Bdown.addWidget(button4, alignment = Qt.AlignCenter)

comb.addLayout(row_Bup)
comb.addLayout(row_Bdown)

group.setLayout(comb)

group.setFixedWidth(250)
group.setFixedHeight(200)

# Τελικό Layout:

total = QVBoxLayout()
total.addLayout(row_Q)
total.addWidget(group, alignment = Qt.AlignCenter)
total.addWidget(on_off, alignment = Qt.AlignRight)
total.addLayout(row_A)

window.setLayout(total)

# loop:

submission.clicked.connect(start_func)

window.show()
app.exec_()
