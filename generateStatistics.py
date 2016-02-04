from datetime import datetime, timedelta

class generateStats:

    def get_data(self, users, tagevent ):
        data = []

        one_month = datetime.now() - timedelta(weeks=4)
        one_month_events = tagevent.query.filter(tagevent.timestamp > one_month).all()

        data.append(self.get_allGenderData(users))
        data.append(self.get_genderTagData(users, one_month_events))
        data.append(self.get_taginsByMonth(tagevent))
        return data

    def get_allGenderData(self, users):
        maleCounter = 0
        femaleCounter = 0
        unknownCounter = 0

        for hit in users:

            js = hit.gender

            if js == "male":
                maleCounter += 1
            if js == "female":
                femaleCounter += 1
            if js == "unknown":
                unknownCounter += 1

        return [maleCounter, femaleCounter, unknownCounter]

    def get_genderTagData(self, users, one_month_events):
        maleCounter = 0
        femaleCounter = 0
        unknownCounter = 0

        for event in one_month_events:

            for user in users:

                if str(user.tag_id) == str(event.tag_id):
                    if user.gender == "male":
                        maleCounter += 1
                    if user.gender == "female":
                        femaleCounter += 1
                    if user.gender == "unknown":
                        unknownCounter += 1

        return [maleCounter, femaleCounter, unknownCounter]

    def get_taginsByMonth(self, event):
        yearArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        now = datetime.now()
        currentYear = str(now.year)

        timestamps = event.query.filter(event.timestamp.contains(currentYear)).all()

        for timestamp in timestamps:

            for x in range(1, 13):

                if x == timestamp.timestamp.month:
                    yearArr[x-1] += 1

        yearArr.append(int(currentYear))
        return yearArr