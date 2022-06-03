from dataclasses import dataclass
import requests
from getpass import getpass
import pathlib
import json


@dataclass
class JWTClient:
    """
    Use a dataclass decorator
    to simply the class construction
    """

    access: str = None
    refresh: str = None
    # ensure this matches your simplejwt config
    header_type: str = "Bearer"
    # this assumesy ou have DRF running on localhost:8000
    base_endpoint = "http://localhost:8000/api"
    # this file path is insecure
    cred_path: pathlib.Path = pathlib.Path("creds.json")

    def __post_init__(self):
        if self.cred_path.exists():
            """
            You have stored creds,
            let's verify them
            and refresh them.
            If that fails,
            restart login process.
            """
            try:
                data = json.loads(self.cred_path.read_text())
            except Exception:
                print("Assuming creds has been tampered with")
                data = None
            if data is None:
                """
                Clear stored creds and
                Run login process
                """
                self.clear_tokens()
                self.perform_auth()
            else:
                """
                `creds.json` was not tampered with
                Verify token ->
                if necessary, Refresh token ->
                if necessary, Run login process
                """
                self.access = data.get("access")
                self.refresh = data.get("refresh")
                token_verified = self.verify_token()
                if not token_verified:
                    """
                    This can mean the token has expired
                    or is invalid. Either way, attempt
                    a refresh.
                    """
                    refreshed = self.perform_refresh()
                    if not refreshed:
                        """
                        This means the token refresh
                        also failed. Run login process
                        """
                        print("invalid data, login again.")
                        self.clear_tokens()
                        self.perform_auth()
        else:
            """
            Run login process
            """
            self.perform_auth()
