import os
import dictionary_repository as dr
from datetime import datetime


class ProfileManipulator:
    def __init__(self, profile_name, x):
        self.profile_name = profile_name
        if self.check_if_profile_exists() == False:
            self.make_profile_folder()
            self.create_profile()

    def check_if_profile_exists(self):
        return bool(os.path.exists(f'player_profiles\\{self.profile_name}'))

    def make_profile_folder(self):
        old_directory = os.getcwd()
        os.chdir('player_profiles')
        os.mkdir(self.profile_name)
        os.chdir(old_directory)

    def create_profile(self):
        profile_dict = {}
        profile_dict['Name'] = self.profile_name
        profile_dict['titles'] = ['Initiate']
        profile_dict['Join Date'] = datetime.strftime(datetime.now(), "%m/%d/%Y")
        profile_dict['Profile age'] = None
        HSK_dict = {}
        HSK_dict['HSK Level'] = 0
        HSK_dict['HSK1 Points'] = 0
        HSK_dict['HSK2 Points'] = 0
        HSK_dict['HSK3 Points'] = 0
        HSK_dict['HSK4 Points'] = 0
        HSK_dict['HSK5 Points'] = 0
        self.profile_dict.append(profile_dict)
        dr.HSK_dictionary = HSK_dict
        dr.profile_dictionary = profile_dict
        for i in self.list:
            if not any(d['Name'] == i for d in self.dict):
                char_dict = {}
                char_dict['Name'] = i
                char_dict['Accuracy'] = 0
                char_dict['HSK_Level'] = self.test_HSK_level(i)
                char_dict['Weight'] = 0
                dr.character_dictionary.append(char_dict)

    def create_run_dict(self):
        pass


v = ProfileManipulator('Fritz', 'x')