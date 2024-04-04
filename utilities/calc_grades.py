from requests import packages, Session
from utilities.env import URL, TOKEN_XPATH, TOKEN, ID, PASSWORD, GRADE_XPATH
from lxml.etree import HTML


def calc_grades(user, password):
    semesters = {"TOTAL": {"SEM9": 0, "SEM8": 0, "SEM7": 0, "SEM6": 0,
                           "SEM5": 0, "SEM4": 0, "SEM3": 0, "SEM2": 0,
                           "SEM1": 0, "TOTAL": 0},
                 "SEM9": {"ENT": 0, "EBMR": 0, "OPTH": 0, "FMIMC": 0},
                 "SEM8": {"OGYN2": 0, "PED2": 0, "MED3": 0, "SURG3": 0},
                 "SEM7": {"surg2": 0, "MED2": 0, "PED1": 0, "OGYN1": 0},
                 "SEM6": {"COM": 0, "SURG1": 0, "MED1": 0},
                 "SEM5": {"FCT": 0, "RLM": 0, "DERM": 0, "PSYC": 0, "BMSP": 0},
                 "SEM4": {"_1104": 0},
                 "SEM3": {"_1103": 0},
                 "SEM2": {"_1102": 0},
                 "SEM1": {"_1101": 0}
                 }
    num = {58: 1, 60: 5}
    try:
        packages.urllib3.disable_warnings()
        session = Session()
        req = session.get(URL, verify=False)
        token = HTML(req.text).xpath(TOKEN_XPATH)[0]
        req = session.post(f"{URL}/login", data={TOKEN: token, ID: user.id,
                                                 PASSWORD: password})
        if "login" in req.url:
            return "Incorrect password"

        req = session.get(f"{URL}/education/grades")
        dom = HTML(req.text)

        for semester in list(semesters.values())[num[user.batch]:]:
            for course in semester:
                try:
                    if dom.xpath(GRADE_XPATH.format(
                            course.strip("_"), 3))[0].text == "PC":
                        break
                    if dom.xpath(GRADE_XPATH.format(
                            course.strip("_"), 4))[0].text == "ر":
                        return "Error processing your grades"
                    semester[course] = int(dom.xpath(GRADE_XPATH.format(
                        course.strip("_"), 3))[0].text)
                except Exception:
                    return "Error processing your grades"

        for semester in list(semesters["TOTAL"]):
            semesters["TOTAL"][semester] = sum(semesters[semester].values())

        session.get(f"{URL}/logout")
        session.close()
        return semesters

    except Exception:
        return "An error occurred"
