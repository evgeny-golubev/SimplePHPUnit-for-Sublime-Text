import os
import shlex
import subprocess
import sublime
import sublime_plugin

class SimplePhpUnitCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(SimplePhpUnitCommand, self).__init__(*args, **kwargs)
        settings = sublime.load_settings('SimplePHPUnit.sublime-settings')
        self.phpunit_path = settings.get('phpunit_path', 'phpunit')

    def run(self, *args, **kwargs):
        try:
            # The first folder needs to be the Laravel Project
            self.PROJECT_PATH = self.window.folders()[0]
            if os.path.isfile("%s" % os.path.join(self.PROJECT_PATH, 'phpunit.xml')) or os.path.isfile("%s" % os.path.join(self.PROJECT_PATH, 'phpunit.xml.dist')):
                self.params = kwargs.get('params', False)
                self.args = [self.phpunit_path]
                if self.params is None:
                    self.window.show_input_panel('Params:', '', self.on_params, None, None)
                else:
                    self.on_done()
            else:
                sublime.status_message("phpunit.xml or phpunit.xml.dist not found")
        except IndexError:
            sublime.status_message("Please open a project with PHPUnit")

    def on_params(self, command):
        self.command = command
        self.args.extend(shlex.split(str(self.command)))
        self.on_done()

    def on_done(self):
        if os.name != 'posix':
            self.args = subprocess.list2cmdline(self.args)
        try:
            self.window.run_command("exec", {
                "cmd": self.args,
                "shell": False,
                "working_dir": self.PROJECT_PATH})
        except IOError:
            sublime.status_message('IOError - command aborted')
