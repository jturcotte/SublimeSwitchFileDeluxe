import sublime, sublime_plugin
import os.path
import platform
import re

def compare_file_names(x, y):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        return x.lower() == y.lower()
    else:
        return x == y

def commonBase(fileName, extensions):
    base = fileName
    ext = ''
    for e in extensions:
        match = re.match('(.*)(' + re.escape(e) + ')$', fileName)
        if match and base.startswith(match.group(1)):
            base = match.group(1)
            ext = match.group(2)
    return base, ext

class SwitchFileDeluxeCommand(sublime_plugin.WindowCommand):
    def run(self, extensions=[], paths=['.']):
        if not self.window.active_view():
            return

        if '.' not in paths:  # always search in same path
            paths.append('.')

        path = self.window.active_view().file_name()
        if not path:
            return

        dir, file = os.path.split(path)
        base, ext = commonBase(file, extensions)

        start = 0
        count = len(extensions)


        if ext != "":
            for i in range(0, len(extensions)):
                if compare_file_names(extensions[i], ext):
                    start = i + 1
                    count -= 1
                    break

        dirsWithOpenedFiles = set([os.path.dirname(v.file_name()) for v in self.window.views() if v.file_name()])

        for i in range(0, count):
            idx = (start + i) % len(extensions)

            new_file = base + extensions[idx]

            for relative_path in paths:
                new_path = os.path.normpath(os.path.join(dir, relative_path, new_file))
                if os.path.exists(new_path):
                    self.window.open_file(new_path)
                    return
            for d in dirsWithOpenedFiles:
                if os.path.exists(os.path.join(d, new_file)):
                    self.window.open_file(os.path.join(d, new_file))
                    return

        # Fallback to the Goto menu only if the file matches one of the extensions.
        if base != file:
            sublime.status_message("No file to switch found in directories of opened files, showing the Goto menu.")
            self.window.run_command("show_overlay", {"overlay": "goto", "text": base})
