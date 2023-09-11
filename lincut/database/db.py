class DataBase:
    def __init__(self):
        self.MessagesDB = {}
        self.DrUsersDB = {}
        self.PatientUsersDB = {}
        self.GroupsDB = {}
        self.ChannelsDB = {}
        self.CalendarDB = {}
        self.SessionsDB = {}
        self.VisionDB = {}
        self.AIModels = {}

    def addDrUser(self, user):
        self.DrUsersDB[user.id] = user
        return user

    def addPatientUser(self, user):
        self.DrUsersDB[user.id] = user
        return user

    def searchDr(self, id):
        return self.DrUsersDB[id] if id in self.DrUsersDB else None

    def searchPatient(self, id):
        return self.PatientUsersDB[id] if id in self.PatientUsersDB else None

    def searchUser(self, id):
        return self.searchDr(id) if self.searchDr(id) else self.searchPatient(id)

    def searchUserByEmail(self, email):
        for user in self.DrUsersDB.values():
            if user.email == email:
                return user
        for user in self.PatientUsersDB.values():
            if user.email == email:
                return user
        return None

    def searchUserByPhone(self, phone):
        for user in self.DrUsersDB.values():
            if user.phone_number == phone:
                return user
        for user in self.PatientUsersDB.values():
            if user.phone_number == phone:
                return user
        return None

    def searchUserByPhoneOrEmail(self, phone_or_email):
        user = self.searchUserByEmail(phone_or_email)
        if user:
            return user
        return self.searchUserByPhone(phone_or_email)

    def editUser(self, user):
        if user.id in self.DrUsersDB:
            self.DrUsersDB[user.id] = user
        elif user.id in self.PatientUsersDB:
            self.PatientUsersDB[user.id] = user
        else:
            return None
        return user

    def deleteUser(self, id):
        if id in self.DrUsersDB:
            del self.DrUsersDB[id]
        elif id in self.PatientUsersDB:
            del self.PatientUsersDB[id]
        else:
            return None
        return id

    def addCalendar(self, data, calendar):
        calendar.id = len(data) + 1
        self.CalendarDB[calendar.id] = calendar
        return calendar

    def searchCalendar(self, id, user_id):
        return (
            self.CalendarDB[id]
            if id in self.CalendarDB and self.CalendarDB[id].user_id == user_id
            else None
        )

    def UserCalendar(self, user_id):
        return [
            calendar
            for calendar in self.CalendarDB.values()
            if calendar.user_id == user_id
        ]

    def editCalendar(self, calendar):
        if calendar.id in self.CalendarDB:
            self.CalendarDB[calendar.id] = calendar
        else:
            return None
        return calendar

    def editUserCalendar(self, user_id, calendar):
        if (
            calendar.id in self.CalendarDB
            and self.CalendarDB[calendar.id].user_id == user_id
        ):
            self.CalendarDB[calendar.id] = calendar
        else:
            return None
        return calendar

    def Pagination(self, data, page, limit):
        if page is None and limit is None:
            return data
        if page is None:
            page = 1
        else:
            page = int(page)
        if limit is None:
            limit = 10
        else:
            limit = int(limit)
        start = (page - 1) * limit
        end = start + limit
        if start > len(data):
            return None
        if end > len(data):
            end = len(data)
        return data[start:end]

    def deleteCalendar(self, id):
        if id in self.CalendarDB:
            del self.CalendarDB[id]
        else:
            return None
        return id

    def authenicate(self, email, password):
        user = self.searchUserByEmail(email)
        if user and user.password == password:
            return user
        return None

    def addMessage(self, message):
        message.id = len(self.MessagesDB) + 1
        self.MessagesDB[message.id] = message
        return message

    def searchMessage(self, id):
        return self.MessagesDB[id] if id in self.MessagesDB else None

    def UserMessages(self, user_id):
        return [
            message for message in self.MessagesDB.values() if message.sender == user_id
        ] + [
            message
            for message in self.MessagesDB.values()
            if message.reciver == user_id
        ]

    def deleteMessage(self, message_id):
        if message_id in self.MessagesDB:
            del self.MessagesDB[message_id]
        else:
            return None
        return message_id

    def editMessage(self, message):
        if message.id in self.MessagesDB:
            self.MessagesDB[message.id] = message
        else:
            return None
        return message

    def addAIModel(self, model):
        model.id = len(self.AIModels) + 1
        self.AIModels[model.id] = model
        return model

    def searchAIModel(self, id):
        return self.AIModels[id] if id in self.AIModels else None

    def searchAIModelByName(self, name):
        for model in self.AIModels.values():
            if model.name == name:
                return model
        return None

    def editAIModel(self, model):
        if model.id in self.AIModels:
            self.AIModels[model.id] = model
        else:
            return None
        return model

    def deleteAIModel(self, id):
        if id in self.AIModels:
            del self.AIModels[id]
        else:
            return None
        return id

    def addSession(self, session):
        session.id = len(self.SessionsDB) + 1
        self.SessionsDB[session.id] = session
        return session

    def searchSession(self, id):
        return self.SessionsDB[id] if id in self.SessionsDB else None

    def searchSessionByUser(self, user_id):
        return [
            session
            for session in self.SessionsDB.values()
            if session.user_id == user_id
        ]

    def editSession(self, session):
        if session.id in self.SessionsDB:
            self.SessionsDB[session.id] = session
        else:
            return None
        return session

    def deleteSession(self, id):
        if id in self.SessionsDB:
            del self.SessionsDB[id]
        else:
            return None
        return id

    def addVision(self, vision):
        vision.id = len(self.VisionDB) + 1
        self.VisionDB[vision.id] = vision
        return vision
