import requests

class TelegramBot:
    def __init__(self, bot_token):
        self.bot_api = 'https://api.telegram.org/bot' + bot_token

    def get(self, method, params):
        url = self.bot_api + '/' + method
        response = requests.get(url , params=params)
        return response.json()


    def getMe(self):
        return self.get('getMe',{})

    def send(self, chat_id, message, message_type='text', reply_to_message_id=None):
        params = { 'chat_id' : chat_id }
        if reply_to_message_id :
            params['reply_to_message_id'] = reply_to_message_id
        if message_type == 'text':
            self.sendMessage(chat_id, message, reply_to_message_id)
        params[message_type] = message
        return self.get('send{}'.format(message_type.capitalize()), params)


    def sendMessage(self,chat_id, text, reply_to_message_id=None ):
        params = { 'chat_id': chat_id,
                    'text': text,
                  }
        if reply_to_message_id :
            params['reply_to_message_id'] = reply_to_message_id

        return  self.get('sendMessage',params)


    def forwardMessage(self, chat_id, from_chat_id, message_id):
        params = { 'chat_id': chat_id,
                    'from_chat_id': from_chat_id,
                    'message_id': message_id
                    }
        return self.get('forwardMessage',params)


    def sendUserProfilePhotos(self, user_id, offset=None, limit=None):
        params = { 'user_id' : user_id }
        if offset :
            params['offset'] = offset
        if limit :
            params['limit'] = limit
        return self.get('sendUserProfilePhotos',params)


    def getFile(self, file_id):
        return self.get('getFile', { 'file_id' : file_id})
    

    def kickChatMember(self, chat_id, user_id, until_date):
        params = { 'chat_id' : chat_id,
                    'user_id' : user_id,
                    'until_date' : until_date
                    }
        return self.get('kickChatMember', params)

    
    def unbanChatMember(self, chat_id, user_id):
        params = { 'chat_id' : chat_id,
                    'user_id' : user_id
                    }
        return self.get('unbanChatMember',params)

    
    def restrictChatMember(self,chat_id, user_id, permissions, until_dat):
        pass


    def promoteChatMember(self, chat_id, user_id, promotion):
        pass


    def setChatAdministratorCustomTitle(self, chat_id, user_id, custom_title):
        params = { 'chat_id' : chat_id,
                    'user_id' : user_id,
                    'custom_title' : custom_title
                    }
        return self.get('setChatAdministratorCustomTitle', params)

    
    def setChatPermissions(self, chat_id, permissions):
        pass

    
    def exportChatInviteLink(self, chat_id):
        return self.get('exportChatInviteLink', { 'chat_id' : chat_id})


    def setChatPhoto(self, chat_id, photo):
        params = { 'chat_id' : chat_id,
                    'photo' : photo
                    }
        return self.get('setChatPhoto',params)


    def setChatTitle(self, chat_id, title):
        params = { 'chat_id' : chat_id,
                    'title' : title
                    }
        return self.get('setChatTitle',params)


    def setChatDescription(self, chat_id, description):
        params = { 'chat_id' : chat_id,
                    'description' : description
                    }
        return self.get('setChatDescription',params)


    def pinChatMessage(self, chat_id, message_id, disable_notification=False):
        params = { 'chat_id' : chat_id,
                    'message_id' : message_id,
                    'disable_notification': disable_notification
                    }
        return self.get('pinChatMessage',params)


    def unpinChatMessage(self, chat_id):
        return self.get('unpinChatMessage',{ 'chat_id' : chat_id})


    def getChat(self, chat_id):
        return self.get('getChat', { 'chat_id' :chat_id})


    def getChatAdministrators(self, chat_id):
        return self.get('getChatAdministrators', {'chat_id':chat_id})


    def getChatMember(self, chat_id, user_id):
        params = { 'chat_id' : chat_id,
                    'user_id' : user_id
                    }
        return self.get('getChatMember', params)


    def editMessageText(self, chat_id, message_id, text ):
        params = { 'chat_id' : chat_id,
                    'message_id' : message_id,
                    'text' : text
                    }
        return self.get('editMessageText', params)


    def stopPoll(self, chat_id, message_id):
        params = { 'chat_id' :chat_id,
                    'message_id' : message_id
                    }
        return self.get('stopPoll', params)


    def deleteMessage(self, chat_id, message_id):
        params = { 'chat_id' : chat_id,
                    'message_id' : message_id
                    }
        return self.get('deleteMessage', params)






