import random
from model.Candidate import Candidate
from lib.JobCategories import JobCategories
from lib.Degrees import Degrees
from lib.Minors import Minors
from lib.CourseCatalog import CourseCatalog
from calculator.UtilityCalculator import UtilityCalculator


class CandidateFactory(object):
    """Generates Candidate criteria."""

    def __init__(self):
        super(CandidateFactory, self).__init__()
        random.seed()

    def generateCandidate(self, job_category):
        preferred_category = JobCategories.get(JobCategories, const_type=job_category)
        courses = [CourseCatalog.COURSES[random.choice(list(CourseCatalog.COURSES.keys()))] for _ in range(5)]
        skills = ['Java', 'Python', 'JavaScript' 'Git', 'Agile', 'HTML', 'CSS', 'Django', 'Vue', 'Gradle', 'Technial Writing']

        for course in courses:
            for skill in course['skills']:
                if skill not in skills:
                    skills.append(skill)

        years_experience = random.randint(0, 4)
        experience_category = None
        if years_experience > 0:
            experience_category = JobCategories.CONSTANTS[random.choice(list(JobCategories.CONSTANTS.keys()))]
            for extra_skill in self.generateExperienceSkills(experience_category):
                if extra_skill not in skills:
                    skills.append(extra_skill)

        projects = self.generateCandidateProjects(courses)

        minor_name = Minors.CONSTANTS[random.choice(list(Minors.CONSTANTS.keys()))] if random.randint(0, 1) else None

        candidate = Candidate(
            base_utility=0.0,
            preferred_category=preferred_category,
            courses=courses,
            gpa=round(random.randrange(2.0, 4.0) + random.random(), 2),
            skills=skills,
            years_experience=years_experience,
            experience_category=experience_category,
            projects=projects,
            min_salary=random.randrange(35000, 50000, 3000),
            degree_name=Degrees.get(Degrees, 'BACHELORS_CS'),
            minor_name=minor_name
        )

        calculator = UtilityCalculator()
        candidate.set_base_utility(calculator.calclulateCandidateBaseUtility(candidate))

        return candidate

    def generateCandidates(self, num_candidates, categories={'WEB_MOBILE': 0.6, 'DATA_SCIENCE_ML': 0.2, 'EMBEDDED_SYSTEMS': 0.1, 'GAME_DEV': 0.1}):
        candidates = []

        for category, percent in categories.items():
            for _ in range(int(num_candidates * percent)):
                candidates.append(self.generateCandidate(category))

        while len(candidates) < num_candidates:
            candidates.append(self.generateCandidate('WEB_MOBILE'))

        return candidates


    def generateExperienceSkills(self, job_category):
        add_skills = []
        skills_pool = []

        if 'WEB_MOBILE' == job_category:
            skills_pool = ['DevOps', 'C#', 'MySQL', 'Unit testing', 'PHP', 'Angular', 'TypeScript', 'Bootstrap', 'LESS', 'Postgres', 'MongoDB', 'JIRA', 'AWS', 'Ruby on Rails', 'Laravel', 'Symphony', 'Swift', 'ASP.NET', '.NET', 'Spring', 'jQuery', 'Node', 'Webpack', 'Yarn']
        elif 'DATA_SCIENCE_ML' == job_category:
            skills_pool = ['Big Data', 'Statistics', 'AWS', 'Hadoop', 'Storm', 'Hive', 'Spark', 'Node', 'Webpack', 'Yarn', 'MapReduce', 'ML', 'AI', 'Tableau', 'TensorFlow', 'Keras', 'Neural Networks']
        elif 'EMBEDDED_SYSTEMS' == job_category:
            skills_pool = ['C', 'C++', 'Assembly', 'Microcontrollers', 'Linux', 'Architecture', 'Embedded', 'Eclipse', 'State Machines', 'Kernel', 'RTOS']
        else:
            skills_pool = ['Unity', 'Maya', 'CryEngine', 'Unreal Engine', 'AI', 'Animation', 'Game Design', 'C++', 'C#', 'Gimp', 'Blender', 'Objective-C']

        num_skills = random.randint(3,7)
        while len(add_skills) < num_skills:
            choice = random.choice(skills_pool)
            if choice not in add_skills:
                add_skills.append(choice)

        return add_skills

    def generateCandidateProjects(self, courses):
        # please add any additional skills you can think of
        skills_pool = ['Django', 'JavaScript', 'Game development', 'Technial Writing', 'AI', 'ML', 'Web Application', 'Neural Networks', 'Cryptosystem', 'Embedded System', 'System design', 'Computer Vision', 'Compiliers', 'AWS', 'SQL', 'Node']
        projects = []

        for _ in range(random.randint(0,3)):
            temp_skills = []
            num_skills = random.randint(1,4)

            while len(temp_skills) < num_skills:
                choice = random.choice(skills_pool)
                if choice not in temp_skills:
                    temp_skills.append(choice)

            projects.append({'skills': temp_skills})

        return projects