def safe_convert(value: str):
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


class Settings:
    def __init__(self, setting_names=None, settings_file='settings_file.txt'):
        if setting_names is None:
            setting_names = []
        self.settings_file = settings_file
        self.settings = {}

        try:
            with open(self.settings_file) as stored_settings:
                for line in stored_settings.read().splitlines():
                    name, value = line.split(" = ")
                    self.settings[name] = safe_convert(value)
        except FileNotFoundError:
            with open(self.settings_file, "w") as stored_settings:
                pass

        for name in setting_names:
            self.get(name)

    def get(self, name, default=None):
        if name not in self.settings and default is not None:
            self.settings[name] = default
            self.save(name)
        elif name not in self.settings:
            user_input = input("What value would you like for " + str(name) + "? ")
            self.settings[name] = safe_convert(user_input)
            self.save(name)

        return self.settings[name]

    def save(self, name=None):
        line_format = "{} = {}\n"
        if name is None:
            with open(self.settings_file, 'w+') as stored_settings:
                for name, value in self.settings.items():
                    stored_settings.write(line_format.format(name, value))
        else:
            with open(self.settings_file, "a+") as stored_settings:
                stored_settings.write(line_format.format(name, self.settings[name]))


