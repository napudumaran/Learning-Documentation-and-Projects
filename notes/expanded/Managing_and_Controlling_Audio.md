All audio device outputs can be listed via:

pactl list short sinks

- pactl is PulseAudio/PipeWire audio tool, built to use CLI (Command-Line Interface)]
- list means to show information about objects in this category 
- short gives us the output into table form instead of a wall of text
- sink is just computer jargon for audio output device

This command basically says: show all sound output devices in a table

This is an example of my output:

alsa_output.usb-Razer_Razer_Nari_Ultimate-00.pro-output-1   RUNNING
alsa_output.usb-SteelSeries_SteelSeries_Arena_7-00.analog-stereo  IDLE

Now that we see our audio output devices, we can reference them properly in commands.

For example, for more detailed info on a certain device we can run:

pactl list sinks | grep -A20 "Name: alsa_output.usb-Razer_Razer_Nari_Ultimate-00.pro-output-1"

- | means to take the output of a command(s) and input it through another set of commands
- grep literally means global regular expression print, which basically means search for things that match this pattern
- `-A` is a flag that means "after"
- the `20` added to `-A` means to show only up to 20 lines of output

We mainly care about the
- Name:
- Sample Specs:
