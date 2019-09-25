from csv import DictReader
from os import path
from urllib.request import urlretrieve
from collections import Counter

DATA = path.join('tmp', 'bite_output_log.txt')
if not path.isfile(DATA):
    urlretrieve('https://bit.ly/2HoFZBd', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        rows = []
        with open(data, 'r', encoding='utf-8', newline='') as csvfile:
            reader = DictReader(csvfile)

            for row in reader:
                rows.append(row)

        return rows


    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return len({row['bite'] for row in self.rows})

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return len({row['bite'] for row in self.rows if row['completed'].lower() == "true"})

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return len({row['user'] for row in self.rows})

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        return len({row['user'] for row in self.rows if row['completed'].lower() == 'true'})

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        c = Counter([row['bite'] for row in self.rows])

        return c.most_common(1)[0][0]

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        c = Counter([row['user'] for row in self.rows if row['completed'].lower() == "true"])

        return c.most_common(1)[0][0]


if __name__ == "__main__":
    mycls = BiteStats()
    print(mycls.number_bites_accessed)
    print(mycls.number_bites_resolved)
    print(mycls.number_users_active)
    print(mycls.number_users_solving_bites)
    print(mycls.top_bite_by_number_of_clicks)
    print(mycls.top_user_by_bites_completed)

