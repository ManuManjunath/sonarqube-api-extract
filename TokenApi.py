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

    def get_tokens(self):
        """
        List all users of the sonar instance, note this may require higher level access
        :return: list of tokens in json format
        """
        token_url = '%(base_url)s/api/user_tokens/search' % {'base_url': self.base_url}
        response = requests.get(token_url, auth=HTTPBasicAuth(username=self.user, password=self.password), verify=False)
        print(response.status_code)
        return response.json()


def main():
    """
    Get all tokens and print them
    :return: None
    """
    sonar = Sonar(user=ARGS.sonar_user, password=ARGS.sonar_password, base_url=ARGS.sonar_base_url)
    for token in sonar.get_tokens():
        print(token)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-suser', '--sonar_user', help='sonar user', required=True)
    PARSER.add_argument('-spwd', '--sonar_password', help='sonar password', required=False)
    PARSER.add_argument('-surl', '--sonar_base_url', help='sonar url', required=True)
    ARGS = PARSER.parse_args()
    main()
