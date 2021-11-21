import dropbox

class FileUpload:
    def __init__(self, acces_token):
        self.acces_token = acces_token
    
    def sendFile(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.acces_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    accessToken = "dOFJD-Rt5-AAAAAAAAAAAa7laaIznkbyeSRomDlReAPWFmON4H2Ue8CyIYHm5CjM"
    fileUpload = FileUpload(accessToken)

    fileFrom = input("enter the file you want to save: ")
    fileTo = input("enter where you save the file: ")

    fileUpload.sendFile(fileFrom,fileTo)
    print("file has been moved")

main()
