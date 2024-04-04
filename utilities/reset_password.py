from requests import packages, Session
from utilities.env import URL, TOKEN_XPATH, TOKEN, ID, PASSWORD
from lxml.etree import HTML


def reset_password(id, password):
    try:
        packages.urllib3.disable_warnings()
        session = Session()
        res = session.get(URL, verify=False)
        token = HTML(res.content).xpath(TOKEN_XPATH)[0]
        res = session.post(f"{URL}/login", data={TOKEN: token, ID: id,
                                                 PASSWORD: password})
        if "login" in res.url:
            return "Incorrect password"

        session.get(f"{URL}/logout")
        session.close()
        return True

    except Exception:
        return "An error occurred"
