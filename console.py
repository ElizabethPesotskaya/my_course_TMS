from providers.data_povider import DataProvider


class ConsoleDbApp:
    def __init__(self, raw_data_provider, orm_data_provider):
        self.data_provider: DataProvider | None = None
        self.raw_data_provider = raw_data_provider
        self.orm_data_provider = orm_data_provider

    def start_app(self):
        choose = int(input("Choose data provider for initialization: 1 - raw 2 "))
        self.data_provider = self.raw_data_provider if choose == 1 else self.orm_data_provider


        print("Starting ConsoleApp ...")
        self.data_provider.create_tables()



        while True:
            action_item = input("ACTION_ITEMS")


