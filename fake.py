import shutil
import zipfile

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
        zip1 = ""
        zip2 = ""
        if self.job == lawyer:
            shutil.copyfile("/Users/mariamessick/Desktop/MIT/Work1.zip", self.out_folder+"SC_Cases.zip")
            zip1 = self.out_folder+"SC_Cases.zip"
        else:
            shutil.copyfile("/Users/mariamessick/Desktop/MIT/", self.out_folder+"Forms.zip")
            zip1 = self.out_folder+"Forms.zip"
        if self.sex == female:
            shutil.copyfile("/Users/mariamessick/Desktop/MIT/FamilyVacation.zip", 
                            self.out_folder + self.last + "_Vacation.zip")
            zip2 = self.out_folder + self.last + "_Vacation.zip"
        else:
            shutil.copyfile("/Users/mariamessick/Desktop/MIT/PuppyPics.zip", 
                            self.out_folder+"PuppyPics.zip")
            zip2 = self.out_folder+"PuppyPics.zip"

        zip_ref1 = zipfile.ZipFile(zip1, 'r')
        zip_ref1.extractall(self.out_folder)
        zip_ref1.close()

        zip_ref2 = zipfile.ZipFile(zip2, 'r')
        zip_ref2.extractall(self.out_folder)
        zip_ref2.close()

    def set_job(self, job):
        self.job = job

    def set_sex(self, sex):
        self.sex = sex

    def set_folder(self, folder):
        self.out_folder = folder


# example
me = Profile("Maria", "Messick", "Lawyer", "Female", "/Users/mariamessick/Desktop/")
me.get_files()
