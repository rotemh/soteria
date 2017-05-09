import utils
import base64

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

        self.f1 = None
        self.f2 = None

    def get_files(self):
        # get files from the server
        if self.job == lawyer:
            # request lawyer files
            self.f1 = utils.get_request(utils.SERVER_ADDRESS + "profile/lawyer")
        else:
            # request doctor files
            self.f1 = utils.get_request(utils.SERVER_ADDRESS + "profile/doctor")
        # if self.sex == female:
        #     # request vacation files
        #     # self.f2 = utils.get_request(utils.SERVER_ADDRESS + "profile/female")
        # else:
        #     # request puppy files
        #     self.f2 = utils.get_request(utils.SERVER_ADDRESS + "profile/male")

        b64 = lambda x: base64.b64decode(x)
        self.f1 = b64(self.f1)
        # self.f2 = b64(self.f2)

    def extract_files(self):
        utils.unzip(self.f1, self.out_folder)
        # utils.unzip(self.f2, self.out_folder)



# example
me = Profile("Maria", "Messick", "Doctor", "Female", "/Users/rotemhemo/Desktop/time_capsule")
me.get_files()
print(me.f1)
me.extract_files()

