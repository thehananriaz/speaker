import os

if __name__ == '__main__':
        while True:
            x=input("What do you want to say: ")
            if x=="exit":
                os.system("say 'bye'")
                break
            command= f"say {x}"
            os.system(command)
