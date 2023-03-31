# Trivia Game V0.3 #
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox)

from random import (choice, shuffle)
from numpy import array_split

from Questions import (Questions_dict, Answers_dict)

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
                    
        ButtonList = [btn_1,btn_2,btn_3,btn_4]      # Φτιάφε λίστα με κουμπιά
        
        shuffle(ButtonList)         # Ανακάτεψε τα κουμπιά
                    
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
                break
                        
        global_key = key
        
    except:     # Αφού τελειώσουν οι διαθέσιμες ερωτήσεις
        end_func()

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

def update_timer():
    global remaining_time

    remaining_time += -1

    if remaining_time >= 0:
        time_label.setText("Χρόνος που απομένει:\n%s" % str(remaining_time))
    else:
        timer.stop()

        time_window.show()

        end_func()
        
def end_func():

    global points
    
    group.hide()        # Κρύψε την ομάδα κουμπιών 
    submission.hide()   # Κρύψε το κουμπί υποβολής
    on_off.hide()       # Κρύψε το κουμπί on / off
    time_label.hide()   # Κρύψε τον χρόνο
        
    points = str(points)
    ans_lenght = len(Answers_dict)

    lenght = ans_lenght
    try:
        if points == "1":
            ap = "Από τις %s ερωτήσεις μόνο μια απαντήθηκε σωστά." % lenght
        elif points == "0":
            ap = "Από τις %s ερωτήσεις καμία δεν απαντήθηκε σωστά." % lenght
        elif points == str(ans_lenght):
            ap = "Όλες οι ερωτήσεις απαντήθηκαν σωστά."
        else:
            ap = "Από τις %s ερωτήσεις οι %s απαντήθηκαν σωστά." % (lenght, points)
            
    except:
        ap = "Δεν προσπάθησες καθόλου..."

    question.setText(ap)    # Δε τον αριθμό τον σωστών απαντήσεων


# Αρχικοποίηση global μεταβλητών

global button1
global button2
global button3
global button4

start_value = 0

# Labels:

question = QLabel("Εδώ θα εμφανίζονται οι ερωτήσεις και κάτω \nοι πιθανές απανήσεις.")

time_label = QLabel("Χρονόμετρο")

# Χρονόμετρο:

remaining_time = 120

timer = QTimer()
timer.setInterval(1000)

timer.timeout.connect(update_timer)

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

time_window = QMessageBox()
time_window.setIcon(QMessageBox.Warning)
time_window.setText("Τέλος χρόνου!")
time_window.setStandardButtons(QMessageBox.Ok)

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
