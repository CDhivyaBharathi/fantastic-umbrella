import os 
import dropbox
#
class TransferData:
    def _init_(self , access_token):
        self.access_token = access_token
#
    def upload_file(self , file_from , file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root , dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.jooin(root , filename)
                relative_path = os.path.relpath(local_path , file_from)
                dropbox_path = os.path.join(file_tp , relative_path)

                with open(local_path , 'rb') as f:
                    dbx.files_upload(f.read() , dropbox_path , mode=writeMode('overwrite'))



def main():
    access_token = '7oIb_JFl1wAAAAAAAAAAAcC8-zzh4umzf5xgs43hdskmH1hxUtY5nXcCvn1R3992'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer:- "))
    file_to = input("enter the full path to upload to dropbox:- ")

    transferData.upload_file(file_from , file_to)
    print("file has been successfully moved !!!")

main()
