import pypyodbc as odbc
from prettytable import PrettyTable
# cur = conn.cursor();

#************************************************************************************#
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-MMUBQFK\SQLEXPRESS01'
DATABASE_NAME = 'Gestion'
# uid=<username>;
# pwd=<password>;

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={{{SERVER_NAME}}};
    DATABASE={{{DATABASE_NAME}}};
    Trust_Connection=yes;     
"""
try:
    conn = odbc.connect(connection_string)
    print("Connexion établie avec succès !")
    # Effectue les opérations souhaitées sur la base de données
except Exception as e:
    print("Erreur lors de la connexion à la base de données :", str(e))
cur = conn.cursor();    
#*************************************tsy miasa*********************************************#

def read(conn):
   print("Read")
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM employes")
   for row in cursor:
      print(f'row = {row}')
   print()
   
def create(conn):
   print("Creating")
   cursor = conn.cursor()
   cursor.execute(
      'INSERT INTO employes(nomEmp,prenomEmp,post,lieu) VALUES(?,?,?,?);',
      ('RAZAFIMANDIMBY','Lionot','USA','Google')
      )
   conn.commit()
   read(conn)
   
#******************************************Ending tsy miasa****************************************#
def showData():   
    # cur = conn.cursor();
    Query = "SELECT * FROM employes";
    cur.execute(Query);
    records = cur.fetchall();
    # print(records);
    table = PrettyTable(['Identification','Last name','First name','Post','Address']);
    for infos in records:
        table.add_row([infos['id'],infos['nom'],infos['prenom'],infos['post'],infos['lieu']]);
    print(table);    
    print("\nyou have been choose option show Data\n");


    
def DeleteData():
    print("You have been choose option Delete data\n");
    Id_Emp = int(input("Enter id to delete a employe:  "));
    print("\n");
    # print(Id_Emp);
    # cur = conn.cursor();
    Query = f"DELETE FROM employes WHERE id = {Id_Emp}";
    cur.execute(Query);
    conn.commit();
    refreshData(); 


    
def InsertData():
    print("You have been choose option Insert Data\n");
    # id = int(input("Enter your id: "));
    nom = input("Enter your Last name: ");
    prenom = input("Enter your First name: ");
    poste = input("Enter your Post: ");
    lieuEmp = input("Enter your Address: ");
    print("\n");
    # cur = conn.cursor();
    Query = f"INSERT INTO employes (nom, prenom, post, lieu) VALUES ('{nom}', '{prenom}', '{poste}', '{lieuEmp}')";
    cur.execute(Query);
    conn.commit();
    refreshData();
    


    
def UpdateData():
    print("You have been choose option Update Data\n");
    id = int(input("Enter your id: "));
    print("\n");
    
    #coucou
    Request = f"SELECT nom,prenom,post,lieu FROM employes WHERE id='{id}' ";
    cur.execute(Request);
    records = cur.fetchall();
    #print(records);
    
    if records:
        var1 = records[0]["nom"]
        var2 = records[0]["prenom"]
        var3 = records[0]["post"]
        var4 = records[0]["lieu"]
       # print(var1, var2, var3, var4)
    else:
        print("Aucun enregistrement trouvé")
    
    nom = input(f"You can change your Last name [{var1}]: ")
    if nom.strip() == "":
        nom = var1

    prenom = input(f"You can change your First name [{var2}]: ")
    if prenom.strip() == "":
        prenom = var2

    poste = input(f"You can change your Post [{var3}]: ")
    if poste.strip() == "":
        poste = var3

    lieuEmp = input(f"You can change your Address [{var4}]: ")
    if lieuEmp.strip() == "":
        lieuEmp = var4
    print("\n");
    
    #print(var1, var2, var3, var4)
    
    # Si l'utilisateur ne saisit rien, les variables gardent leur valeur d'origine var1, var2, var3 et var4
    # Sinon, les nouvelles valeurs saisies par l'utilisateur remplacent les anciennes valeurs
 
    Query = f"UPDATE employes SET nom='{nom}', prenom='{prenom}', post='{poste}', lieu='{lieuEmp}' WHERE id='{id}'";
    cur.execute(Query);
    conn.commit();
    refreshData();
    


def refreshData():   
    # cur = conn.cursor();
    Query = "SELECT * FROM employes";
    cur.execute(Query);
    records = cur.fetchall();
    # print(records);
    table = PrettyTable(['Identification','Last name','First name','Post','Address']);
    for infos in records:
        table.add_row([infos['id'],infos['nom'],infos['prenom'],infos['post'],infos['lieu']]);
    print(table);
    print("\nSuccess\n");
    
    
        
    
def ExitApp():
    print("You have been choose option exit\n");
    
def NotOption():
    print("You have been choose bad option\n");   
#**********************************************************************************#


option = None;

while(option != 0):

    print("\n**************************************");

    print("\n1: Show Data");
    print("2: Delete Data");
    print("3: Insert Data");
    print("4: Upadate Data");
    print("0: Exit\n");
   
    print("**************************************\n");

    option = int(input("Choose Option: "));
    print("\n");
    #print(f"You have selected: {option}")

    if(option == 1):
       showData();

    elif(option == 2):
       DeleteData();

    elif(option == 3):
       InsertData();

    elif(option == 4):
       UpdateData();

    elif(option == 0):
        ExitApp();

    else:
       NotOption();                         