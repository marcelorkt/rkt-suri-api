from configurations import config
from classes.Request import Request
from classes.Sheets import Sheets
from classes.User import User
from classes.Messages import Messages

def insert_user():
    try:
        user_list = User.get_all_users()
        worksheet = Sheets(config("WORKSHEET_URL"), 0)
        worksheet.clear_sheet(True)
        worksheet.update_batch(user_list, "AC", "Usuários adicionados")
    except Exception as e:
        print(e)
    
def clear_sh():
    worksheet = Sheets(config("WORKSHEET_URL"), 0)
    worksheet.clear_sheet(True)
    

def get_user_message():
    user_list = User.get_all_users()
    user = Messages(user_list[0])
    for i in user.messages:
            if i['type'] == 'UserMessage':
                print(i['text'])
    
    
    
def main():
    # get_user_message()
    insert_user()
    # clear_sh()
        
main()