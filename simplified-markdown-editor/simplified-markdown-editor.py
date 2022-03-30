class MarkdownEditor:

    def __init__(self):
        pass

    format = ("plain", "bold", "italic", "header",
                            "link", "inline-code", "ordered",
                            "list", "unordered-list", "new-line")

    special_commands = "!help", "!done"

    commands = (*format, *special_commands)

    def show_help(self):
        print("Available formatters:", *self.format)
        print("Special commands:", *self.special_commands)

    def correctly_input_command(self, string):
        user_input = input(string)
        while user_input not in self.commands:
            print("Unknown formatting type or command")
            user_input = input(string)
        return user_input

    def menu_options(self):
        option = self.correctly_input_command("Choose a formatter: > ")
        if option == "!help":
            self.show_help()
            self.menu_options()
        elif option == "!done":
            return


mde = MarkdownEditor()
mde.menu_options()
