from graphics import *
from userclass import*
from random import randint
from DailyMaintenance import *
from time import sleep
from symptomlogclass import *


def drawButton(pt1, pt2, color, label, win):
    button = Rectangle(pt1,pt2)
    button.setFill(color)
    button.draw(win)

    centerX, centerY = (pt1.getX()+pt2.getX())/2, (pt1.getY()+pt2.getY())/2
    button_label = Text(Point(centerX, centerY), label)
    button_label.setFill("white")
    button_label.draw(win)

def is_clicked(point, pt1, pt2):
    """Check if a point (mouse click) is inside a rectangle defined by pt1 and pt2."""
    return pt1.getX() <= point.getX() <= pt2.getX() and pt1.getY() <= point.getY() <= pt2.getY()


def main():

    win = GraphWin("Symptom Sync", 500, 750)

    win.setCoords(0, 0, 500, 750)
    

    background = Image(Point(0,0),"images/background.png")
    background.draw(win)

    calendartop = Image(Point(250,620),"images/calendartop.png")
    calendartop.draw(win)

    calendar = Image(Point(250,470), "images/calendar.png")
    calendar.draw(win)

    prompt = Image(Point(250,350), "images/prompt.png")
    prompt.draw(win)

    new_user=User(0,"John Doe",50,"male","","","",60,200)

    def undraw_all():
        calendartop.undraw()
        prompt.undraw()
        medicine.undraw()
        dailystat.undraw()
        symptomsummary.undraw()
        usericon.undraw()
        photo.undraw()
        symptom.undraw()
        calendar.undraw()

    def main_menu():
        calendartop.draw(win)
        prompt.draw(win)
        medicine.draw(win)
        dailystat.draw(win)
        symptomsummary.draw(win)
        usericon.draw(win)
        photo.draw(win)
        symptom.draw(win)
        calendar.draw(win)

    def hide_user_icon():
        name.undraw()
        age.undraw()
        gender.undraw()
        diagnosis.undraw()
        medication.undraw()
        allergies.undraw()
        height.undraw()
        weight.undraw()
        user_icon_submit.undraw()
        user_icon_button_label.undraw()

    def hide_daily_stat():
        sleep.undraw()
        heartrate.undraw()
        bloodpressure.undraw()
        progress_bar.undraw()
        progress_bar2.undraw()
        progress_bar3.undraw()
        progress_fill.undraw()
        progress_fill2.undraw()
        progress_fill3.undraw()
        daily_stat_submit.undraw()
        daily_stat_button_label.undraw()

    def hide_medicine():
        bottle.undraw()
        bottle_fill.undraw()
        medicine_button_plus.undraw()
        medicine_button_plus_label.undraw()
        medicine_button_minus.undraw()
        medicine_button_minus_label.undraw()
        medicine_exit_button.undraw()
        
        

    def find_points(width,height,center):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        ## you should comment these variables...
        xmax, xmin = x+w, x-w 
        ymax, ymin = y+h, y-h
        print("xmin:",xmin)
        print("xmax:",xmax)
        print("ymin",ymin)
        print("ymax",ymax)

    symptom = Image(Point(250,300),"images/symptom.png")
    symptom.draw(win)
    #320 x 51
    

    medicine = Image(Point(250,250),"images/medicine.png")
    medicine.draw(win)
    #320 x 53

    dailystat = Image(Point(250,200),"images/dailystat.png")
    dailystat.draw(win)
    #320 x 55

    symptomsummary = Image(Point(360,70),"images/symptomsummary.png")
    symptomsummary.draw(win)
    #240 x 74

    usericon = Image(Point(450,700),"images/usericon.png")
    usericon.draw(win)
    #80 x 66

    photo = Image(Point(120,70),"images/photo.png")
    photo.draw(win)
 

    while True:
        pt=win.getMouse()
        if is_clicked(pt,Point(90,274.5),Point(410,325.5)): #symptoms clicked##############################
            undraw_all()

            id_entry = Entry(Point(250, 650), 20)
            id_entry.setText("Enter your User ID")
            id_entry.draw(win)

            physical_symptom=Entry(Point(250,600), 30)
            physical_symptom.setText("Describe your physical symptom")
            physical_symptom.draw(win)
           
            physical_severity = Entry(Point(250,570), 30)
            physical_severity.setText("On a scale of 1 to 5, how severe is this symptom? ")
            physical_severity.draw(win)

            mental_symptom= Entry(Point(250,540), 30)
            mental_symptom.setText("Describe your mental symptom ")
            mental_symptom.draw(win)

            mental_severity= Entry(Point(250,510), 30)
            mental_severity.setText("On a scale of 1 to 5, how severe is this symptom? ")
            mental_severity.draw(win)
           

            symptoms_submit = Rectangle(Point(190,340),Point(310, 310))
            symptoms_submit.setFill("light blue")
            symptoms_submit.draw(win)

            centerX, centerY = (Point(190,340).getX()+Point(310, 310).getX())/2, (Point(190,340).getY()+Point(310, 310).getY())/2
            user_icon_button_label = Text(Point(centerX, centerY), "Submit")
            user_icon_button_label.setFill("white")
            user_icon_button_label.draw(win)

            while True:
                pt = win.getMouse()

                if 190 <= pt.getX() <= 310 and 310 <= pt.getY() <= 340:
                    
                    user_id = int(id_entry.getText())
                    physical_log= SymptomLog(symptom_type="physical", description=physical_symptom.getText(), severity=int(physical_severity.getText()))
                    mental_log = SymptomLog(symptom_type="mental", description=mental_symptom.getText(), severity=int(mental_severity.getText()))

                    if user_id in users_dict:
                        user = users_dict[user_id]
                        user.add_symptom_log(physical_log)
                        user.add_symptom_log(mental_log)

                        print(f"All symptom logs for {user.name}:")
                        for log in user.symptoms_logs:
                            print(log)
                
               
                        id_entry.undraw()
                        physical_symptom.undraw()
                        physical_severity.undraw()
                        mental_symptom.undraw()
                        mental_severity.undraw()
                        symptoms_submit.undraw()
                        user_icon_button_label.undraw()

                    confirmation = Text(Point(250, 100), "Symptoms added to calendar." + str(new_user.get_user_id()))
                    confirmation.setSize(16)
                    confirmation.draw(win)
                    time.sleep(5)
                    confirmation.undraw()
                main_menu()



            
            

            
        elif is_clicked(pt,Point(90,223.5),Point(410,276.5)): #medicine clicked##############################
            undraw_all()
            bottle=Rectangle(Point(150,300),Point(350,600))
            bottle.draw(win)

            amount=300
            bottle_fill=Rectangle(Point(150,300),Point(350,amount))
            bottle_fill.setFill("white")

            #def drawButton(pt1, pt2, color, label, win):
            medicine_button_plus = Rectangle(Point(150,240),Point(200,290))
            medicine_button_plus.setFill("green")
            medicine_button_plus.draw(win)
            centerX, centerY = (Point(150,240).getX()+Point(200,290).getX())/2, (Point(150,240).getY()+Point(200,290).getY())/2
            medicine_button_plus_label = Text(Point(centerX, centerY), "+")
            medicine_button_plus_label.setFill("white")
            medicine_button_plus_label.draw(win)

            medicine_button_minus = Rectangle(Point(300,240),Point(350,290))
            medicine_button_minus.setFill("red")
            medicine_button_minus.draw(win)
            centerX, centerY = (Point(300,240).getX()+Point(350,290).getX())/2, (Point(300,240).getY()+Point(350,290).getY())/2
            medicine_button_minus_label = Text(Point(centerX, centerY), "-")
            medicine_button_minus_label.setFill("white")
            medicine_button_minus_label.draw(win)

            medicine_exit_button = Rectangle(Point(200,150),Point(300,200))
            medicine_exit_button.setFill("light blue")
            medicine_exit_button.draw(win)
            centerX, centerY = (Point(200,150).getX()+Point(300,200).getX())/2, (Point(200,150).getY()+Point(300,200).getY())/2
            medicine_exit_button_label = Text(Point(centerX, centerY), "Exit")
            medicine_exit_button_label.setFill("white")
            medicine_exit_button_label.draw(win)

            pt=win.getMouse()

            while not is_clicked(pt,Point(200,150),Point(300,200)):
                if is_clicked(pt,Point(150,240),Point(200,290)):
                    amount+=10
                    bottle_fill.undraw()
                    bottle_fill=Rectangle(Point(150,300),Point(350,amount)).draw(win)
                    bottle_fill.setFill("white")
                    
                elif is_clicked(pt,Point(300,240),Point(350,290)):
                    amount-=10
                    bottle_fill.undraw()
                    bottle_fill=Rectangle(Point(150,300),Point(350,amount)).draw(win)
                    bottle_fill.setFill("white")
                    
                pt=win.getMouse()
            hide_medicine()
            main_menu()


        elif is_clicked(pt,Point(90,172.5),Point(410,227.5)): #daily stat clicked##############################
            undraw_all()
            sleep=Entry(Point(250,600), 30)
            sleep.setText("How much sleep did you get?")
            sleep.draw(win)

            heartrate=Entry(Point(250,525), 30)
            heartrate.setText("What is your heartrate?")
            heartrate.draw(win)

            bloodpressure=Entry(Point(250,450), 30)
            bloodpressure.setText("What is your blood pressure?")
            bloodpressure.draw(win)

            progress_bar=Rectangle(Point(170,570),Point(340,560))
            progress_bar.draw(win)
            progress_fill=Rectangle(Point(170,570),Point(340,560))

            progress_bar2=Rectangle(Point(170,495),Point(340,485))
            progress_bar2.draw(win)
            progress_fill2=Rectangle(Point(170,495),Point(340,485))

            progress_bar3=Rectangle(Point(170,420),Point(340,410))
            progress_bar3.draw(win)
            progress_fill3=Rectangle(Point(170,420),Point(340,410))

            daily_stat_submit = Rectangle(Point(190,340),Point(310, 310))
            daily_stat_submit.setFill("light blue")
            daily_stat_submit.draw(win)

            centerX, centerY = (Point(190,340).getX()+Point(310, 310).getX())/2, (Point(190,340).getY()+Point(310, 310).getY())/2
            daily_stat_button_label = Text(Point(centerX, centerY), "Submit")
            daily_stat_button_label.setFill("white")
            daily_stat_button_label.draw(win)

            #drawButton(Point(190,340), Point(310, 310), "light blue", "Submit", win) 
               
            pt = win.getMouse()
                
            if 190 <= pt.getX() <= 310 and 310 <= pt.getY() <= 340:
                    if int(sleep.getText())<5:
                        progress_fill.undraw()
                        progress_fill=Rectangle(Point(170,570),Point(210,560))
                        progress_fill.draw(win)
                        progress_fill.setFill("red")
                    elif 5<=int(sleep.getText())<8:
                        progress_fill.undraw()
                        progress_fill=Rectangle(Point(170,570),Point(260,560))
                        progress_fill.draw(win)
                        progress_fill.setFill("yellow")
                    elif int(sleep.getText())>=8:
                        progress_fill.undraw()
                        progress_fill=Rectangle(Point(170,570),Point(335,560))
                        progress_fill.draw(win)
                        progress_fill.setFill("green")
                    sleep.setText(sleep.getText()+" hours")

                    if 157 >= int(heartrate.getText())>=93:
                        progress_fill2.undraw()
                        progress_fill2=Rectangle(Point(170,495),Point(335,485))
                        progress_fill2.draw(win)
                        progress_fill2.setFill("green")
                    elif 83<=int(heartrate.getText())<93 or 157<int(heartrate.getText())<=167:
                        progress_fill2.undraw()
                        progress_fill2=Rectangle(Point(170,495),Point(260,485))
                        progress_fill2.draw(win)
                        progress_fill2.setFill("yellow")
                    elif int(heartrate.getText())<83 or int(heartrate.getText())>167:
                        progress_fill2.undraw()
                        progress_fill2=Rectangle(Point(170,495),Point(210,485))
                        progress_fill2.draw(win)
                        progress_fill2.setFill("red")
                    heartrate.setText(heartrate.getText()+" bpm")

                    if int(bloodpressure.getText())<=120:
                        progress_fill3.undraw()
                        progress_fill3=Rectangle(Point(170,420),Point(335,410))
                        progress_fill3.draw(win)
                        progress_fill3.setFill("green")
                    elif 120<int(bloodpressure.getText())<=159:
                        progress_fill3.undraw()
                        progress_fill3=Rectangle(Point(170,420),Point(260,410))
                        progress_fill3.draw(win)
                        progress_fill3.setFill("yellow")
                    elif int(bloodpressure.getText())>=160:
                        progress_fill3.undraw()
                        progress_fill3=Rectangle(Point(170,420),Point(210,410))
                        progress_fill3.draw(win)
                        progress_fill3.setFill("red")
                    bloodpressure.setText(bloodpressure.getText()+" millimeters of Hg")
                    update()
            time.sleep(5)
            hide_daily_stat()
            main_menu()
            

        elif is_clicked(pt,Point(240,33),Point(480,107)): #symptom summary clicked##############################
            print("wow!")
            undraw_all()

        elif is_clicked(pt,Point(410,667),Point(490,733)): #user icon clicked##############################
            undraw_all()
            
            name=Entry(Point(250,600), 30)
            name.setText("Enter your name: ")
            name.draw(win)
           
            age = Entry(Point(250,570), 30)
            age.setText("Enter your age: ")
            age.draw(win)

            gender= Entry(Point(250,540), 30)
            gender.setText("Enter your sex: ")
            gender.draw(win)

            diagnosis= Entry(Point(250,510), 30)
            diagnosis.setText("Enter any diagnosis you already have: ")
            diagnosis.draw(win)

            medication= Entry(Point(250,480), 30)
            medication.setText("Enter any medications you are on (comma-separated): ")
            medication.draw(win)

            allergies= Entry(Point(250,450), 30)
            allergies.setText("Enter your allergies you have(comma-separated): ")
            allergies.draw(win)

            height= Entry(Point(250,420), 30)
            height.setText("Enter your height(in inches): ")
            height.draw(win)

            weight= Entry(Point(250,390), 30)
            weight.setText("Enter your weight(in lbs): ")
            weight.draw(win)

            user_icon_submit = Rectangle(Point(190,340),Point(310, 310))
            user_icon_submit.setFill("light blue")
            user_icon_submit.draw(win)

            centerX, centerY = (Point(190,340).getX()+Point(310, 310).getX())/2, (Point(190,340).getY()+Point(310, 310).getY())/2
            user_icon_button_label = Text(Point(centerX, centerY), "Submit")
            user_icon_button_label.setFill("white")
            user_icon_button_label.draw(win)

            users_dict = {}
            
            pt = win.getMouse()
            
            if 190 <= pt.getX() <= 310 and 310 <= pt.getY() <= 340:
                new_user=User(randint(0, 1000),name.getText(),int(age.getText()),gender.getText(),diagnosis.getText(),medication.getText(),allergies.getText(),int(height.getText()),int(weight.getText()))
                users_dict[new_user.get_user_id()] = new_user

                confirmation = Text(Point(250, 100), "User created!\n Your User ID is " + str(new_user.get_user_id()))
                confirmation.setSize(16)
                confirmation.draw(win)
                time.sleep(5)
                confirmation.undraw()

                print("Current Users Dictionary:")
                for user_id, user in users_dict.items():
                    print("User ID:", user_id, ", User Details:", user)

            time.sleep(5)
            hide_user_icon()
            main_menu()

        else:##############################
            
            win.getMouse()

            win.close()

        pt=win.getMouse()


        

main()
