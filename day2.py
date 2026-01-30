student_id = input("ID: ")
Email_id =input("Email: ")
Password = input("Password: ")
referral_code = input("Referral Code: ")

if student_id[0:3]=="CSE" and student_id[3]=="-" and student_id[4].isdigit() and student_id[5].isdigit() and student_id[6].isdigit():
    if Email_id.count("@")>=1 and Email_id.count(".")>=1 and Email_id[0]!="@" and Email_id[len(Email_id)-1]!="@" and Email_id[len(Email_id)-4:len(Email_id)]==".edu":
        if len(Password)>=8 and Password[0]>='A' and Password[0]<='Z' and Password.count("0")+Password.count("1")+Password.count("2")+Password.count("3")+Password.count("4")+Password.count("5")+Password.count("6")+Password.count("7")+Password.count("8")+Password.count("9")>=1 :
          if referral_code[0:3]=="REF" and referral_code[3].isdigit() and referral_code[4].isdigit() and referral_code[len(referral_code)-1]=="@":
              print("APPROVED")
          else :
              print("REJECTED")
        else :
            print("REJECTED")
    else:
        print("REJECTED")
else:
    print("REJECTED")


