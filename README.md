# ScientificPythonWorshop
Repository of the Scientific Python Worshop at UOA

## Γενικά για το Workshop
Κάθε Τετάρτη -μετά το coffee break το τομέα αστροφυσικής- στις 13:30 - 15:00 στην αίθουσα διαλέξεων του Τομέα ΑΑΜ, πραγματοποιούνται workshops πάνω
σε ένα ευρύ φάσμα επιστημονικού προγραμματισμού και ανάλυσης δεδομένων με τη χρήση της γλώσσας προγραμματισμού Python και τις βιβλιοθήκες
Numpy, Scipy, Sympy, Pandas, Scikit-Learn και Matplotlib. Το περιβάλλον που θα χρησιμοποιούμε είναι το Jupyter Notebook.

Οι βιβλιοθήκες αυτές είναι εύκολα προσβάσιμες μέσω της πλατφόρμας Anaconda που είναι διαθέσιμη για Linux, Windows και Mac. (https://www.continuum.io/downloads).

Πληροφορίες: ekpa.highenergy@gmail.com // mighalis@gmail.com

Συντονιστές:
    Μιχάλης Παπαχρήστου (mighalis@gmail.com)
    Φώτης Αναγνωστόπουλος

Στο τελευταίο Workshop ο Αλέξανδρος Λουρόπουλος μας παρουσίασε το σύστημα κατανεμημένου ελέγχου (distributed version control system) git. Για όσους ενδιαφέρονται θα υπάρξει και συνέχεια.


### Επόμενο τακτικό Workshop >> Τετάρτη 28/2 στις 13.30 στην άιθουσα διαλέξεων του τομέα Αστροφυσικής
<!---
### Μέσα στην επόμενη εβδομάδα θα ανακοινωθεί και ενα doodle poll για τη χρήση ενός δεύτερου χρόνου συναντήσεων λόγω των σεμιναρίων του τομέα.
-->


### Notebooks
0. ***Εισαγωγικό tutorial, επίδειξη των δυνατοτήτων της Python***
https://github.com/UOAPythonWorkshop/WorkshopNotebooks/blob/master/Tutorial.ipynb

1. ***Δραστηριότητα 1: Γραμμική προσαρμογή δεδομένων με τη χρήση κοσμολογικών μοντέλων σε δεδομένα supernovae***
https://github.com/UOAPythonWorkshop/WorkshopNotebooks/blob/master/Linear_Regresion_ex_and_extras.ipynb

2. ***Δραστηριότητα 2: Εκτίμηση της περιόδου του ηλιακού κύκλου μέσω μετασχηματισμού fourier***
https://github.com/UOAPythonWorkshop/WorkshopNotebooks/blob/master/Sun%20Periodicity.ipynb

----------------------
Τα παρακάτω notebooks παρουσιάστηκαν και χρησιμοποιήθηκαν στα workshop της προηγούμενης περιόδου.

* ***Προσομοιώση κίνησης ενός βλήματος με μεθόδους αριθμητικής ολοκλήρωσης***
https://github.com/UOAPythonWorkshop/WorkshopNotebooks/blob/master/2nd%20Workshop.ipynb

* ***Εισαγωγή στη βιβλιοθήκη συμβολικών πράξεων SYMPY, παράδειγμα με ένα απλό πρόβλημα μηχανικής και του προβλήματος των 3 σωμάτων***
https://github.com/UOAPythonWorkshop/WorkshopNotebooks/blob/master/3rd%20Workshop%20(Sympy%20Tutorial).ipynb
(Το πρόβλημα των 3 σωμάτων λόγω χρόνου δεν έγινε στο workshop)

* ***Παρουσίαση στην αποθήκευση και ανάλυση δεδομένων αριθμητικών εξομοιώσεων από τον κώδικα PLUTO***
(για να αποθηκέυσει κάποιος τα δεδομένα απλά τρέχει το script PLUTOdata.py μέσω της εντολής python PLUTOdata.py εντός ενος φακέλου με dbl δεδομένα από τον PLUTO. Η διαδικασία αυτή δημιουργεί ένα npz αρχείο με το όνομα του φακέλου στο οποίο βρισκόμαστε καθώς και μερικά χαρακτηριστικά στιγμιότυπα σε μορφή png για μια πρώτη γέυση των αποτελεσμάτων. Για την ανάλυση τους μπορούμε να ανατρέξουμε τα δεδομένα μέσω της συνάρτηση np.load('arxeio.npz'))

πχ
```python
Data=np.load('arxeio.npz')
Density=Data['RHO'].T) #.Τ -> Transpose the Matrix
plt.imshow(Density[:,:,-1] #τελευταίο στιγμίοτυπο (Density[y,x,t])
```
