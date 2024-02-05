import datetime as dt
class Human:
    def __init__(self):   
        my_inputs=[{'my_name':"What is your Name? "},{'my_sex':"What is your sex? (Please indicate M for Male, F for Female or N for Non-Binary) "}, {'my_dob':"What is your Date of Birth? (Please use this format YYYY-mm-dd) "},{'my_city':"What City were you born in? "},{'my_sin':"What is your SIN? "}]
        print(f"{' Begin ':*^79}")
        print("You have 3 attempts to answer each question correctly!")
        for dict in my_inputs:
            for key, value in dict.items():
                print("\n")
                print(f"{'*':*^79}")
                attempts=4
                while True:
                    try:
                        my_answer=input(value)
                        setattr(self,key,my_answer)

                        if key=='my_name':
                            if len(my_answer)>=1:
                                self.my_name=my_answer.title()
                                break
                            else:
                                print("Name should have a length greater than 1!")
                                raise ValueError

                        elif key=='my_sex':
                            gender_options={'M','F','N'}
                            self.my_sex=my_answer.upper()
                            if self.my_sex not in gender_options:
                                raise ValueError
                            else:
                                break
                        
                        elif key=='my_dob':
                            self.my_dob=dt.datetime.strptime(self.my_dob,"%Y-%m-%d").date()
                            if type(self.my_dob) is not dt.date:
                                raise ValueError
                            elif self.my_dob>dt.date.today():
                                print("Your Date of Birth can't be greater than today's date!")
                                raise ValueError
                            elif dt.date.today().year-self.my_dob.year>=100:
                                print("Are you sure you are",dt.date.today().year-self.my_dob.year, "years old!")
                                age_question=input("Please Enter Y for Yes and N for No: ").upper()
                                age_set={'Y','N'}
                                if age_question in age_set:
                                    if age_question=='Y':
                                        break
                                    else:
                                        ValueError
                                else:
                                    print("You did not enter Y or N.")
                                    raise ValueError
                            else:
                                break
                        
                        elif key=='my_city':
                            if len(my_answer)>=1:
                                self.my_city=my_answer.title()
                                break
                            else:
                                print("City should have a length greater than 1!")
                                raise ValueError

                        elif key=='my_sin':
                            if not int(self.my_sin):
                                raise ValueError
                            else:
                                break
                        else:
                            break

                    except ValueError:
                        attempts-=1
                        error_messages={'my_name':"Please enter your Name.",'my_sex':"Your Sex should be a String and one letter to indicate your gender: 'M' for Male, 'F' for Female or 'N' for Non-Binary.",'my_dob':"Your DOB should be in this format 'YYYY-mm-dd'.",'my_city':"Your enter the city you were born in.",'my_sin':"Your SIN should be an Integer."}
                        if attempts>0:
                            print("You have", attempts,"attempts left!","Hint:",error_messages[key])
                            continue
                        else:
                            print("Learn from the mistake above and below and try again!")
                            raise
        print("\n")
        print(f"{' Questions Successfully Completed! ':*^79}")

    def who_am_i(self):
        gender={'M':'male','F':'female','N':'non-binary'}
        pronoun={'M':'He','F':'She','N':'They'}
        possessive={'M':'his','F':'her','N':'their'}
        plural={'M':'was','F':'was','N':'were'} 
        age=dt.date.today().year-self.my_dob.year
        satement=f"{self.my_name} is a {age} year old {gender[self.my_sex]}. {pronoun[self.my_sex]} {plural[self.my_sex]} born in {self.my_city} and {possessive[self.my_sex]} SIN # is {self.my_sin}."
        return satement

print("\n")

##"In order to use this class, please create an object using the class name. After creating the class, use the who_am_i() method to print the Human's information

You=Human()

print("\n")

print(You.who_am_i())



