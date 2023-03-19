The Trivia Game

Καλώς ήρθατε στο PyQt5 Trivia Game! Αυτό είναι ένα απλό παιχνίδι γνώσεων που δημιουργήθηκε με τη χρήση της Python3 και της PyQt5. Παρουσιάζει στο χρήστη
ένα σύνολο από 20 ερωτήσεις με απαντήσεις πολλαπλής επιλογής, όπου ο χρήστης πρέπει να επιλέξει μια απάντηση για να προχωρήσει στην επόμενη ερώτηση.

Απαιτήσεις

Για να εκτελέσετε αυτό το πρόγραμμα, θα πρέπει να έχετε εγκαταστήσει στον υπολογιστή σας τα ακόλουθα:

    Python 3
    PyQt5

    Καθώς και ένα σύνολο βιβλιοθηκών που συνοδεύουν την python3:
    
        Random
        Numpy 

Μπορείτε να εγκαταστήσετε το PyQt5 χρησιμοποιώντας το pip:

pip install PyQt5

Χρήση

Για να ξεκινήσετε το παιχνίδι, απλά εκτελέστε το αρχείο Trivia_Game.py στο τερματικό σας:

python3 Trivia_Game.py

Το παιχνίδι θα ξεκινήσει εξηγώντας την τοποθεσία των κουμπιών. Αφού πατηθεί το κουμπί "Ξεκίνα" θα σας παρουσιαστεί η πρώτη ερώτηση. Χρησιμοποιήστε τα
κουμπιά επιλογής για να επιλέξετε την απάντησή σας και κάντε κλικ στο κουμπί "Υποβολή" για να προχωρήσετε στην επόμενη ερώτηση. Μετά από κάθε απάντηση το
παιχνίδι θα σας ενημερώνει αν απαντήσατε σωστά ή όχι. Αυτή η λειτουργία μπορεί να απενεργοποιηθεί κάνοντας κλικ στο κουμπί επιλογής κάτω δεξιά.

Προσαρμογή

Αν θέλετε να προσθέσετε τις δικές σας ερωτήσεις στο παιχνίδι, μπορείτε να το κάνετε επεξεργάζοντας το αρχείο Trivia_Game.py. Απλά επεξεργαστείτε το
Questions_dict προσθέτοντας ως κλειδί την ερώτησή σας και ως τιμές τις 4 πιθανές απαντήσεις. Στη συνέχεια, επεξεργαστείτε το λεξικό Answers_dict
προσθέτοντας, και πάλι, την ίδια ερώτηση ως κλειδί και ως τιμή μόνο τη σωστή απάντηση.
Αυτή η μέθοδος είναι προσωρινή και πρόκειται να αλλάξει στην επόμενη έκδοση.

Άδεια χρήσης

Αυτό το έργο έγινε στο πλαίσιο της άσκησης "Φτιάξε ένα παιχνίδι γνώσεων".

