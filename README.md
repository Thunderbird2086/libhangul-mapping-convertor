# libhangul mapping convertor
python helper script to convert [hangul keyboard mapping](https://github.com/libhangul/libhangul/tree/main/data/keyboards) for any keyboard.

When I switched my keyboard layout from QWERT to Colemak-DH (the physical layout), it became a disaster to type Korean on my Mac and Linux systems.
Because, IMEs designed to use English letters to convert to Korean letters so that Korean layout has been modified along with Colemak modification.
After research, I found [libhangul](https://github.com/libhangul/libhangul) uses mapping xml for Korean Input, which allows me to modify its
mapping xml for any physical keyboard layout.

On Mac, [구름 입력기](https://github.com/gureum/gureum) uses [libhangul](https://github.com/libhangul/libhangul), so the same approach can be applied.

## requirements
1. Input Method with [libhangul](https://github.com/libhangul/libhangul)
1. python3

## How to use
1. update [config.yaml](config.yaml) as needed
   ```yaml
   name: colemak-dh:crkbd:thunderbird2086
   conversions:
   - targets:
       - hangul-keyboard-2.xml
       - hangul-keyboard-2-full.xml
     mapping:
       e: f
       r: p
       t: b
       s: r
       d: s
   ```
   `name` is a reference and inserted into xml mapping
   ```xml
   <?xml version='1.0' encoding='utf-8'?>
   <hangul-keyboard id="2" type="jamo" converted="colemak-dh:crkbd:thunderbird2086">
   ```
   `targets` has mappig file names to be modified. In case [구름 입력기](https://github.com/gureum/gureum) is installed on a Mac, 
   it can be found under `/Library/Input Methods/Gureum.app/Contents/Frameworks/Hangul.framework/Versions/A/Resources/keyboards`.<br>
   `mappig` contains key mapping.  For instance, `e: f` changes key `e` to `f`.  Refer to the image below.
1. run `convert.py`, which requires _input path_ at least.
   ```shell
   $ python3 convert.py --help
   usage: Keyboard mapping convertor for libhangul [-h] [--config CONFIG] --in_path IN_PATH [--out_path OUT_PATH]
   
   optional arguments:
     -h, --help            show this help message and exit
     --config CONFIG, -c CONFIG
                           mapping confiiguration
     --in_path IN_PATH, -i IN_PATH
                           path for input files
     --out_path OUT_PATH, -o OUT_PATH
                           path for output files. Default is current directory.
   ```
 1. copy the output file to the input directory.
 1. enjoy
 
 * sample keyboard layout: [custom Colemak-DH layout](https://github.com/qmk/qmk_firmware/tree/master/keyboards/crkbd/keymaps/thunderbird2086)
   ![crkbd:thunderbird2086:colemak-dh:hangul-2-set](https://i.imgur.com/m52dZk0.png)
