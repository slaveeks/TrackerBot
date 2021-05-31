from sdk.codexbot_sdk import CodexBot
from config import APPLICATION_TOKEN, APPLICATION_NAME, SERVER, DB
from hello import CommandHello


class HelloWorld:

    def __init__(self):
        self.sdk = CodexBot(APPLICATION_NAME, SERVER['host'], SERVER['port'], db_config=DB, token=APPLICATION_TOKEN)

        self.sdk.log("Hw module initialized")

        self.sdk.register_commands([
            ('hello_world', 'Send hello', CommandHello(self.sdk)),
        ])

        self.sdk.start_server()



if __name__ == "__main__":
    hw = HelloWorld()
