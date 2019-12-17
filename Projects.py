import argparse
import requests
from requests.auth import HTTPBasicAuth


class Sonar(object):
    """
    Create a base Sonar Class for connection and internal method calls
    """
    def __init__(self, user, password, base_url):
        """
        Parameters to create the class an any pre instantiation
        :param user: is the user or the token to connect.
        :param password: is the password associated to the user connecting. Note if you just have a user token leave password empty.
        :param base_url: is the base url without the ending slash
        """
        self.user = user
        if password is None:
            self.password = ""
        else:
            self.password = password
        self.base_url = base_url

    def get_projects(self, search_string):
        """
        Get list of all projects form sonar
        :return: list of tokens in json format
        """
        project_url = '%(base_url)s/api/projects/search?q=%(search_string)s' % {
            'base_url': self.base_url, 'search_string': search_string
        }
        response = requests.get(project_url, auth=HTTPBasicAuth(username=self.user, password=self.password), verify=False)
        return response.json()


def main():
    """
    Get all tokens and print them
    :return: None
    """
    sonar = Sonar(user=ARGS.sonar_user, password=ARGS.sonar_password, base_url=ARGS.sonar_base_url)
    for project in sonar.get_projects(ARGS.sonar_project_filter)['components']:
        print(project)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-suser', '--sonar_user', help='sonar user', required=True)
    PARSER.add_argument('-spwd', '--sonar_password', help='sonar password', required=False)
    PARSER.add_argument('-surl', '--sonar_base_url', help='sonar url', required=True)
    PARSER.add_argument('-project', '--sonar_project_filter', help='sonar project filter', required=True)
    ARGS = PARSER.parse_args()
    main()
