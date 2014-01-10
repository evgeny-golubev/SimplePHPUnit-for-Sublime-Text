Simple PHPUnit commands
===============

This plugin allows you the run the PHPUnit tests using the Sublime Text interface, without having to open and use the command line.

### Available commands:

- `PHPUnit: Run`
- `PHPUnit: Run with params`

### Coloring output:

![Coloring output](https://raw.github.com/m0nah/SimplePHPUnit-for-Sublime-Text/master/Screen%20Shot.png)

### Installation:
Use Package Controller or create a the directory `SimplePHPUnit` in your Sublime Text Packages directory, and you're ready to go.

### Usage:
Press Cmd + Shift + P for the dropdown command list, search for `PHPUnit: `, and pick your command. Also you can use `Tools/PHPUnit...` menu item

### Keybinding:

You can use command `simple_php_unit` for your keybinding.

Example:

```json
{ "keys": ["super+ctrl+alt+t"], "command": "simple_php_unit" }
```

### Notes:
- PHPUnit config file needs to been in the root folder of your structure in the sidebar.
- You need insert in Sublime Text user settings `"show_panel_on_build": true` or use `Tools/Build Results/Show Build Results` menu item for view results.

Give some feedback.

Thanks.
