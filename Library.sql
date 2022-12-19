create database Library;
use Library;
create table books (BCODE int,BNAME varchar(50),Author varchar(30),QTY int);
create table users (BID int,NAME varchar(50),BCODE int,ISSUING_DATE date,RETURN_DATE date);
insert into books values(1,"THE ART OF WAR","SUN TEU",8),(2,"THE CIVIL WAR IN FRANCE","K.H.MARX",5),(3,"UZUMAKI","JUNJIO ITO",1),(4,"MOLOTOV REMEBERS","ALBERT REISES",3),(5,"THE PHENOMENOLOGY OF SPIRIT","GEORGE F. HEGEL",4),(6,"BLACK SKIN WHITE MASK","FRANZ FANON",2),(7,"IMPERISALISM IN 21ST CENTURY","JOHN SMITH",1),(8,"THE WAR OF WORLDS","H.G. WELLS",3),(9,"MUSIC THEORY FOR DUMMIES","M. PILHOFER",1),(10,"PHYSICS CLASS XII","NCERT",10),(11,"THE WRETCHED OF THE EARTH","FRANZ FANON",9),(12,"CRIME AND PUNISHMENT","FYODOR DOSTOEVSKY",13),(13,"THE STORY OF MY EXPERIMENTS WITH TRUTH","M.K GANDHI",8),(14,"CYBERNETICS REVOLUTIONARIES","EDEN MEDINA",3),(15,"JURASSIC PARK","MICHAEL CRICHTON",1),(16,"PRIDE AND PREJUDICE","JANE AUSTEN",5),(17,"THE LOST WORLD","MICHAEL CRICHTON",1),(18,"DEATH NOTE","TSUGUMI OHBA",1),(19,"ANTI-DUHRING","FRIEDRICH ENGELS",3),(20,"WHAT IS TO BE DONE?","V.I. ULYANOV",3),(21,"CRITIQUE OF PURE REASON","IMMANUEL KANT",1),(22,"THE SPIRIT OF HORSEPOWER","AMADEO BORDIGA",10),(23,"A CRITIQUE OF THE GERMAN IDEOLOGY","K.H.MARX",2),(24,"FIVE POINT SOMEONE","CHETAN BHAGAT",3),(25,"THE SORCERER'S STONE","J.K ROWLING",3),(26,"THE ORIGIN OF THE GREAT PURGE","J. ARCH GETTY",2),(55,"HITCHHIKERS GUIDE TO THE GALAXY","DOUGLAS ADAMS",1),(134,"THE LEGEND OF THE SLEEPY HOLLOW","WASHINGTON ERWING",9);
insert into users values(1,"Rahul Saini",3,'2021-02-25','2021-03-04'),(2,"Kuvam Sethi",1,'2021-02-02','2021-02-09'),(3,"Dhairya Kumar",134,'2021-02-12','2021-02-19'),(4,"Anita Ratan",16,'2021-02-28','2021-03-07'),(5,"Nabhi Jain",8,'2021-03-03','2021-03-10'),(6,"Aakriti Jain",21,'2021-03-01','2021-03-08'),(7,"Rohan Chadha",13,'2021-02-27','2021-03-06'),(8,"Salim Merchant",20,'2021-02-12','2021-02-19'),(9,"Sonu Nigam",9,'2021-02-09','2021-02-16'),(10,"Abhishek Saxena",10,'2021-02-27','2021-03-06');