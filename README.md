# comment2card

Add comments as note cards to the project boards. Designed for copy-pasting URLs from the browser.

    $ # Add GitHub token to ~/.rexim-config
    $ list_projects.py https://github.com/morganey-lang/Morganey
    77801: Morning Tsoding
        167646: Planned
        167647: In Progress
        491004: Done (25.12.2016)
        423150: Done (04.12.2016)
        398176: Done (27.11.2016)
        373654: Done (20.11.2016)
        ...
    $ # Add column id 167646 to ~/.rexim-config
    $ make_note.py https://github.com/morganey-lang/Morganey/issues/281#issuecomment-256299869
