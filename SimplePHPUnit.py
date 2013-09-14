import os
import sys
import shlex
import subprocess
import sublime
import sublime_plugin

if sys.version_info < (3, 3):
    raise RuntimeError('SimplePHPUnit works with Sublime Text 3 only')

SPU_THEME = 'Packages/SimplePHPUnit/SimplePHPUnit.hidden-tmTheme'
SPU_SYNTAX = 'Packages/SimplePHPUnit/SimplePHPUnit.hidden-tmLanguage'

class ShowInPanel:
    def __init__(self, window):
        self.window = window

    def display_results(self):
        self.panel = self.window.get_output_panel("exec")
        self.window.run_command("show_panel", {"panel": "output.exec"})

        self.panel.settings().set("color_scheme", SPU_THEME)
        self.panel.set_syntax_file(SPU_SYNTAX)

class SimplePhpUnitCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(SimplePhpUnitCommand, self).__init__(*args, **kwargs)
        settings = sublime.load_settings('SimplePHPUnit.sublime-settings')
        self.phpunit_path = settings.get('phpunit_path')

    def run(self, *args, **kwargs):
        try:
            # The first folder needs to be the Laravel Project
            self.PROJECT_PATH = self.window.folders()[0]
            if os.path.isfile("%s" % os.path.join(self.PROJECT_PATH, 'phpunit.xml')) or os.path.isfile("%s" % os.path.join(self.PROJECT_PATH, 'phpunit.xml.dist')):
                self.params = kwargs.get('params', False)
                self.args = [self.phpunit_path, '--stderr']
                if self.params is True:
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
            self.run_shell_command(self.args, self.PROJECT_PATH)
        except IOError:
            sublime.status_message('IOError - command aborted')

    def run_shell_command(self, command, working_dir):
            self.window.run_command("exec", {
                "cmd": command,
                "shell": False,
                "working_dir": working_dir
            })
            self.display_results()
            return True

    def display_results(self):
        display = ShowInPanel(self.window)
        display.display_results()

    def window(self):
        return self.view.window()
