SublimeSwitchFileDeluxe
=======================

Switch header/source based on generic suffixes (not just the extension).

If a file can't be found in the same directory, the command also searches for it in the directory of other already opened files.
It can also search in relative paths specified with `"paths"` setting. For example if `"paths"` is `["..", "../impl", "internal"]`, then header/source will be searched in parent folder, in 'impl' sibling folder and in 'internal' subfolder.

Example
=======

Qt has private headers with a "<base>_p.h" suffix, and QtWebKit has platform specific implementation headers/sources with a "<base>Qt.<ext>" suffix.
The following keymap setting would allow switching between "File.cpp" -> "FileQt.cpp" -> "FileQt.h" -> "File.h" -> "File_p.h" -> "File_p_p.h" -> ...
It also would search for files in sibling `impl` and `include` folders.

    [
        { "keys": ["alt+o"], "command": "switch_file_deluxe", "args": {
            "extensions": [".cpp", ".cxx", ".cc", ".c", "Qt.cpp", "Qt.h", ".hpp", ".hxx", ".h", "_p.h", "_p_p.h", ".ipp", ".inl", ".m", ".mm"],
            "paths": ["../impl", "../include"]
        } }
    ]

**Note:** The dot has to be explicitely specified before extensions, unlike the standard switch_file command.
