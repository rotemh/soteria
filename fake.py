import utils

lawyer = "Lawyer"
doctor = "Doctor"
female = "Female"
male = "Male"


class Profile(object):
    def __init__(self, first, last, job, sex, out_folder):
        self.first = first
        self.last = last
        self.job = job
        self.sex = sex
        self.out_folder = out_folder

    def get_files(self):
        # for now get files from local folder
        f1 = ""
        f2 = ""
        if self.job == lawyer:
            # request lawyer files
            f1 = utils.get_request("url")
        else:
            # request doctor files
            f1 = utils.get_request("url")
        if self.sex == female:
            # request vacation files
            f2 = utils.get_request("url")
        else:
            # request puppy files
            f2 = utils.get_request("url")
        self.f1 = f1
        self.f2 = f2

    def extract_files(self):
        utils.unzip(self.f1, self.out_folder)
        utils.unzip(self.f2, self.out_folder)




# example
me = Profile("Maria", "Messick", "Lawyer", "Female", "/Users/mariamessick/Desktop/")
me.get_files()
me.extract_files()

