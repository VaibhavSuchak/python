import os
if __name__=='__main__':
    print("Welcomee to robospeaker........ ")
    while True:
        x=input("Enter what you want me to speak:")
        if x=="z":
            os.system("say 'by by friend'")
            break
        command = f"{x}"
        os.system(command)