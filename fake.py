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
        # get files from the server
        if self.job == lawyer:
            # request lawyer files
            f1 = utils.get_request(utils.SERVER_ADDRESS + "profile/lawyer")
        else:
            # request doctor files
            f1 = utils.get_request(utils.SERVER_ADDRESS + "profile/doctor")
        if self.sex == female:
            # request vacation files
            f2 = utils.get_request(utils.SERVER_ADDRESS + "profile/female")
        else:
            # request puppy files
            f2 = utils.get_request(utils.SERVER_ADDRESS + "profile/male")
        self.f1 = bytearray(f1)
        self.f2 = bytearray(f2)

    def extract_files(self):
        utils.unzip(self.f1, self.out_folder)
        utils.unzip(self.f2, self.out_folder)




# example
me = Profile("Maria", "Messick", "Lawyer", "Female", "/Users/mariamessick/Desktop/")
me.get_files()
me.extract_files()

