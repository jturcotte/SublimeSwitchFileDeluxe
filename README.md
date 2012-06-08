SublimeSwitchFileDeluxe
=======================

Switch header/source based on generic suffixes (not just the extension).

If a file can't be found in the same directory, the command also search for it in the directory of other already opened files.

Example
=======

Qt has private headers with a "<base>_p.h" suffix, and QtWebKit has platform specific implementation headers/sources with a "<base>Qt.<ext>" suffix.
The following keymap setting would allow switching between "File.cpp" -> "FileQt.cpp" -> "FileQt.h" -> "File.h" -> "File_p.h" -> "File_p_p.h" -> ...

    [
        { "keys": ["alt+o"], "command": "switch_file_deluxe", "args": {"extensions": [".cpp", ".cxx", ".cc", ".c", "Qt.cpp", "Qt.h", ".hpp", ".hxx", ".h", "_p.h", "_p_p.h", ".ipp", ".inl", ".m", ".mm"]} }
    ]

**Note:** The dot has to be explicitely specified before extensions, unlike the standard switch_file command.
