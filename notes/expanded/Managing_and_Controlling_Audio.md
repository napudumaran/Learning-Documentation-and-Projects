# Managing and Controlling Audio (Linux CLI)

---

## 🎧 Listing Audio Output Devices

---

To see all available audio output devices (called *sinks*), run:

``` bash
pactl list short sinks
```

Here's a short breakdown of the command:
- `pactl` is a command-line tool for controlling PulseAudio (and PipeWire with compatibility)
- `list` means to show information about a specific object type
- `short` means to output the results in table form for readibility
- `sink` refers to audio output devices

This command basically says: "Show all sound output devices in a table format."

### Example of my output:

| 58 | alsa_output.usb-SteelSeries_SteelSeries_Arena_7-00.analog-stereo | PipeWire | s24le 2ch | 48000Hz | SUSPENDED |

| 89 | alsa_output.usb-Razer_Razer_Nari_Ultimate-00.pro-output-0        | PipeWire | s16le 1ch | 48000Hz | SUSPENDED |

| 90 | alsa_output.usb-Razer_Razer_Nari_Ultimate-00.pro-output-1        | PipeWire | s16le 2ch | 48000Hz | SUSPENDED |

Now that we see our audio output devices, we can reference them properly in commands.

For example, for more detailed info on a certain device we can run:

``` bash
pactl list sinks | grep -A20 "Name: alsa_output.usb-Razer_Razer_Nari_Ultimate-00.pro-output-1"
```

- `|` means to take the output of a command(s) and input it through another set of commands
- `grep` literally means global regular expression print, which basically means search for things that match this pattern
- `-A` is a flag that means "after"
- the `20` added to `-A` means to show only up to 20 lines of output

We mainly care about the
- Name:
- Sample Specs:
