from global_variables import GlobalVariables


class TextIsLongerThanMaxTextLengthException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.Text = f"Your note is longer than {GlobalVariables.MaxTextLength}"
